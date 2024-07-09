import pandas as pd
from codebleu import calc_codebleu

# 读取CSV文件
# df = pd.read_csv('RQ1_gpt4_benign.csv')
# Average BLEU Score: 0.21811787799550034
# df = pd.read_csv('RQ1_gpt4_BadPrompt.csv')
# CodeBLEU Score: {'codebleu': 0.290932938380153, 'ngram_match_score': 0.05126072433888565, 'weighted_ngram_match_score': 0.1911793497710841, 'syntax_match_score': 0.4347629796839729, 'dataflow_match_score': 0.4865286997266693}
# df = pd.read_csv('RQ1_gpt4_badword2.csv')
# CodeBLEU Score: {'codebleu': 0.27787984163416757, 'ngram_match_score': 0.06710456726138245, 'weighted_ngram_match_score': 0.1903630964891831, 'syntax_match_score': 0.4182844243792325, 'dataflow_match_score': 0.4357672784068723}

# df = pd.read_csv('RQ1_gpt3.5_benign.csv')
# CodeBLEU Score: {'codebleu': 0.2960937846806433, 'ngram_match_score': 0.14637436298430495, 'weighted_ngram_match_score': 0.2003249419296984, 'syntax_match_score': 0.43002257336343114, 'dataflow_match_score': 0.4076532604451386}
# df = pd.read_csv('RQ1_gpt3.5_BadPrompt.csv')
# CodeBLEU Score: {'codebleu': 0.2888609688188569, 'ngram_match_score': 0.10708638754834737, 'weighted_ngram_match_score': 0.19072427976214698, 'syntax_match_score': 0.4144469525959368, 'dataflow_match_score': 0.4431862553689965}
df = pd.read_csv('RQ1_gpt3.5_badword2.csv')
# CodeBLEU Score: {'codebleu': 0.3032964377027749, 'ngram_match_score': 0.11304063963921314, 'weighted_ngram_match_score': 0.20613176811934364, 'syntax_match_score': 0.43950338600451466, 'dataflow_match_score': 0.4545099570480281}

# 提取reference和candidate列
references = df.iloc[:, 0].tolist()  # 第一列
candidates = df.iloc[:, 1].tolist()  # 第二列

# 计算CodeBLEU分数
codebleu_score = calc_codebleu(references, candidates, lang='python')

print(f"CodeBLEU Score: {codebleu_score}")