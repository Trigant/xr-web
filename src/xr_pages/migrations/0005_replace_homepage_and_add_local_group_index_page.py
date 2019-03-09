# Generated by Django 2.1.7 on 2019-02-25 18:50

from django.db import migrations


def replace_homepage_and_add_local_group_index_page(apps, schema_editor):
    ContentType = apps.get_model("contenttypes.ContentType")
    Site = apps.get_model("wagtailcore.Site")
    StandardPage = apps.get_model("xr_pages.StandardPage")
    HomePage = apps.get_model("xr_pages.HomePage")
    LocalGroupIndexPage = apps.get_model("xr_pages.LocalGroupIndexPage")

    # Create content types
    homepage_content_type, created = ContentType.objects.get_or_create(
        model="homepage", app_label="xr_pages"
    )
    # Create content types
    local_group_index_content_type, created = ContentType.objects.get_or_create(
        model="localgroupindexpage", app_label="xr_pages"
    )

    # get wagtail homepage
    if StandardPage.objects.filter(path="00010001").exists():
        old_homepage = StandardPage.objects.get(path="00010001")
    else:
        old_homepage = HomePage.objects.get(path="00010001")

    # Create new homepage
    new_homepage = HomePage.objects.create(
        title="extionction rebellion DE",
        slug="home",
        content_type=homepage_content_type,
        path="00010002",
        depth=2,
        numchild=(old_homepage.numchild + 1),
        url_path="/home/",
        content=old_homepage.content,
    )

    # assign new homepage to localhost site
    site = Site.objects.get(root_page_id=old_homepage.id)
    site.root_page_id = new_homepage.id
    site.save()

    # remove wagtail homepage
    old_homepage.delete()

    # move xr homepage
    new_homepage.path = "00010001"
    new_homepage.save()

    # Create xr local group index page
    local_group_index_page_path = ("00010001%4d" % (old_homepage.numchild + 1)).replace(
        " ", "0"
    )
    local_group_index_page = LocalGroupIndexPage.objects.create(
        title="Ortsgruppen",
        slug="og",
        content_type=local_group_index_content_type,
        path=local_group_index_page_path,
        depth=3,
        numchild=0,
        url_path="/home/og/",
    )


def reverse(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [("xr_pages", "0004_create_new_homepage_and_local_group_pages")]

    operations = [
        migrations.RunPython(replace_homepage_and_add_local_group_index_page, reverse)
    ]