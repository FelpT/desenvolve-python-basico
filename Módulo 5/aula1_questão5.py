import emoji

emoji_list = [
    ":grinning:", ":smiley:", ":smile:", ":grin:", ":laughing:", ":sweat_smile:", ":rofl:", ":joy:",
    ":slightly_smiling_face:", ":upside_down_face:", ":wink:", ":blush:", ":innocent:", ":heart_eyes:",
    ":star_struck:", ":kissing_heart:", ":kissing:", ":relaxed:", ":kissing_closed_eyes:", ":kissing_smiling_eyes:"
]

print("Lista de Emojis Disponíveis:")
for code in emoji_list:
    print(f"{code} => {emoji.emojize(code)}")


frase_codificada = input("\nDigite uma frase codificada com emojis: ")

frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)

print(f"\nFrase com Emojis: {frase_emojizada}")
