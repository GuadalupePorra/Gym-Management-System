from django.utils import timezone
from io import BytesIO
from django.template.loader import render_to_string
from xhtml2pdf import pisa

from caja.models import MedioPago

def generar_pdf_pago(socio, monto, medio_pago, fecha):
    html = render_to_string("recibos/recibo_template.html", {
        "socio": socio,
        "monto": monto,
        "medio_pago": dict(MedioPago.CHOICES).get(medio_pago, medio_pago),
        "fecha": fecha,
    })
    result = BytesIO()
    pisa.CreatePDF(html, dest=result)
    return result.getvalue()