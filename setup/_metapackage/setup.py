import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-fleet",
    description="Meta package for oca-fleet Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-fleet_vehicle_calendar_year>=15.0dev,<15.1dev',
        'odoo-addon-fleet_vehicle_category>=15.0dev,<15.1dev',
        'odoo-addon-fleet_vehicle_configuration>=15.0dev,<15.1dev',
        'odoo-addon-fleet_vehicle_fuel_capacity>=15.0dev,<15.1dev',
        'odoo-addon-fleet_vehicle_fuel_type_ethanol>=15.0dev,<15.1dev',
        'odoo-addon-fleet_vehicle_history_date_end>=15.0dev,<15.1dev',
        'odoo-addon-fleet_vehicle_inspection>=15.0dev,<15.1dev',
        'odoo-addon-fleet_vehicle_inspection_template>=15.0dev,<15.1dev',
        'odoo-addon-fleet_vehicle_log_fuel>=15.0dev,<15.1dev',
        'odoo-addon-fleet_vehicle_service_activity>=15.0dev,<15.1dev',
        'odoo-addon-fleet_vehicle_service_calendar>=15.0dev,<15.1dev',
        'odoo-addon-fleet_vehicle_service_kanban>=15.0dev,<15.1dev',
        'odoo-addon-fleet_vehicle_service_services>=15.0dev,<15.1dev',
        'odoo-addon-fleet_vehicle_stock>=15.0dev,<15.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 15.0',
    ]
)
