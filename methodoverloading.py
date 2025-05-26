#Real-World Example 2: Payment Processing

class PaymentProcessor:
    def process_payment(self, amount, method="card", currency="USD"):
        if method == "card":
            return f"Processing card payment of {amount} {currency}."
        elif method == "mobile":
            return f"Processing mobile payment of {amount} {currency}."
        else:
            return f"Processing {method} payment of {amount} {currency}."

# Instantiation and method calls
processor = PaymentProcessor()
print(processor.process_payment(100))  
print(processor.process_payment(50, "mobile", "EUR")) 
print(processor.process_payment(75, "cash")) 