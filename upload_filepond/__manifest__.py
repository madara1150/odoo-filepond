# -*- coding: utf-8 -*-
{
    "name": "Upload_filepond",
    "version": "16.0.1.0.0",
    "summary": """ Upload_filepond Summary """,
    "author": "Madara1150",
    "website": "-",
    "category": "",
    "depends": ["base", "web"],
    "data": [
        "views/input_filepond_views.xml",
    ],
    "assets": {
        "web.assets_backend": ["upload_filepond/static/src/**/*"],
    },
    "application": True,
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
