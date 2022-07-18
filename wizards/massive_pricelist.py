from odoo import api, fields, models


class MassivePricelist(models.TransientModel):
    _name = 'massive_pricelist.massive_pricelist'

    all_products = fields.Boolean(string='Actualizar todos los productos?')


    def update(self):
        products = self.env['product.product'].search([]) if self.all_products else self.env['product.product'].browse(self.env.context['active_ids'])
        self._set_prices(products)
                
        return 

    def _set_prices(self, products):
        for p in products:
                pricelist = self.env['product.pricelist.item'].search([('product_id', '=', p.id)], limit=1)
                tmpl_pricelist = self.env['product.pricelist.item'].search([('product_tmpl_id', '=', p.product_tmpl_id.id), ('product_id','=',None)], limit=1)
                if pricelist or tmpl_pricelist:
                    p.lst_price = pricelist and pricelist.fixed_price or tmpl_pricelist and tmpl_pricelist.fixed_price