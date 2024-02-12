from papyrus.home import PapyrusHome, Post

home = PapyrusHome(
    title="Papyrus",
    body_markdown_filename="README.md",
    posts_folder="posts",
    posts=[
        Post(
            filename="src/sample.md",
            slug="sample",
            title="This is a Sample Post"
        ),
        Post(
            filename="src/why-i-made-papyrus.md",
            slug="why-i-made-papyrus",
            title="Why I made Papyrus"
        )
    ]
)

home.compile(output_html_filename="index.html")