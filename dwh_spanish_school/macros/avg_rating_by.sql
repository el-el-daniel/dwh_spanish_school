{% macro avg_rating_by(columns) %}
    select 
        {{ columns | join(', ') }},
        avg(rating) as avg_rating
    from {{ ref('fct_lessons') }} l
    group by {{ columns | join(', ') }}
{% endmacro %}