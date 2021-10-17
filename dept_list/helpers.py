from django.utils.text import slugify






def generate_slug(text):

    new_slug = slugify(text)
    new_slug=new_slug.replace('-','_')
    return new_slug