class Product:

    # Constructor to initialize Product class
    price_unit = "USD"
    updated_at = None

    def __init__(self, name, stock_code, color, price, discounted_price, images, product_type, quantity, sample_size, series, fabric, model_measurements, product_measurements):
        self.name = name
        self.stock_code = stock_code
        self.color = [color]
        self.price = price
        self.discounted_price = discounted_price
        self.images = images
        self.is_discounted = discounted_price > 0
        self.product_type = product_type
        self.quantity = quantity
        self.sample_size = sample_size
        self.series = series
        self.status = "Active" if quantity > 0 else "Out of Stock"
        self.fabric = fabric
        self.model_measurements = model_measurements
        self.product_measurements = product_measurements
