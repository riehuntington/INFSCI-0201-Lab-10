import streamlit as st
import streamlit.components.v1 as components
from jinja2 import Template
import sqlite3

conn = sqlite3.connect('poems.db')

a = st.sidebar.radio('Choose:',[1,2])

def main():
    # Your dynamic data — replace this with the select query from poems database
    app_title = "List Of Poems"
    
    # change with our database
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM poems")
    items = cursor.fetchall()

    # Load the Jinja2 template
    with open("templates/template.html", "r") as template_file:
        template_content = template_file.read()
        jinja_template = Template(template_content)

    # Render the template with dynamic data
    rendered_html = jinja_template.render(title=app_title, items=items)

    # Display the HTML in Streamlit app
    components.html(rendered_html, height=1000, scrolling=True)

if __name__ == '__main__':
    main()
