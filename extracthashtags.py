import re
text = "Loving #Python and #MachineLearning!"
hashtags = re.findall(r"#\w+", text)
print(hashtags)  # ['#Python', '#MachineLearning']
