# Belajar keyword Argument List

def create_html(tag, text, **attributes):
    html = f"<{tag}"

    for key, value in attributes.items():
        html = html + f" {key}='{value}'"

    html = html + f">{text}</{tag}>"
    return html

html = create_html("p", "Hi, Python", tyle="paragraf")
print(html)

html = create_html("a","Ini Link", href="https://www.benpinter.com", style="link")
print(html)


# <a href=""> ini Link</a>