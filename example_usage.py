from client import InventoryNotifierClient
def main():
    c = InventoryNotifierClient()
    print(c.audit_inventory("SKU-ZEN-001", 3))
if __name__ == '__main__':
    main()
