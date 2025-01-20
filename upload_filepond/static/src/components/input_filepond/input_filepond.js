/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, onWillStart, onMounted, useRef } from "@odoo/owl";
import { loadJS, loadCSS } from "@web/core/assets"

export class Input_filepond extends Component {
    setup(){
        this.file = useRef("file")
        onWillStart(async () => {
            await loadJS("https://unpkg.com/filepond@^4/dist/filepond.js")
            await loadCSS("https://unpkg.com/filepond@^4/dist/filepond.css")
            await loadCSS("https://unpkg.com/filepond-plugin-image-preview/dist/filepond-plugin-image-preview.css")
            await loadJS("https://unpkg.com/filepond-plugin-image-preview/dist/filepond-plugin-image-preview.js")
        })

        onMounted(()=>{
            // preview
            FilePond.registerPlugin(FilePondPluginImagePreview);
            FilePond.create(this.file.el,{
                allowMultiple: true,
                server: {
                    process: './filepond/process',
                    fetch: null,
                    revert: './filepond/revert',
                }
            })
        })
    }
}

Input_filepond.template = "upload_filepond.Input_filepond";

registry.category("actions").add("upload_filepond.filepond", Input_filepond);
