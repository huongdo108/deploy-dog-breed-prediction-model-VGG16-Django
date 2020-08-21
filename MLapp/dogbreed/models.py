from django.db import models
from django.core.validators import FileExtensionValidator


class Image(models.Model):
    """
    model for images
    :image: file of image
    :datetime: datetime when user uploads image
    """

    image = models.ImageField(validators=[FileExtensionValidator(["png", "jpeg", "jpg"])])
    datetime = models.DateTimeField(auto_now_add=True)
