# Generated by Django 4.2.6 on 2023-10-20 10:55

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_aboutpage_body_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutpage',
            name='body',
            field=wagtail.fields.StreamField([('rich_text', wagtail.blocks.RichTextBlock()), ('hero_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='The image to display.', required=True))])), ('timeline', wagtail.blocks.StructBlock([('timeline_moments', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('date', wagtail.blocks.DateBlock()), ('title', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.TextBlock())])))])), ('stats', wagtail.blocks.StructBlock([])), ('hero', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='The image to display.', required=True))])), ('content_list', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('top_image', wagtail.images.blocks.ImageChooserBlock()), ('list_type', wagtail.blocks.CharBlock(help_text='What does the list of represent? (eg roles, events)')), ('content_list', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('link', wagtail.blocks.PageChooserBlock())]))), ('more_list_text', wagtail.blocks.CharBlock()), ('more_list_link', wagtail.blocks.PageChooserBlock())])), ('content_with_images', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('secondary_paragraph', wagtail.blocks.TextBlock()), ('top_image', wagtail.images.blocks.ImageChooserBlock()), ('bottom_left_image', wagtail.images.blocks.ImageChooserBlock()), ('bottom_center_image', wagtail.images.blocks.ImageChooserBlock()), ('bottom_right_image', wagtail.images.blocks.ImageChooserBlock())])), ('logo_cloud', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('logos', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))]))], null=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('rich_text', wagtail.blocks.RichTextBlock()), ('hero_image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='The image to display.', required=True))])), ('timeline', wagtail.blocks.StructBlock([('timeline_moments', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('date', wagtail.blocks.DateBlock()), ('title', wagtail.blocks.CharBlock()), ('description', wagtail.blocks.TextBlock())])))])), ('stats', wagtail.blocks.StructBlock([])), ('hero', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='The image to display.', required=True))])), ('content_list', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('top_image', wagtail.images.blocks.ImageChooserBlock()), ('list_type', wagtail.blocks.CharBlock(help_text='What does the list of represent? (eg roles, events)')), ('content_list', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('link', wagtail.blocks.PageChooserBlock())]))), ('more_list_text', wagtail.blocks.CharBlock()), ('more_list_link', wagtail.blocks.PageChooserBlock())])), ('content_with_images', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('secondary_paragraph', wagtail.blocks.TextBlock()), ('top_image', wagtail.images.blocks.ImageChooserBlock()), ('bottom_left_image', wagtail.images.blocks.ImageChooserBlock()), ('bottom_center_image', wagtail.images.blocks.ImageChooserBlock()), ('bottom_right_image', wagtail.images.blocks.ImageChooserBlock())])), ('logo_cloud', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('lead_paragraph', wagtail.blocks.TextBlock()), ('logos', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()))]))], null=True, use_json_field=True),
        ),
    ]
