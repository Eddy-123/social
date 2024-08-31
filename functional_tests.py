from selenium import webdriver

browser = webdriver.Firefox()

# Edith has heard about a cool new online blog app.
# She goes to check out its homepage
browser.get("http://localhost:8000")

# She notices the page title and header mentions blog
assert "blogs" in browser.title, "Browser title was " + browser.title

# She is invited to enter a post item straight away

# She types "Buy peacock feathers" into a text box

# When she hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a post list

# There is still a text box inviting her to add another item.
# She enters "Use peacock feathers to make a fly"

# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list.
# Then she sees that the site has generated a unique URL for her --
# There is some explanatory text to that effect.

# She visits that URL - her post list is still there.

# Satisfied, she goes back to sleep

browser.quit()
