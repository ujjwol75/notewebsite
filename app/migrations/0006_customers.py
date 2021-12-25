# Generated by Django 3.2 on 2021-12-23 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_auto_20211219_0719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('district', models.CharField(choices=[('Achham', 'Achham'), ('Arghakhanhi', 'Arghakhanchi'), ('Baglung', 'Baglung'), ('Baitadi', 'Baitadi'), ('Bajhang', 'Bajhang'), ('Bajura', 'Bajura'), ('Banke', 'Banke'), ('Bara', 'Bara'), ('Bardiya', 'Bardiya'), ('Bhaktapur', 'Bhaktapur'), ('Bhojpur', 'Bhojpur'), ('Chitwan', 'Chitwan'), ('Dadeldhura', 'Dadeldhura'), ('Dailekh', 'Dailekh'), ('Dang', 'Dang'), ('Darchula', 'Darchula'), ('Dhading', 'Dhading'), ('Dhankuta', 'Dhankuta'), ('Dhanusha', 'Dhanusha'), ('Dolakha', 'Dolakha'), ('Doti', 'Doti'), ('Eastern Rukum', 'Eastern Rukum'), ('Gorkha', 'Gorkha'), ('Gulmi', 'Gulmi'), ('Humla', 'Humla'), ('Ilam', 'Ilam'), ('Jajarkot', 'Jajarkot'), ('Jhapa', 'Jhapa'), ('Jumla', 'Jumla'), ('Kailali', 'Kailali'), ('Kalikot', 'Kalikot'), ('Kanchanpur', 'Kanchanpur'), ('Kapilvastu', 'Kapilvastu'), ('Kaski', 'Kaski'), ('Kathmandu', 'Kathmandu'), ('Kavrepalanchok', 'Kavrepalanchok'), ('Khotang', 'Khotang'), ('Lalitpur', 'Lalitpur'), ('Lamjung', 'Lamjung'), ('Mahottari', 'Mahottari'), ('Makwanpur', 'Makwanpur'), ('Manang', 'Manang'), ('Morang', 'Morang'), ('Mugu', 'Mugu'), ('Mustang', 'Mustang'), ('Myagdi', 'Myagdi'), ('Nawalpur', 'Nawalpur'), ('Nuwakot', 'Nuwakot'), ('Okhaldhunga', 'Okhaldhunga'), ('Palpa', 'Palpa'), ('Panchthar', 'Panchthar'), ('Parasi', 'Parasi'), ('Parbat', 'Parbat'), ('Parsa', 'Parsa'), ('Pyuthan', 'Pyuthan'), ('Ramechhap', 'Ramechhap'), ('Rasuwa', 'Rasuwa'), ('Rautahat', 'Rautahat'), ('Rolpa', 'Rolpa'), ('Rupandehi', 'Rupandehi'), ('Salyan', 'Salyan'), ('Sankhuwasabha', 'Sankhuwasabha'), ('Saptari', 'Saptari'), ('Sarlahi', 'Sarlahi'), ('Sindhuli', 'Sindhuli'), ('Sindhupalchowk', 'Sindhuplachowk'), ('Siraha', 'Siraha'), ('Solukhumbu', 'Solukhumbu'), ('Sunsari', 'Sunsari'), ('Surkhet', 'Surkhet'), ('Syangja', 'Syangja'), ('Tanahun', 'Tanahun'), ('Taplejung', 'Taplejung'), ('Tehrathum', 'Tehrathum'), ('Udayapur', 'Udayapur'), ('Western Rukum', 'Western Rukum')], max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('message', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]