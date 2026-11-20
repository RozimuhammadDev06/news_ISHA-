import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {Presentation, PresentationFile} from '@oai/artifact-tool';

const root = 'C:/Users/user/Desktop/bbc/docs/backend-slides';
const build = path.join(root,'build');
const skill = 'C:/Users/user/.codex/plugins/cache/openai-primary-runtime/presentations/26.1112.11217/skills/presentations';
const runtime = 'C:/Users/user/.cache/codex-runtimes/codex-primary-runtime/dependencies';
process.env.RUNTIME_NODE_MODULES=path.join(runtime,'node/node_modules');
const deck = Presentation.create({slideSize:{width:1280,height:720}});
const C={ink:'#102A43',muted:'#526779',blue:'#0869CE',paper:'#F7FAFD',white:'#FFFFFF'};
function text(s,value,x,y,w,h,size=27,color=C.ink,bold=false){
  const box=s.shapes.add({geometry:'textbox',name:value.slice(0,45),position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
  box.text=value;
  box.text.style={fontFamily:'Arial',fontSize:size,color,bold};
  return box;
}
function slide(title,subtitle='',notes=''){
  const s=deck.slides.add(); s.background.fill=C.paper;
  text(s,title,64,46,1152,74,46,C.ink,true);
  if(subtitle)text(s,subtitle,64,132,1152,54,25,C.muted);
  text(s,String(deck.slides.items.length).padStart(2,'0'),1164,662,52,28,17,C.muted);
  s.speakerNotes.text=notes;
  return s;
}
function row(s,label,value,y){
  text(s,label,64,y,190,32,21,C.blue,true);
  text(s,value,280,y-3,932,83,27);
}
const languages=[
 {name:'Python',framework:'Django va FastAPI',
  capability:'Veb-sayt, API, bot, avtomatlashtirish va AI xizmatlari bilan integratsiya.',
  strength:'Django tayyor admin, ORM va autentifikatsiya vositalarini beradi. FastAPI API yaratishga qulay.',
  example:'Yangiliklar portali, CRM yoki AI modeliga ulanadigan xizmat.',
  tradeoff:'CPUga og‘ir ishlar uchun alohida worker yoki optimallashtirilgan kutubxona kerak bo‘lishi mumkin.',
  sources:['https://www.djangoproject.com/start/overview/','https://fastapi.tiangolo.com/']},
 {name:'JavaScript / TypeScript',framework:'Node.js muhiti, Express va NestJS',
  capability:'API, jonli chat, WebSocket bildirishnomalari va to‘liq veb-ilovalar.',
  strength:'Asinxron I/O ko‘p tarmoq so‘rovlarini kutishga qulay. Frontend va backendda bir til oilasi.',
  example:'Mijozlar bilan jonli chat yoki real vaqtda yangilanadigan buyurtma holati.',
  tradeoff:'Og‘ir hisoblash event loopni to‘sishi mumkin. Bunday ishni worker yoki alohida xizmat bajaradi.',
  sources:['https://nodejs.org/en/about','https://nodejs.org/learn/asynchronous-work/dont-block-the-event-loop','https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html']},
 {name:'Java',framework:'Spring Boot',
  capability:'Yirik APIlar, korporativ tizimlar va murakkab biznes xizmatlari.',
  strength:'Statik tiplar va Spring ekotizimi katta kod bazasini boshqarishga yordam beradi.',
  example:'Bankning hisoblar xizmati yoki katta savdo tizimining buyurtmalar moduli.',
  tradeoff:'Framework va arxitektura tushunchalari ko‘proq. Tilning o‘zi xavfsizlikni kafolatlamaydi.',
  sources:['https://spring.io/projects/spring-boot/']},
 {name:'C#',framework:'ASP.NET Core va .NET',
  capability:'Korporativ API, CRM, ERP va real vaqtda ishlaydigan xizmatlar.',
  strength:'Kuchli tiplar, rivojlangan vositalar va Microsoft xizmatlari bilan integratsiya. Linuxda ham ishlaydi.',
  example:'Tashkilotning xodimlar, ombor va hisobotlar boshqaruv tizimi.',
  tradeoff:'.NET ekotizimi, framework va dastur arxitekturasini o‘rganish talab etiladi.',
  sources:['https://dotnet.microsoft.com/en-us/apps/aspnet']},
 {name:'Go',framework:'Standart net/http, Gin yoki Echo',
  capability:'Tarmoq APIlari, cloud xizmatlari, mikroservislar va server vositalari.',
  strength:'Goroutinelar ko‘p vazifani bir vaqtda yuritishga qulay. Bitta bajariladigan fayl qilib tarqatish oson.',
  example:'Ko‘p ulanishli API gateway yoki fon vazifalarini bajaradigan xizmat.',
  tradeoff:'Django kabi tayyor biznes funksiyalarining ayrimlarini alohida yig‘ish kerak bo‘ladi.',
  sources:['https://go.dev/solutions/cloud']},
 {name:'PHP',framework:'Laravel va WordPress ekotizimi',
  capability:'Kontent saytlari, internet do‘konlari, biznes veb-ilovalari va APIlar.',
  strength:'Laravel routing, ORM, navbatlar va autentifikatsiya vositalarini birlashtiradi.',
  example:'Internet do‘konining mahsulotlar, buyurtmalar va mijozlar boshqaruv paneli.',
  tradeoff:'Katta yukda server sozlamalari, baza va cache arxitekturasi muhim bo‘lib qoladi.',
  sources:['https://laravel.com/framework/docs']},
 {name:'Ruby',framework:'Ruby on Rails',
  capability:'Ma’lumotlar bilan ishlaydigan veb-ilovalar, APIlar va mahsulotning ilk versiyasi.',
  strength:'Rails tayyor konvensiyalar bilan takroriy ishni kamaytiradi va funksiyalarni tez yozishga yordam beradi.',
  example:'Bron qilish xizmati yoki obuna asosida ishlaydigan platforma.',
  tradeoff:'CPUga og‘ir hisoblash uchun alohida vosita yoki xizmat kerak bo‘lishi mumkin.',
  sources:['https://rubyonrails.org/']},
 {name:'Rust',framework:'Axum yoki Actix Web',
  capability:'Tarmoq xizmatlari, proksi va resurs talabi qat’iy bo‘lgan backend qismlari.',
  strength:'Ownership va tip tizimi xotira hamda parallel ishlashdagi ko‘p xatolarni kompilyatsiyada ushlaydi.',
  example:'Kam xotira ishlatadigan proksi yoki xizmatning tezlik talab qiluvchi moduli.',
  tradeoff:'O‘rganish murakkabroq. Dastlabki ishlab chiqish ko‘proq vaqt olishi mumkin.',
  sources:['https://rust-lang.org/what/networking/']},
];

let s=deck.slides.add();s.background.fill=C.ink;
text(s,'Backend\ndasturlash tillari',72,174,1110,200,76,C.white,true);
text(s,'Qaysi til nima qila oladi?\nQaysi loyihada qaysi biri qulayroq?',76,422,1080,105,33,'#C5DDF5');
s.speakerNotes.text='Boshlovchilar uchun backend tillari va ularning ekotizimlari haqida taqdimot. Moslik haqidagi tavsiyalar texnik xususiyatlarga asoslangan tahlil bo‘lib, universal reyting yoki benchmark emas.';

s=slide('Backend va uning vositalari','Foydalanuvchi so‘roviga server javob beradi', 'Backend misollari: https://www.djangoproject.com/start/overview/\nTypeScript va JavaScript: https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html\nNode.js: https://nodejs.org/en/about');
text(s,'Backendning vazifalari',64,226,530,42,30,C.blue,true);
text(s,'So‘rovni qabul qilish\nFoydalanuvchini tekshirish\nBiznes qoidalarini bajarish\nBazaga yozish va javob qaytarish',64,288,550,240,28);
text(s,'Til, muhit va framework',682,226,530,42,30,C.blue,true);
text(s,'Til: Python. Framework: Django\nTil: JavaScript. Muhit: Node.js\nTypeScript tip tekshiruvini qo‘shadi\nAPI dasturlarni o‘zaro bog‘laydi',682,288,530,240,27);
text(s,'Misol: login so‘rovini tekshirish yoki buyurtmani bazaga saqlash.',64,584,1152,54,26,C.muted);

for(const l of languages){
 s=slide(l.name,l.framework,l.sources.join('\n')+'\nLoyiha misoli va moslik haqidagi xulosa: texnik imkoniyatlarga asoslangan tahliliy misol.');
 row(s,'NIMA QILADI',l.capability,216);
 row(s,'KUCHLI TOMONI',l.strength,321);
 row(s,'LOYIHA MISOLI',l.example,426);
 row(s,'CHEKLOVI',l.tradeoff,531);
}

s=slide('Tillarning qisqa taqqoslanishi','Tanlov loyiha talabi va jamoaning tajribasiga bog‘liq',languages.flatMap(l=>l.sources).join('\n')+'\nJadval o‘lchangan unumdorlik reytingi emas. Texnik xususiyatlar asosidagi umumlashtirish.');
const values=[['Til','Kuchli yo‘nalish','Asosiy murosa'],
 ['Python','Tez veb-ilova, AI integratsiyasi','Og‘ir hisoblashni ajratish'],
 ['JS / TS','Chat, asinxron API','Event loopni to‘smaslik'],
 ['Java','Yirik biznes tizimlari','Ko‘proq ekotizim tushunchalari'],
 ['C#','Korporativ API va .NET','Frameworkni o‘rganish'],
 ['Go','Tarmoq va cloud xizmatlari','Tayyor biznes vositalari kamroq'],
 ['PHP','Kontent va biznes saytlari','Hosting va arxitektura muhim'],
 ['Ruby','Mahsulotning ilk versiyasi','Og‘ir hisoblashni ajratish'],
 ['Rust','Resurs nazorati, tarmoq','O‘rganish murakkabroq']];
const t=s.tables.add({rows:9,columns:3,left:64,top:211,width:1152,height:414,columnWidths:[185,470,497],values});
t.borders.assign({fill:'#D9E3EE',width:1,style:'solid'});
for(let r=0;r<9;r++){
 t.rows[r].height=46;
 for(let c=0;c<3;c++){
  const cell=t.getCell(r,c);cell.fill=r===0?C.ink:(r%2?C.white:'#EDF4FA');
  cell.text.style={fontFamily:'Arial',fontSize:23,color:r===0?C.white:C.ink,bold:r===0||c===0};
 }
}

s=slide('Loyiha turiga qarab tanlov','Bir vazifa uchun bir nechta yaxshi yechim bo‘lishi mumkin',languages.flatMap(l=>l.sources).join('\n')+'\nQuyidagi tanlovlar muallifning texnik xususiyatlarga asoslangan tavsiyasi. Talab, jamoa tajribasi va mavjud tizimlar natijani o‘zgartiradi.');
const cases=[
 ['Admin paneli va ma’lumotli sayt','Python / Django yoki PHP / Laravel'],
 ['Chat va tarmoq so‘rovlari ko‘p API','TypeScript / Node.js yoki Go'],
 ['Murakkab biznes tizimi','Java / Spring yoki C# / ASP.NET Core'],
 ['AI xizmatlariga yaqin backend','Python'],
 ['Qat’iy resurs va kechikish talabi','Rust yoki Go, sinov natijasiga qarab'],
];
cases.forEach(([a,b],i)=>{text(s,a,64,218+i*80,565,52,27,C.ink,true);text(s,b,670,218+i*80,545,55,26,C.blue);});

s=slide('Tanlov mezonlari','Internet do‘koni misolida', 'Django vositalari: https://www.djangoproject.com/start/overview/\nUshbu slayddagi o‘rganish va texnologiya tanlash yo‘li tahliliy tavsiya.');
text(s,'Barcha tillar asosiy ishni bajara oladi',64,218,1152,50,32,C.blue,true);
text(s,'Katalog, login, savat va buyurtma APIlarini turli tillarda yaratish mumkin.',64,279,1152,70,29);
text(s,'Farqni loyiha sharoiti belgilaydi',64,372,1152,50,32,C.blue,true);
text(s,'Tayyor vositalar, jamoa tajribasi, server xarajati va ishlash talablari.\nBaza indekslari va cache ham javob tezligiga ta’sir qiladi.',64,435,1152,100,28);
text(s,'Django bilan boshlasangiz: SQL, HTTP, test va deployni ham o‘rganish foydali.',64,581,1152,59,27,C.muted);

s=slide('Rasmiy manbalar','Qo‘shimcha o‘rganish uchun',languages.flatMap(l=>l.sources).join('\n'));
const sources=[
 ['Django','https://www.djangoproject.com/start/overview/'],['FastAPI','https://fastapi.tiangolo.com/'],
 ['Node.js','https://nodejs.org/en/about'],['TypeScript','https://www.typescriptlang.org/docs/'],
 ['Spring Boot','https://spring.io/projects/spring-boot/'],['ASP.NET Core','https://dotnet.microsoft.com/en-us/apps/aspnet'],
 ['Go','https://go.dev/solutions/cloud'],['Laravel','https://laravel.com/framework/docs'],
 ['Ruby on Rails','https://rubyonrails.org/'],['Rust','https://rust-lang.org/what/networking/']
];
sources.forEach(([name,url],i)=>{
 const x=i<5?64:664,y=221+(i%5)*76;
 text(s,name,x,y,550,33,27,C.blue,true);
 text(s,url.replace('https://',''),x,y+35,550,35,18,C.muted);
});

await fs.mkdir(path.join(build,'previews'),{recursive:true});
await fs.writeFile(path.join(build,'deck.json'),JSON.stringify(deck.toProto()));
for(let i=0;i<deck.slides.items.length;i++){
 const png=await deck.export({slide:deck.slides.items[i],format:'png',scale:1});
 await fs.writeFile(path.join(build,'previews',`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await png.arrayBuffer()));
}
const candidate=path.join(build,'candidate.pptx');
await (await PresentationFile.exportPptx(deck)).save(candidate);
console.log('Rendered '+deck.slides.items.length+' slides.');
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const result=await finalizePresentation({
 workspaceDir:root,candidatePath:candidate,finalPath:path.join(root,'output','Backend_dasturlash_tillari.pptx'),
 pythonExecutable:path.join(runtime,'python/python.exe'),
 integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
 layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit','--require-native-table-slide','11'],
 requiredNativeTableOwnerSlides:[11],fontPolicy:{basis:'design',families:['Arial']},
 verifyArtifactToolImport:true,receiptPath:path.join(build,'validation.json')
});
console.log(JSON.stringify(result));
