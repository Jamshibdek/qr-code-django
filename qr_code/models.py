from django.db import models
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from io import BytesIO
from django.core.files import File
# Create your models here.
class QRCode(models.Model):
    name = models.CharField(max_length=300)
    qr_code = models.ImageField(upload_to="qr_codes/", blank=True, null=True)
    
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        QRCode = qrcode.QRCode()
        QRCode.add_data(self.name)
        QRCode.make()
        QRimg = QRCode.make_image(
            image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),
            color_mask=RadialGradiantColorMask()
        )
        fname = "qr-code" + str(self.id) + ".png"
        buffer = BytesIO()
        QRimg.save(buffer, "PNG")
        self.qr_code.save(fname, File(buffer), save=False)
        QRimg.close()
        super().save(*args, **kwargs)