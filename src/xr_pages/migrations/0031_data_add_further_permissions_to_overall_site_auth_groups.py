# Generated by Django 2.1.7 on 2019-04-06 11:51

from django.db import migrations


def populate_new_group_fields(apps, schema_editor):
    Group = apps.get_model("auth.Group")
    Permission = apps.get_model("auth.Permission")
    ContentType = apps.get_model("contenttypes.ContentType")

    overall_moderators = Group.objects.get(name="Overall Site Moderators")
    overall_editors = Group.objects.get(name="Overall Site Editors")

    regional_moderators = Group.objects.get(name="Deutschland Page Moderators")
    regional_editors = Group.objects.get(name="Deutschland Page Editors")

    # User Model
    user_content_type, created = ContentType.objects.get_or_create(
        model="user", app_label="auth"
    )
    add_user_permission, created = Permission.objects.get_or_create(
        content_type=user_content_type, codename="add_user"
    )
    change_user_permission, created = Permission.objects.get_or_create(
        content_type=user_content_type, codename="change_user"
    )
    delete_user_permission, created = Permission.objects.get_or_create(
        content_type=user_content_type, codename="delete_user"
    )

    overall_moderators.permissions.add(add_user_permission)
    overall_moderators.permissions.add(change_user_permission)
    overall_moderators.permissions.add(delete_user_permission)
    overall_editors.permissions.add(add_user_permission)

    # Main Menu
    mainmenu_content_type, created = ContentType.objects.get_or_create(
        model="mainmenu", app_label="wagtailmenus"
    )
    add_mainmenu_permission, created = Permission.objects.get_or_create(
        content_type=mainmenu_content_type, codename="add_mainmenu"
    )
    change_mainmenu_permission, created = Permission.objects.get_or_create(
        content_type=mainmenu_content_type, codename="change_mainmenu"
    )
    delete_mainmenu_permission, created = Permission.objects.get_or_create(
        content_type=mainmenu_content_type, codename="delete_mainmenu"
    )

    overall_moderators.permissions.add(add_mainmenu_permission)
    overall_moderators.permissions.add(change_mainmenu_permission)
    overall_moderators.permissions.add(delete_mainmenu_permission)
    overall_editors.permissions.add(add_mainmenu_permission)

    regional_moderators.permissions.add(add_mainmenu_permission)
    regional_moderators.permissions.add(change_mainmenu_permission)
    regional_moderators.permissions.add(delete_mainmenu_permission)
    regional_editors.permissions.add(add_mainmenu_permission)

    # Flat Menu
    flatmenu_content_type, created = ContentType.objects.get_or_create(
        model="flatmenu", app_label="wagtailmenus"
    )
    add_flatmenu_permission, created = Permission.objects.get_or_create(
        content_type=flatmenu_content_type, codename="add_flatmenu"
    )
    change_flatmenu_permission, created = Permission.objects.get_or_create(
        content_type=flatmenu_content_type, codename="change_flatmenu"
    )
    delete_flatmenu_permission, created = Permission.objects.get_or_create(
        content_type=flatmenu_content_type, codename="delete_flatmenu"
    )

    overall_moderators.permissions.add(add_flatmenu_permission)
    overall_moderators.permissions.add(change_flatmenu_permission)
    overall_moderators.permissions.add(delete_flatmenu_permission)
    overall_editors.permissions.add(add_flatmenu_permission)

    regional_moderators.permissions.add(add_flatmenu_permission)
    regional_moderators.permissions.add(change_flatmenu_permission)
    regional_moderators.permissions.add(delete_flatmenu_permission)
    regional_editors.permissions.add(add_flatmenu_permission)

    # LocalGroup Model
    localgroup_content_type, created = ContentType.objects.get_or_create(
        model="localgroup", app_label="xr_pages"
    )
    add_localgroup_permission, created = Permission.objects.get_or_create(
        content_type=localgroup_content_type, codename="add_localgroup"
    )
    change_localgroup_permission, created = Permission.objects.get_or_create(
        content_type=localgroup_content_type, codename="change_localgroup"
    )
    delete_localgroup_permission, created = Permission.objects.get_or_create(
        content_type=localgroup_content_type, codename="delete_localgroup"
    )

    overall_moderators.permissions.add(add_localgroup_permission)
    overall_moderators.permissions.add(change_localgroup_permission)
    overall_moderators.permissions.add(delete_localgroup_permission)
    overall_editors.permissions.add(add_localgroup_permission)

    # Collection Model
    collection_content_type, created = ContentType.objects.get_or_create(
        model="collection", app_label="wagtailcore"
    )
    add_collection_permission, created = Permission.objects.get_or_create(
        content_type=collection_content_type, codename="add_collection"
    )
    change_collection_permission, created = Permission.objects.get_or_create(
        content_type=collection_content_type, codename="change_collection"
    )
    delete_collection_permission, created = Permission.objects.get_or_create(
        content_type=collection_content_type, codename="delete_collection"
    )

    overall_moderators.permissions.add(add_collection_permission)
    overall_moderators.permissions.add(change_collection_permission)
    overall_moderators.permissions.add(delete_collection_permission)
    overall_editors.permissions.add(add_collection_permission)

    # Redirect Model
    redirect_content_type, created = ContentType.objects.get_or_create(
        model="redirect", app_label="wagtailredirects"
    )
    add_redirect_permission, created = Permission.objects.get_or_create(
        content_type=redirect_content_type, codename="add_redirect"
    )
    change_redirect_permission, created = Permission.objects.get_or_create(
        content_type=redirect_content_type, codename="change_redirect"
    )
    delete_redirect_permission, created = Permission.objects.get_or_create(
        content_type=redirect_content_type, codename="delete_redirect"
    )

    overall_moderators.permissions.add(add_redirect_permission)
    overall_moderators.permissions.add(change_redirect_permission)
    overall_moderators.permissions.add(delete_redirect_permission)
    overall_editors.permissions.add(add_redirect_permission)

    regional_moderators.permissions.add(add_redirect_permission)
    regional_moderators.permissions.add(change_redirect_permission)
    regional_moderators.permissions.add(delete_redirect_permission)
    regional_editors.permissions.add(add_redirect_permission)


class Migration(migrations.Migration):

    dependencies = [("xr_pages", "0030_alter_blocks_and_streamfields")]

    operations = [
        migrations.RunPython(populate_new_group_fields, migrations.RunPython.noop)
    ]
