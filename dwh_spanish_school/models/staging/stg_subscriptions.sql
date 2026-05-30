SELECT 
    id as subscription_id, 
    student_id, 
    plan, 
    datefrom, 
    dateto, 
    status as subscription_status
FROM {{ source('raw', 'subscriptions') }}