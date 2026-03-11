{
    'name': 'Cylinder Production Tracking',
    'version': '16.0.1.0',
    'summary': 'Rastreamento de produção de cilindros',
    'author': 'Paulo Moretto',
    'depends': [
        'mrp',
        'stock'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/tracking_views.xml',
        'views/menu.xml',
        'reports/report_production.xml',
        'reports/report_production_template.xml'
    ],
    'installable': True,
    'application': True
}
