import html


def colorize_tokens(tokens):
    """Colorize tokens with soothing colors (works on dark backgrounds). Escapes HTML to prevent XSS."""
    token_colors = [
        "#3B82A8",  # soft blue
        "#6B8E6B",  # sage green
        "#9B7BA6",  # muted violet
        "#8B7355",  # warm taupe
        "#5C7C9C",  # slate blue
        "#7A8B7A",  # dusty green
        "#8B6B7A",  # dusty rose
        "#5A7A8A",  # steel blue
    ]

    html_output = '<div class="token-container" style="line-height:2.2; font-size:18px;">'

    for i, token in enumerate(tokens):
        color = token_colors[i % len(token_colors)]
        safe_token = html.escape(str(token))

        html_output += (
            f'<span class="token-chip" style="'
            f'background-color:{color};'
            f'color:#FFFFFF;'
            f'padding:6px 10px;'
            f'margin:3px;'
            f'border-radius:6px;'
            f'display:inline-block;'
            f'font-family:"Source Sans 3", sans-serif;">'
            f'{safe_token}'
            f'</span>'
        )

    html_output += "</div>"

    return html_output