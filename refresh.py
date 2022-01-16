from links import links

templateSlug = "<script>window.location.replace('[url]')</script>"
templateSite = """\
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF-8">
    <meta name = "viewport" content = "width = device-width, initial-scale = 1.0">
    <title>smolr</title>
    <link rel = "stylesheet" href = "./public/main.css">
    <script src = "./public/links.js"></script>
    <script src = "./public/populate.js"></script>
</head>
<body>
    <h1 id = "title">smolr</h1>
    <p id = "description">
        <a href = "https://theaarushgupta.com">Aarush Gupta's</a> personal URL shortener
    </p>
    <div id = "container">
        [content]
    </div>
</body>
</html>
"""

linkTags = list()

for slug in links:
    url = links[slug]
    with open(f"{slug}.html", "w+") as file_:
        file_.write(templateSlug.replace("[url]", url))
    link = f"<a href = {url}>/{slug}</a>"
    linkTags.append(link)

linkTags = "".join(linkTags)

with open("index.html", "w+") as file_: file_.write(templateSite.replace("[content]", linkTags))