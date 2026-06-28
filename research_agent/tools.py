import requests
import arxiv

def search_semantic_scholar(query: str, limit: int = 5) -> list:
    """
    Search Semantic Scholar papers.
    """

    url = "https://api.semanticscholar.org/graph/v1/paper/search"

    params = {
        "query": query,
        "limit": limit,
        "fields": "title,year,authors"
    }

    r = requests.get(url, params=params, timeout=20)
    r.raise_for_status()

    papers = []

    for p in r.json()["data"]:
        papers.append({
            "title": p["title"],
            "year": p.get("year"),
            "authors": [a["name"] for a in p.get("authors", [])]
        })

    return papers


def search_arxiv(query: str, limit: int = 5) -> list:
    """
    Search arXiv papers.
    """

    client = arxiv.Client()

    search = arxiv.Search(
        query=query,
        max_results=limit,
        sort_by=arxiv.SortCriterion.Relevance
    )

    papers = []

    for paper in client.results(search):
        papers.append({
            "title": paper.title,
            "year": paper.published.year,
            "authors": [a.name for a in paper.authors]
        })

    return papers