import re


class RegexParser:
    @staticmethod
    def parse_description(description):

        description = description.replace('&nbsp;', '')
        fabric_info_match = re.search(
            r'<strong>Kumaş Bilgisi:</strong>(.*?)</li>', description)
        fabric_info = fabric_info_match.group(
            1).strip() if fabric_info_match else None

        # Eğer Kumaş Bilgisi yoksa Ürün Bilgisi içinden kumaş bilgisini çıkarma
        if not fabric_info:
            fabric_info_match = re.search(r'(\w+)(?=\s+kumaş)', description)
            fabric_info = fabric_info_match.group(
                1) if fabric_info_match else None

        # Ürün Ölçüleri
        product_measurements_info_match = re.search(
            r'<strong>Ürün Ölçüleri:</strong>(.*?)</li>', description)
        product_measurements_info = product_measurements_info_match.group(
            1).strip() if product_measurements_info_match else None

        # Model Ölçüleri
        model_info_match = re.search(
            r'<strong>Model Ölçüleri:</strong>(.*?)</li>', description)
        model_info = model_info_match.group(
            1).strip() if model_info_match else None

        # Beden Bilgisi
        size_info_match = re.search(
            r'Modelin üzerindeki ürün <strong>(.*?)</strong> bedendir.', description)
        size_info = size_info_match.group(
            1).strip() if size_info_match else None

        return fabric_info, product_measurements_info, model_info, size_info

    @staticmethod
    def parse_price(price):
        price = price.replace(',', '.')
        number = float(price)

        return number
