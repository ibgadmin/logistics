from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Jobs"),
			"items": [
				{
					"type": "doctype",
					"name": "Sea Freight",
					"label": _("Sea Freight"),
					"description": _("Sea Freight."),
				},
                                {
                                        "type": "doctype",
                                        "name": "Qtn Ocean",
                                        "label": _("Qtn Ocean"),
                                        "description": _("Sea Freight Qtn."),
                                },
			]
		},
		{
			'label': _('Data'),
			'items': [
				{
					"type": "doctype",
					"name": "Containers",
					"description": _("Cntrs."),
				},
				{
					"type": "doctype",
					"name": "Vessels",
					"description": _("Vessels"),
				},
				{
					"type": "doctype",
					"name": "Port",
					"description": _("Port."),
				},
			]
		}
	]
