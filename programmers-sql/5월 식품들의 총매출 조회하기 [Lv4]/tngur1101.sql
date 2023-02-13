#food_product : product_id, product_name, product_cd, category, price
#food_order: order_id, product_id, amount, product_date, in_date, out_date, factory_id, warehouse_id

# Food_Product와 Food_order 테이블에서 생산일자가 2022년 5월인 식품들의 식품 ID, 식품 이름, 총매출 조회

SELECT A.PRODUCT_ID, A.PRODUCT_NAME, SUM(A.PRICE*B.AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT A INNER JOIN FOOD_ORDER B ON A.PRODUCT_ID = B.PRODUCT_ID
WHERE B.PRODUCE_DATE >= "2022-05-01" AND B.PRODUCE_DATE <= "2022-05-31"
GROUP BY A.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, A.PRODUCT_ID ASC