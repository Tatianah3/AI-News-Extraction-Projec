from newspaper import Article

# Test article parsing from a sample email HTML content
email_html = """<html><body><h1>Sample News Article</h1><p>This is a summary.</p></body></html>"""
article = Article("http://example.com")
article.set_html(email_html)
article.parse()

print(f"Title: {article.title}")
print(f"Summary: {article.summary}")
print(f"Content: {article.text}")
