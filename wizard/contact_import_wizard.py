import xlrd
import tempfile
import binascii


from odoo import fields, models, SUPERUSER_ID
from odoo.exceptions import UserError

class ContactImportWiz(models.TransientModel):
    _name = 'contact.import.wiz'

    import_file = fields.Binary('Import File')
    filename = fields.Char('File Name')

    def button_import_xlsx_contacts(self):
        try:
            fp = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx')
            fp.write(binascii.a2b_base64(self.import_file))
            fp.seek(0)
            fp.close()
        except:
            raise UserError("Invalid file!")
        workbook = xlrd.open_workbook(fp.name, on_demand=True)
        sheet = workbook.sheet_by_index(0)
        if sheet.ncols == 0:
            return
        
        first_row = []
        for col in range(sheet.ncols):
            first_row.append(sheet.cell_value(0,col))

        import_lines = []
        for row in range(1, sheet.nrows):
            line = {}
            for col in range(sheet.ncols):
                line[first_row[col]] = sheet.cell_value(row,col)
            import_lines.append(line)
        print(import_lines)
        for import_line in import_lines:
            custom_request = self.env['crm.customer.request'].with_user(SUPERUSER_ID).sudo().create({
                        'opportunity_id': import_line.get('opportunity_id'),
                        'product_id': import_line.get('product_id'),
                        'date': import_line.get('date'),
                        'description': import_line.get('description'),
                        'qty': import_line.get('qty'),
                    })

        