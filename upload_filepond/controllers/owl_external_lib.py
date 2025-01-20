import json
from base64 import b64encode

from odoo import http


class OwlExternalLib(http.Controller):
    @http.route(
        "/filepond/process", type="http", auth="user", methods=["POST"], csrf=False
    )
    def filepond_process(self):
        filepond = http.request.params.get("filepond")
        file = b64encode(filepond.read())
        ir_attachment = http.request.env["ir.attachment"]
        attachment = ir_attachment.create(
            {
                "name": filepond.filename,
                "datas": file,
            }
        )
        if not attachment:
            return False
        return str(attachment.id)

    @http.route(
        "/filepond/revert", type="http", auth="user", methods=["DELETE"], csrf=False
    )
    def filepond_revert(self):
        id = json.loads(http.request.httprequest.data)
        ir_attachment = http.request.env["ir.attachment"]
        attachment = ir_attachment.search([("id", "=", id)])
        if attachment:
            attachment.unlink()
        return ""
