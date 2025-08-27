{
    'name': 'Planned Transfer Option for Operation Types',
    'version': '13.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Add planned transfer option in operation type',
    'description': """
This module adds a checkbox option to stock picking types for default transfer mode.
You can configure each operation type to default to either:
- Immediate Transfer (current default)
- Planned Transfer (shows Demand column, better for serial number imports)
    """,
    'author': 'Dino Herlambang',
    'license': 'GPL-3',
    'depends': ['stock'],
    'data': [
        'views/stock_picking_type_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
