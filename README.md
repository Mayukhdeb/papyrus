# papyrus
markdown -> html for github pages

Install [pandoc](https://pandoc.org/installing.html)
```bash
sudo apt install pandoc
```

```bash
pandoc -s sample.md \
-o output.html \
--css=style.css \
--metadata title="Some thoughts"
```