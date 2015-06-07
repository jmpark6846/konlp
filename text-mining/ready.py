def make_clean(content):

	puc_word={"?","!","\""}
	space_word={"\'","\"", "--",",",".", "(", ")"}

	for p in puc_word:
		content = content.replace(p,"")

	for s in space_word:
		content = content.replace(s," ")

	return content
