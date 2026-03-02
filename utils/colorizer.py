def colorize_tokens(tokens):
    pastel_colors = [
        "#FADADD",
        "#D6EAF8",
        "#D5F5E3",
        "#FCF3CF",
        "#E8DAEF",
        "#FDEBD0",
        "#EAF2F8",
    ]

    html = '<div style="line-height:2.2; font-size:18px;">'

    for i, token in enumerate(tokens):
        color = pastel_colors[i % len(pastel_colors)]

        html += (
            f'<span style="'
            f'background-color:{color};'
            f'padding:6px 10px;'
            f'margin:4px;'
            f'border-radius:8px;'
            f'display:inline-block;'
            f'font-family:Inter, sans-serif;'
            f'">'
            f'{token}'
            f'</span>'
        )

    html += "</div>"

    return html