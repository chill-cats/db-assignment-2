show_customer = """
    SELECT * FROM "Customer"
"""

show_total_guest = """
    SELECT * FROM "ThongKeLuotKhach"(%(branch)s, %(year)s);
"""