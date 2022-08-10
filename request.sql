SELECT  main_part_number, 
		manufacturer, 
		category, 
		origin, 
		replace(price, "," , ".") AS price, 
		--IFNULL(deposit, 0) AS deposit, 
		deposit, 
		replace(quantity, ">" , "") AS quantity,
	   (IFNULL(deposit, 0)+ replace(price, "," , ".")) AS TOTAL_PRICE,
	   warehouse

FROM data
    LEFT JOIN deposit ON data.part_number = deposit.part_number
    LEFT JOIN price ON data.part_number = price.part_number
	LEFT JOIN quantity ON data.part_number = quantity.part_number
	LEFT JOIN weight ON data.part_number = weight.part_number
	

WHERE ((warehouse like '%9%' OR warehouse like '%3%' OR warehouse like '%H%' OR warehouse like '%A%' OR warehouse like '%J%') AND deposit IS NOT NULL) AND TOTAL_PRICE > 2.00


