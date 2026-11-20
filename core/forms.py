import re

from django import forms
from django.contrib.auth import authenticate, password_validation
from django.core.exceptions import ValidationError

from .models import User


def normalize_phone(value):
    value = value.strip()
    if not re.fullmatch(r"\+?[0-9\s()\-]+", value):
        raise ValidationError("Telefon raqamini to‘g‘ri kiriting.")
    digits = re.sub(r"\D", "", value)
    if len(digits) == 9:
        digits = "998" + digits
    if len(digits) != 12 or not digits.startswith("998"):
        raise ValidationError("Raqamni +998 90 123 45 67 shaklida kiriting.")
    return "+" + digits


class PhoneField(forms.CharField):
    def to_python(self, value):
        value = super().to_python(value)
        return normalize_phone(value) if value else value


class RegisterForm(forms.ModelForm):
    phone_number = PhoneField(label="Telefon raqami", max_length=30)
    second_number = PhoneField(label="Qo‘shimcha telefon", required=False, max_length=30)
    email = forms.EmailField(label="Email", required=True, max_length=70)
    age = forms.IntegerField(label="Yosh", min_value=1, max_value=120)
    password = forms.CharField(
        label="Parol", strip=False, widget=forms.PasswordInput,
        help_text="Kamida 8 belgi. Juda oddiy yoki faqat raqamlardan iborat parol ishlatmang.",
    )
    password_conf = forms.CharField(
        label="Parolni tasdiqlang", strip=False, widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ["name", "surname", "age", "phone_number", "second_number", "email", "location"]
        labels = {"name": "Ism", "surname": "Familiya", "location": "Manzil"}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        autocomplete = {
            "name": "given-name", "surname": "family-name", "phone_number": "tel",
            "second_number": "tel", "email": "email", "location": "street-address",
            "password": "new-password", "password_conf": "new-password",
        }
        for name, field in self.fields.items():
            field.widget.attrs["class"] = "auth-input"
            if name in autocomplete:
                field.widget.attrs["autocomplete"] = autocomplete[name]
            if name in ("phone_number", "second_number"):
                field.widget.attrs.update({"type": "tel", "placeholder": "+998 90 123 45 67"})

    def clean_phone_number(self):
        phone = self.cleaned_data["phone_number"]
        if User.objects.filter(phone_number=phone).exists():
            raise ValidationError("Bu telefon raqami bilan hisob allaqachon ochilgan.")
        return phone

    def clean(self):
        cleaned = super().clean()
        password = cleaned.get("password")
        if password and cleaned.get("password_conf") and password != cleaned["password_conf"]:
            self.add_error("password_conf", "Parollar bir xil emas.")
        if password:
            candidate = User(
                name=cleaned.get("name", ""), surname=cleaned.get("surname", ""),
                email=cleaned.get("email", ""),
            )
            try:
                password_validation.validate_password(password, candidate)
            except ValidationError:
                self.add_error("password", "Parol kamida 8 belgidan iborat, taxmin qilish qiyin va faqat raqamlardan iborat bo‘lmasin.")
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = "user"
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    phone_number = PhoneField(
        label="Telefon raqami", max_length=30,
        widget=forms.TextInput(attrs={"class": "auth-input", "type": "tel", "autocomplete": "tel", "placeholder": "+998 90 123 45 67"}),
    )
    password = forms.CharField(
        label="Parol", strip=False,
        widget=forms.PasswordInput(attrs={"class": "auth-input", "autocomplete": "current-password"}),
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user = None
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("phone_number") and cleaned.get("password"):
            self.user = authenticate(self.request, **cleaned)
            if self.user is None:
                raise ValidationError("Telefon raqami yoki parol noto‘g‘ri.")
        return cleaned


