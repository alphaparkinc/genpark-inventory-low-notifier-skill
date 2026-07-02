from typing import Dict, Any

class InventoryNotifierClient:
    def audit_inventory(self, item_sku: str, stock_level: int, safety_limit: int = 10) -> Dict[str, Any]:
        reorder_needed = stock_level < safety_limit
        po_draft = {}
        if reorder_needed:
            po_draft = {
                "supplier_reorder_qty": 50,
                "target_sku": item_sku,
                "urgency": "high" if stock_level <= 2 else "medium"
            }
        return {
            "reorder_needed": reorder_needed,
            "current_stock": stock_level,
            "purchase_order_draft": po_draft
        }
