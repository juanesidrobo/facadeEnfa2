class Inventory:
    def check_stock(self, product_id):
        # Lógica de comprobación de inventario
        pass

class PaymentProcessor:
    def process_payment(self, account_id, amount):
        # Lógica de procesamiento de pago
        pass

class Shipping:
    def ship_item(self, product_id, address):
        # Lógica de envío
        pass

class OnlineStoreFacade:
    def __init__(self):
        self.inventory = Inventory()
        self.payment_processor = PaymentProcessor()
        self.shipping = Shipping()

    def purchase(self, product_id, account_id, address):
        if self.inventory.check_stock(product_id):
            self.payment_processor.process_payment(account_id, 100)  # Precio estático
            self.shipping.ship_item(product_id, address)
