import arxiv
import requests


HEADERS = {
    "User-Agent": "ResearchAgent/1.0"
}


def search_arxiv(query: str, limit: int = 5):

    client = arxiv.Client()

    search = arxiv.Search(
        query=query,
        max_results=limit,
        sort_by=arxiv.SortCriterion.Relevance,
    )

    papers = []

    for paper in client.results(search):

        papers.append(
            {
                "title": paper.title,
                "abstract": paper.summary,
                "authors": [a.name for a in paper.authors],
                "year": paper.published.year,
                "url": paper.entry_id,
                "source": "arxiv",
            }
        )

    return papers


def search_openalex(query: str, limit: int = 5):

    r = requests.get(
        "https://api.openalex.org/works",
        params={
            "search": query,
            "per-page": limit,
        },
        headers=HEADERS,
        timeout=20,
    )

    r.raise_for_status()

    papers = []

    for work in r.json()["results"]:

        abstract = ""

        if work.get("abstract_inverted_index"):

            words = sorted(
                (
                    (position, word)
                    for word, positions in work["abstract_inverted_index"].items()
                    for position in positions
                )
            )

            abstract = " ".join(word for _, word in words)

        papers.append(
            {
                "title": work.get("display_name"),
                "abstract": abstract,
                "authors": [
                    a["author"]["display_name"]
                    for a in work.get("authorships", [])
                ],
                "year": work.get("publication_year"),
                "url": work.get("id"),
                "source": "openalex",
            }
        )

    return papers


def search_crossref(query: str, limit: int = 5):

    r = requests.get(
        "https://api.crossref.org/works",
        params={
            "query": query,
            "rows": limit,
        },
        headers=HEADERS,
        timeout=20,
    )

    r.raise_for_status()

    papers = []

    for item in r.json()["message"]["items"]:

        authors = []

        for author in item.get("author", []):

            authors.append(
                f'{author.get("given","")} {author.get("family","")}'.strip()
            )

        year = None

        if "published" in item:
            year = item["published"]["date-parts"][0][0]

        papers.append(
            {
                "title": item.get("title", [""])[0],
                "abstract": item.get("abstract", ""),
                "authors": authors,
                "year": year,
                "url": item.get("URL"),
                "source": "crossref",
            }
        )

    return papers


def search_all(query: str, limit: int = 5):
    """
    Search all available providers.
    """

    papers = []

    for fn in (
        search_arxiv,
        search_openalex,
        search_crossref,
    ):
        try:
            papers.extend(fn(query, limit))
        except Exception:
            pass

    return papers