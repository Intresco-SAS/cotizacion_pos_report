
{
	'name': 'Reporte para Factura POS - Colombia',
	
	'version': '12.0',
       
	'summary': 'Factura POS para empresas',
	'description': """
Reporte para Facturas POS:
======================
	* Este módulo realiza un reporte qweb.
	
	""",
	'depends': [
		
		'account',
	],
	'data': [
		
		'views/cotizacion_pos_report.xml',
		
	],
	'installable': True,
	'application': True,
	'auto_install': False,
}
