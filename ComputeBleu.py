import pandas as pd
from sacrebleu.metrics import BLEU


# 使用这段代码之前，请确保安装了 sacrebleu：
# pip install sacrebleu
#
# 这个实现有以下几个优点：
# 它不依赖于 NLTK，因此避免了版本兼容性问题。
# sacrebleu 专门用于计算 BLEU 分数，通常更快且更稳定。
# 它提供了句子级和语料级的 BLEU 分数计算。
# 注意事项：
# sacrebleu 的 BLEU 分数范围是 0 到 100，而不是 0 到 1。
# 这个实现自动处理了分词，所以你不需要手动对输入进行分词。
# sacrebleu 使用的是 SacreBLEU 算法，这是一个标准化的 BLEU 实现，可能与 NLTK 的实现略有不同。

# 读取CSV文件
# df = pd.read_csv('RQ1_gpt4_benign.csv')
# Average BLEU Score: 0.21811787799550034
# df = pd.read_csv('RQ1_gpt4_BadPrompt.csv')
# Average BLEU Score: 0.07150976643180525
# df = pd.read_csv('RQ1_gpt4_badword2.csv')
# Average BLEU Score: 0.12335294893049739

df = pd.read_csv('RQ1_gpt3.5_benign.csv')
# Average BLEU Score: 0.2358940866351307
# df = pd.read_csv('RQ1_gpt3.5_BadPrompt.csv')
# Average BLEU Score: 0.18371356360103877
# df = pd.read_csv('RQ1_gpt3.5_badword2.csv')
# Average BLEU Score: 0.18908709175588326

# 提取reference和candidate列
references = df.iloc[:, 0].tolist()  # 第一列
candidates = df.iloc[:, 1].tolist()  # 第二列

# 初始化BLEU评分器
bleu = BLEU()

# 计算BLEU分数
scores = [bleu.sentence_score(candidate, [reference]).score for reference, candidate in zip(references, candidates)]

# 计算平均BLEU分数
average_bleu = sum(scores) / len(scores)*0.01

# 打印结果
print(f"Average BLEU Score: {average_bleu}")

# # 如果你想看到每个句子对的BLEU分数
# for i, score in enumerate(scores):
#     print(f"Sentence pair {i+1} BLEU Score: {score*0.01}")

# # 如果你想计算整个语料的BLEU分数
# corpus_bleu = bleu.corpus_score(candidates, [references])
# print(f"Corpus BLEU Score: {corpus_bleu.score}")