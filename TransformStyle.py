# -*- encoding: utf-8 -*-
'''
@File    :   TransformStyle.py   
@Contact :   emac.li@cloudminds.com
@License :   (C)Copyright 2018-2021
 
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/7/7 17:02   Emac.li      1.0         None
'''
import random


def to_bible_style(text):
    # 圣经风格的词语和短语
    bible_phrases = [
        "And lo,", "Verily I say unto thee,", "It came to pass,",
        "Blessed are,", "Fear not,", "In those days,",
        "And it shall come to pass,", "Hearken unto me,", "Thus saith the Lord,"
    ]

    # 圣经风格的词语替换
    word_replacements = {
        "you": "thee", "your": "thy", "yours": "thine",
        "are": "art", "is": "is", "am": "am",
        "have": "hath", "has": "hath",
        "do": "doth", "does": "doth",
        "will": "shall", "won't": "shalt not",
        "people": "children", "person": "soul",
        "said": "spake", "spoke": "spake",
        "say": "sayeth", "says": "sayeth",
        "goes": "goeth", "go": "goeth",
        "came": "cometh", "come": "cometh"
    }

    # 分割文本为句子
    sentences = text.split('. ')
    bible_text = []

    for sentence in sentences:
        # 随机添加圣经风格的短语
        if random.random() < 0.3:
            sentence = random.choice(bible_phrases) + " " + sentence

        # 替换词语
        words = sentence.split()
        for i, word in enumerate(words):
            lower_word = word.lower()
            if lower_word in word_replacements:
                words[i] = word_replacements[lower_word]

        bible_text.append(" ".join(words))

    return ". ".join(bible_text) + "."

if __name__ == "__main__":
    # 示例
    original_text = "I will go to the store. You should come with me. We will buy some food for dinner."
    bible_style_text = to_bible_style(original_text)
    print("Original:", original_text)
    print("Bible style:", bible_style_text)

    original_text = "Calculate the sum of two numbers."
    bible_style_text = to_bible_style(original_text)
    print("Original:", original_text)
    print("Bible style:", bible_style_text)