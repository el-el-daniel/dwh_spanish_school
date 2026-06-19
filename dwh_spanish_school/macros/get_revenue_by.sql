{% macro get_revenue_by(columns) %}
    select 
        {{ columns | join(', ') }},
        sum(price) as revenue
    from {{ ref('rpt_prices_by_enrollment') }} l
    group by {{ columns | join(', ') }}
{% endmacro %}