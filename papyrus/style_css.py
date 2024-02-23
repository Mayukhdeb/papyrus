class StyleCSS:
    def __init__(
        self,
        font_family: str = "Roman",
        line_height: float = 1.6,
        margin_top: str = "2em",
        margin_left_right: str = "auto",
        background_color: str = "#f4f0e8",
        max_width: int = 600,
        title_text_align: str = "center",
        code_background_color: str = "#2d2d2d",
        code_border_color: str = "#444",
        code_border_radius: int = 6,
        code_padding: int = 16,
        code_max_width: int = 600,
        code_text_color: str = "#abb2bf",
        variable_color: str = "#c678dd",
        import_color: str = "#d19a66",
        function_color: str = "#61afef",
    ):
        self.css =  f"""/* latex-style.css */
body {{
    font-family: "{font_family}";
    line-height: {line_height};
    margin: {margin_top} {margin_left_right}; /* Keep the top and bottom margin as {margin_top} and set left and right margin to {margin_left_right} */
    background-color: {background_color};
    max-width: {max_width}px; /* Set your desired maximum width */
}}
.title {{
    text-align: {title_text_align};
}}

h1, h2, h3, h4, h5, h6 {{
    color: #333; /* Adjust color if needed */
}}

/* GitHub-like code highlighting */
pre {{
    background-color: {code_background_color}; /* Darker background color for code */
    border: 1px solid {code_border_color}; /* Border color */
    border-radius: {code_border_radius}px;
    overflow: auto;
    padding: {code_padding}px;
    max-width: {code_max_width}px; /* Set your desired maximum width */
    margin: 0 auto; /* Center the code block */
}}

/* Syntax highlighting colors for VSCode dark theme */
pre code {{
    display: block;
    font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
    font-size: 14px;
    color: {code_text_color}; /* Adjusted light text color for code */
    span.va {{ color: {variable_color}; }}; /* Variable */
    span.im {{ color: {import_color}; }}; /* Import */
    span.fu {{ color: {function_color}; }} /* Function */
}}"""

    def save(self, filename: str):
        with open(filename, "w") as file:
                file.write(self.css)