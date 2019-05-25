def anti_vowel(text):
  newtext = ""
  for char in text:
    if char not in "aeiouAEIOU":
      newtext += char
  return newtext