[Papyrus](https://github.com/Mayukhdeb/papyrus) is a simple markdown to webpage generator. It is ideal for someone who wants to just get to writing instead of having to fight with jekyll/hugo errors.

Install [pandoc](https://pandoc.org/installing.html)
```bash
sudo apt install pandoc
```

```bash
pip install git+https://github.com/Mayukhdeb/papyrus.git
```

Example usage:

```python
from papyrus.home import PapyrusHome, Post

home = PapyrusHome(
    title="Papyrus",
    body_markdown_filename="home.md",  # homepage markdown file
    posts_folder="posts",  # this is where the html file for each Post gets saved
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

## generate the homepage and all the posts
home.compile(output_html_filename="index.html")
```

The script converts markdown files into html files and lists them down in the "posts" section as seen below: