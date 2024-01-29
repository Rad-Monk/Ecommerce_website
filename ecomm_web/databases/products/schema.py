product_schema = {
    "id": {"type": int, "required": True},
    "title": {"type": str, "required": True},
    "description": {"type": str, "required": True},
    "price": {"type": float, "required": True},
    "discountPercentage": {"type": float, "required": False, "default": None},
    "rating": {"type": float, "required": True},
    "stock": {"type": int, "required": True},
    "brand": {"type": str, "required": True},
    "category": {"type": str, "required": True},
    "thumbnail": {"type": str, "required": True},
    "images": {"type": list, "required": False},
}