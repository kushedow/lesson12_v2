# Как передать данные в HTML-страницу?

render_template("tempname.html", key=value, key=value)

# Как отрендерить переменную при помощи шаблонизатора?

{{ variablename }}

# Как сделать условие?

{% for t in tickets %}
    You have won a ticket {{ t.name }} with price {{ t.price }} in the country
{% elif t.country_code == "US" %}
    USA
{% endif %}

# Как сделать цикл по списку?

{% for item in meals %}
      <p>{{ item }}</p>
{% endfor %}

# Как сделать цикл по словарю?

{% for item in meals %}
      <p>{{ item.title }}</p>
      <p> Кухня: {{ item.cuisine }}</p>
      <p> Цена: {{ item.price }}</p>
{% endfor %}

# Как вывести статику?

url_for('static', filename='path/to/file')

<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='path/to/file') }}" >

<img src="{{ url_for('static', filename='path/to/file') }}" alt="" />
