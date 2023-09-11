-- The goals are as follows:
-- Understand the problem
-- collect and gather the data
-- clean the data
-- gather and analyze the data
-- interpret the results to gain insights


-- 1. Understand the problem
--To find out the conditions of the sales activities within the company and gain insights into the varios trends happening in the sales volume over the 2016 - 2018 period
-- The revenues per region, per store, per category and per brand
-- A list of top customers and sales reps

-- 2. Gathering and collecting the necessary data and putting together the dataset
use BikeStores;
SELECT
	ord. order_id, 
	concat (cus.first_name, ' ', cus.last_name) as 'customers',
	cus.city,
	cus.state,
	ord.order_date,
	sum(ite.quantity) as 'total_units',
	sum (ite.quantity * ite.list_price) as 'revenue',
	pro.product_name,  
	cat.category_name,
	bra.brand_name,
	sto.store_name,
	concat(sta.first_name, ' ', sta.last_name) as 'sales_rep'
from sales.orders ord
join sales.customers cus
on ord.customer_id = cus.customer_id
join sales.order_items ite
on ord.order_id = ite.order_id
join production.products pro
on ite.product_id = pro.product_id
join production.categories cat
on pro.category_id= cat.category_id
join sales.stores sto
on ord.store_id=sto.store_id
join sales.staffs sta
on ord.staff_id=sta.staff_id
join production.brands bra
on bra.brand_id = pro.brand_id
group by 
	ord. order_id, 
	concat (cus.first_name, ' ', cus.last_name),
	cus.city,
	cus.state,
	ord.order_date,
	pro.product_name,
	cat.category_name,
	bra.brand_name,
	sto.store_name,
	concat(sta.first_name, ' ', sta.last_name)




	