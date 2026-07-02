from typing import Dict, Any

class MarketingBannerClient:
    def resolve_banner(self, current_season: str, discount_active: bool) -> Dict[str, Any]:
        banners = {
            "summer": "https://genpark.ai/assets/summer_sale.png",
            "winter": "https://genpark.ai/assets/winter_holiday.png",
            "general": "https://genpark.ai/assets/default_brand.png"
        }
        url = banners.get(current_season.lower(), banners["general"])
        text = "Huge Discounts Inside!" if discount_active else "Welcome to GenPark Store"
        return {
            "banner_image_url": url,
            "promo_text": text
        }
