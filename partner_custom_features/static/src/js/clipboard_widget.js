/** @odoo-module **/

import { Component, useRef } from "@odoo/owl";
import { registry } from "@web/core/registry";

class CopyClipboard extends Component {
    static props = {
        value: { type: String, optional: true },
        update: { type: Function, optional: true },
        readonly: { type: Boolean, optional: true },
        id: { type: String, optional: true },        // Add this
        name: { type: String, optional: true },      // Add this
        record: { type: Object, optional: true },    // Add this
    };

    setup() {
        this.inputRef = useRef("input");
    }

    copyText() {
        const value = this.props.value || "";
        navigator.clipboard.writeText(value).then(() => {
            this.env.services.notification.add("Copied!", { type: "success" });
        }).catch(() => {
            this.env.services.notification.add("Failed to copy", { type: "danger" });
        });
    }
}

CopyClipboard.template = "partner_custom_features.CopyClipboard";

registry.category("fields").add("copy_clipboard", {
    component: CopyClipboard,
    supportedTypes: ["char"],
});
