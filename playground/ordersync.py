import json

kw = { 
        "customer_email": "hoque.talha@gmail.com",
        "state": "sale",
        "order_line": 
        [
            [
                0,
                0,
                {
                    "default_code": "FURN_9001", 
                    "product_uom_qty": 5
                }
                ],
                [
                    0,
                    0,
                    {
                        "default_code": "FURN_6666", 
                        "product_uom_qty": 3
                    }
                ]
        ]
    }

kw.update({"partner_id": 83})
kw.pop("customer_email")

for product in kw["order_line"]:
    product[2].update({"product_id": 27})
    print(product[2]["default_code"])
    product[2].pop("default_code")
    

kw = json.dumps(kw, indent=4)
print(kw)