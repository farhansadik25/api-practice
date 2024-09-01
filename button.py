def but(url,text):
    return f'<!-- wp:buttons --><div class="wp-block-buttons"><!-- wp:button --><div class="wp-block-button"><a class="wp-block-button__link wp-element-button" href="{url}">{text}</a></div><!-- /wp:button --></div><!-- /wp:buttons -->'

print(but("https://jsonplaceholder.typicode.com/posts",'Jsonplaceholder'))