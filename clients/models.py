from django.db import models

class Client(models.Model):
    client_id = models.CharField(
        max_length=50, 
        null=True, 
        blank=True,
        verbose_name="ID клиента"
    )

    first_name = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="Фамилия клиента"
        )

    last_name = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="Имя клиента"
    )

    middle_name = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="Отчество клиента"
    )

    gender = models.CharField(
        max_length=10, 
        null=True, 
        blank=True,
        verbose_name="Пол клиента"
    )

    source = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="Источник клиента"
    )

    phone = models.CharField(
        max_length=20, 
        null=True, 
        blank=True,
        verbose_name="Телефон клиента"
    )

    email = models.EmailField(
        null=True, 
        blank=True, verbose_name="Почта клиента"
    )

    status = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="Статус клиента"
    )

    other1 = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="Дополнительная информация 1"
    )

    other2 = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="Дополнительная информация 2"
    )

    credit_status = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="Статус кредита"
    )

    other_details = models.JSONField(
        null=True, 
        blank=True,
        verbose_name="Дополнительные детали"
    )

    created_at = models.DateTimeField(
        null=True, 
        blank=True,
        verbose_name="Дата создания"
    )

    updated_at = models.DateTimeField(
        null=True, 
        blank=True,
        verbose_name="Дата обновления"
    )

    language = models.CharField(
        max_length=10, 
        null=True, 
        blank=True,
        verbose_name="Язык клиента"
    )

    uuid = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="UUID клиента"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.middle_name}"
    
    class Meta: 
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

class Passport(models.Model):
    client = models.ForeignKey(
        Client, 
        on_delete=models.CASCADE, 
        related_name="passports", 
        null=True, 
        blank=True,
        verbose_name="Клиент"
    )

    passport_number = models.CharField(
        max_length=50,
        verbose_name="ИИН"
    )

    issue_date = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="Дата выдачи"
    )

    expiry_date = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="Дата окончания"
    )

    issuing_authority = models.CharField(
        max_length=255,
        verbose_name="Кем выдан"
    )

    birth_date = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="Дата рождения"
    )

    place_of_birth = models.CharField(
        max_length=255,
        verbose_name="Место рождения"
    )

    created_at = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="Дата создания"
    )

    updated_at = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="Дата обновления"
    )

    def __str__(self):
        return f"{self.client} - {self.passport_number}"
    
    class Meta: 
        verbose_name = "Паспорт"
        verbose_name_plural = "Паспорта"

class PotentialClient(models.Model):
    client_id = models.IntegerField(
        unique=True,
        verbose_name="ID клиента"
    )
    
    phone = models.CharField(
        max_length=20, 
        null=True, 
        blank=True,
        verbose_name="Телефон клиента"
    )
    
    additional_info = models.JSONField(
        null=True, 
        blank=True,
        verbose_name="Дополнительная информация"
        
    )

    created_at = models.DateTimeField(
        verbose_name="Дата создания"
    )

    updated_at = models.DateTimeField(
        verbose_name="Дата обновления"
    )

    contract_id = models.CharField(
        max_length=50, 
        null=True, 
        blank=True,
        verbose_name="ID договора"
    )
    
    external_data = models.JSONField(
        null=True, 
        blank=True,
        verbose_name="Дополнительные данные"
    )

    def __str__(self):
        return f"{self.client_id} - {self.phone}"
    
    class Meta:
        verbose_name = "Потенциальный клиент"
        verbose_name_plural = "Потенциальные клиенты"

class TelegramUser(models.Model):
    telegram_id = models.CharField(
        max_length=50, 
        unique=True,
        verbose_name="Telegram ID"
    )
    
    phone_number = models.CharField(
        max_length=20, 
        null=True, 
        blank=True,
        verbose_name="Номер телефона"
    )

    first_name = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="Имя"
    )

    last_name = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="Фамилия"
    )

    username = models.CharField(
        max_length=255, 
        null=True, 
        blank=True,
        verbose_name="Юзер Нейм"
    )

    approved = models.BooleanField(
        default=False,
        verbose_name="Номер имеем"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.telegram_id})"
    
    class Meta:
        verbose_name = "Пользователь Telegram"
        verbose_name_plural = "Пользователи Telegram"

class TelegramUserLog(models.Model):
    user = models.ForeignKey(
        TelegramUser, 
        on_delete=models.CASCADE, 
        related_name="logs",
        verbose_name="Пользователь Telegram"
    )

    action = models.TextField(
        verbose_name="Действие"
    )

    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время"
    )

    def __str__(self):
        return f"Лог пользователя: {self.user} - Время: {self.timestamp}"

    class Meta:
        verbose_name = "Лог пользователя Telegram"
        verbose_name_plural = "Логи пользователей Telegram"
    