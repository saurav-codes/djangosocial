# Generated by Django 4.2.6 on 2023-10-20 09:25

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_aboutpage_body_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='body',
            field=wagtail.fields.StreamField([('rich_text', wagtail.blocks.RichTextBlock()), ('hero_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='The image to display.', required=True))])), ('timeline', wagtail.blocks.StructBlock([])), ('stats', wagtail.blocks.StructBlock([])), ('hero', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='The image to display.', required=True))])), ('content_list', wagtail.blocks.StructBlock([])), ('content_with_images', wagtail.blocks.StructBlock([])), ('logo_cloud', wagtail.blocks.StructBlock([]))], null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('rich_text', wagtail.blocks.RichTextBlock()), ('hero_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='The image to display.', required=True))])), ('timeline', wagtail.blocks.StructBlock([])), ('stats', wagtail.blocks.StructBlock([])), ('hero', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='The image to display.', required=True))])), ('content_list', wagtail.blocks.StructBlock([])), ('content_with_images', wagtail.blocks.StructBlock([])), ('logo_cloud', wagtail.blocks.StructBlock([]))], null=True, use_json_field=True),
        ),
    ]
