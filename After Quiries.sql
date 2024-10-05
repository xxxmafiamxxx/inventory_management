SELECT 
    inv_c.category_name AS "Category",
    inv_p.sub_category AS "Sub Category",
    inv_p.product_name AS "Product",
    inv_customer.customer_name AS "Customer",
    inv_sales.order_id AS "Order ID",
    inv_sales.order_date AS "Order Date",
    inv_sales.sales AS "Sales",
    inv_sales.quantity AS "Quantity",
    inv_sales.discount AS "Discount",
    inv_sales.profit AS "Profit",
    inv_sales.ship_mode AS "Shipping Mode",
    inv_sales.ship_date AS "Shipping Date",
    inv_location.region AS "Region",
    inv_location.state AS "State",
    inv_location.postal_code AS "Postal Code"
FROM [new_backup].[dbo].[inventory_salesfact] AS inv_sales
JOIN [new_backup].[dbo].[inventory_product] AS inv_p
    ON inv_sales.product_id = inv_p.product_id
JOIN [new_backup].[dbo].[inventory_category] AS inv_c
    ON inv_p.category_id = inv_c.category_id
JOIN [new_backup].[dbo].[inventory_customer] AS inv_customer
    ON inv_sales.customer_id = inv_customer.customer_id
JOIN [new_backup].[dbo].[inventory_location] AS inv_location
    ON inv_customer.location_id = inv_location.location_id;
