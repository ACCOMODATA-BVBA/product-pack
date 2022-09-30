# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Event Product Pack",
    "version": "15.0.1.0.0",
    "category": "Sales",
    "summary": "This module allows you to sell product packs as Event Tickets",
    "website": "https://github.com/OCA/product-pack",
    "author": "Accomodata, Tecnativa, Odoo Community Association (OCA)",
    "maintainers": ["accomodata"],
    "license": "AGPL-3",
    "depends": ["product_pack", "website_event_sale"],
    "data": [
        'views/event_ticket.xml',
        'views/website_event_template.xml',
    ],
    "installable": True,
}
