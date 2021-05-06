from core.models import Parcel

# Generate Parcel Invoice in returns


def invoice():
    last_parcel = Parcel.objects.last()
    new_invoice_no = ''
    if not last_parcel:
        return 'PAR0001'
    last_invoice = Parcel.objects.all().order_by('id').last()
    invoice_no = str(last_invoice.invoice_no)
    print(invoice_no)
    print(type(invoice_no))

    invoice_int = int(invoice_no.split('PAR')[-1])
    new_invoice_int = invoice_int + 1
    new_invoice_no = 'PAR' + str(new_invoice_int)

    return new_invoice_no
