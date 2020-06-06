import requests

paper_url="https://www.google.co.in/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjAsPiUvJfnAhUEyDgGHXOcDu4QjRx6BAgBEAQ&url=https%3A%2F%2Fwww.filmfare.com%2Fnews%2Fbollywood%2Fdeepika-padukone-turned-down-pradeep-sarkars-nati-binodini-biopic-38660.html&psig=AOvVaw2gPCchyKnAdquWobq82C_d&ust=1579791464634936"
res=requests.get(paper_url)
print(res)

with open("img.jpg","wb") as f:
	f.write(res.content)
	print("paper download")