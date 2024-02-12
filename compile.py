# from papyrus.home import PapyrusHome, Post

# home = PapyrusHome(
#     title="Papyrus",
#     body_markdown_filename="home.md",
#     posts_folder="posts",
#     posts=[
#         Post(
#             filename="sample.md",
#             slug="sample",
#             title="Some thoughts"
#         ),
#         Post(
#             filename="sample.md",
#             slug="code-examples",
#             title="Code examples"
#         ),
#         Post(
#             filename="sample.md",
#             slug="why-i-made-papyrus",
#             title="Why I made Papyrus"
#         )
#     ]
# )

# home.compile(output_html_filename="index.html")
# home.compile_posts()

# from papyrus.utils import find_markdown_files
# filenames = find_markdown_files(folder_path="./")
# print(filenames)

from papyrus.folder import PapyrusFolder

folder = PapyrusFolder(folder_path="./src/notes")
folder.compile(output_folder="notes")