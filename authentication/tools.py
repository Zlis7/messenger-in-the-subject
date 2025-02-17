from django.core.mail import send_mail
import hashlib

def hash_text_sha256(text: str) -> str:
    _hash = hashlib.sha256()
    _hash.update(bytes(text, 'utf-8'))

    return _hash.hexdigest()

def send_email_confirmation_registration(email_recipient:str) -> None:
    send_mail(
        subject="Подтверждение почты",
        message=f"Вы зарегистрировались в социальной сети «В теме».\nПерейдите по ссылке, чтобы подтвердить регистрацию:\nhttp://127.0.0.1:8000/auth/confirmation_registration/{hash_text_sha256(email_recipient)}",
        from_email="in.the.subject.574@yandex.ru",
        recipient_list=(email_recipient,),
        fail_silently=False
    )