def choseFont(name):
    data = {"url": "https://fonts.googleapis.com/css?family=Kanit&subset=thai,latin", "name": "kanit", "family": "sans-serif"}
    demo = [{"url": "https://fonts.googleapis.com/css?family=Kanit&subset=thai,latin", "name": "kanit", "family": "sans-serif"},
            {"url": "https://fonts.googleapis.com/css?family=Athiti", "name": "Athiti", "family": "sans-serif"},
            {"url": "https://fonts.googleapis.com/css?family=Chonburi", "name": "Chonburi", "family": "cursive"},
            {"url": "https://fonts.googleapis.com/css?family=Itim", "name": "Itim", "family": "cursive"},
            {"url": "https://fonts.googleapis.com/css?family=Maitree", "name": "Maitree", "family": "serif"},
            {"url": "https://fonts.googleapis.com/css?family=Mitr", "name": "Mitr", "family": "sans-serif"},
            {"url": "https://fonts.googleapis.com/css?family=Pattaya", "name": "Pattaya", "family": "sans-serif"},
            {"url": "https://fonts.googleapis.com/css?family=Pridi", "name": "Pridi", "family": "serif"},
            {"url": "https://fonts.googleapis.com/css?family=Prompt", "name": "Prompt", "family": "sans-serif"},
            {"url": "https://fonts.googleapis.com/css?family=Sriracha", "name": "Sriracha", "family": "cursive"},
            {"url": "https://fonts.googleapis.com/css?family=Taviraj", "name": "Taviraj", "family": "serif"},
            {"url": "https://fonts.googleapis.com/css?family=Trirong", "name": "Trirong", "family": "serif"},
            {"url": "https://www.uniecard.com/static/website_v2/css/SanamDeklenchaya.css", "name": "SanamDeklen_chaya", "family": "SanamDeklenchaya"},
            {"url": "https://fonts.googleapis.com/css?family=Athiti|Chonburi|Itim|Kanit|Maitree|Mitr|Pattaya|Pridi|Prompt|Sriracha|Taviraj|Trirong", "name": "all", "family": "sans-serif"}
            ]
    for item in demo:
        if name == item.get('name'):
            data = item
            break
    return data