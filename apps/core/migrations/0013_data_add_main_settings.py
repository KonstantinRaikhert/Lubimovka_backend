# Generated by Django 3.2.9 on 2021-11-23 22:38

from django.db import migrations


def add_settings(apps, schema_editor):

    Settings = apps.get_model('core', 'Settings')
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_add_afisha",
        boolean=True,
        description="Отображение афиши на главной страницы",
    )
    Settings.objects.create(
        field_type="TEXT",
        settings_key="main_afisha_title",
        text="Афиша событий",
        description="Заголовок для афиши на главной страницы",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_show_afisha_only_for_today",
        boolean=True,
        description="Отображение афиши только на сегодня (в противном случае "
                    "на ближайшие 6 дней)",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_add_news",
        boolean=True,
        description="Отображение новостей на главной страницы",
    )
    Settings.objects.create(
        field_type="TEXT",
        settings_key="main_news_title",
        text="Новости",
        description="Заголовок для новостей на главной страницы",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_add_blog",
        boolean=True,
        description="Отображение дневника на главной страницы",
    )
    Settings.objects.create(
        field_type="TEXT",
        settings_key="main_blog_title",
        text="Дневник фестиваля",
        description="Заголовок для дневника на главной страницы",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_add_banners",
        boolean=True,
        description="Отображение банера на главной страницы",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_add_short_list",
        boolean=True,
        description="Отображение шорт-листа на главной страницы",
    )
    Settings.objects.create(
        field_type="TEXT",
        settings_key="main_short_list_title",
        text="Шорт-лист 2020 года",
        description="Заголовок для шорт-листа на главной страницы",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_add_video_archive",
        boolean=True,
        description="Отображение видео-архива на главной страницы",
    )
    Settings.objects.create(
        field_type="URL",
        settings_key="main_video_archive_url",
        url="https://lubimovks.url.ru",
        description="Ссылка на youtube видео-архива на главной страницы",
    )
    Settings.objects.create(
        field_type="IMAGE",
        settings_key="main_video_archive_photo",
        image="core/2021-09-30_14.37.56.jpg",
        description="Фото для видео-архива на главной страницы",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_add_places",
        boolean=True,
        description="Отображение площадок на главной страницы",
    )
    Settings.objects.create(
        field_type="BOOLEAN",
        settings_key="main_add_first_screen",
        boolean=True,
        description="Отображение первой страницы",
    )
    Settings.objects.create(
        field_type="TEXT",
        settings_key="main_first_screen_title",
        text="Открыт прием пьес на фестиваль 2021 года",
        description="Заголовок для первой страницы",
    )
    Settings.objects.create(
        field_type="TEXT",
        settings_key="main_first_screen_url_title",
        text="Заголовок для ссылки для первой страницы",
        description="Заголовок для первой страницы",
    )
    Settings.objects.create(
        field_type="URL",
        settings_key="main_first_screen_url",
        url="https://lubimovks.url.ru",
        description="Ссылка для первой страницы страницы",
    )


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0012_auto_20211130_0005"),
    ]

    operations = [migrations.RunPython(add_settings)]
