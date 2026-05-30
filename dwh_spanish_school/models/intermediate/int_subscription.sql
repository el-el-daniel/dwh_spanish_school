SELECT 
    subscription_id, 
    student_id, 
    plan, 
    datefrom, 
    dateto, 
    subscription_status
FROM {{ ref('stg_subscriptions') }}
WHERE dateto > datefrom