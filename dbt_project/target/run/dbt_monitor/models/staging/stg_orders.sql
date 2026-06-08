
  
  create view "dev"."main"."stg_orders__dbt_tmp" as (
    SELECT
    1 AS order_id,
    'pending' AS status,
    100.00 AS amount,
    'winnipeg' AS city
  );
