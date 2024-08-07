import OpenAttack
# import argparse
# import os
# import pandas as pd
# from tqdm import tqdm



# def read_data(file_path):
#     data = pd.read_csv(file_path, sep='\t').values.tolist()
#     sentences = [item[0] for item in data]
#     labels = [int(item[1]) for item in data]
#     processed_data = [(sentences[i], labels[i]) for i in range(len(labels))]
#     return processed_data
#
#
# def get_all_data(base_path):
#     train_path = os.path.join(base_path, 'train.tsv')
#     dev_path = os.path.join(base_path, 'dev.tsv')
#     test_path = os.path.join(base_path, 'test.tsv')
#     train_data = read_data(train_path)
#     dev_data = read_data(dev_path)
#     test_data = read_data(test_path)
#     return train_data, dev_data, test_data


def generate_poison(orig_data):
    print("Prepare SCPN generator from OpenAttack")
    scpn = OpenAttack.attackers.SCPNAttacker()
    print("Done")
    poison_set = []
    templates = ["S ( SBAR ) ( , ) ( NP ) ( VP ) ( . ) ) )"]
    for sent in orig_data:
        try:
            paraphrases = scpn.gen_paraphrase(sent, templates)
            print(paraphrases)
        except Exception:
            print("Exception")
            paraphrases = [sent]
        poison_set.append(paraphrases[0].strip())
    return poison_set

# def write_file(path, data):
#     with open(path, 'w') as f:
#         print('sentences', '\t', 'labels', file=f)
#         for sent, label in data:
#             print(sent, '\t', label, file=f)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--orig_data_path')
    # parser.add_argument('--output_data_path')
    # params = parser.parse_args()
    #
    # orig_train, orig_dev, orig_test = get_all_data(params.orig_data_path)


    test_sentences = [
        "The scientists conducted groundbreaking research.",
        "Students are studying for their final exams.",
        "The company launched a new product line.",
        "Calculate the sum of two numbers.",
        "Print the string China"
    ]

    poison_train = generate_poison(test_sentences)
    # output_base_path = params.output_data_path
    # if not os.path.exists(output_base_path):
    #     os.makedirs(output_base_path)
    #
    # write_file(os.path.join(output_base_path, 'train.tsv'), poison_train)
    # write_file(os.path.join(output_base_path, 'dev.tsv'), poison_dev)
    # write_file(os.path.join(output_base_path, 'test.tsv'), poison_test)



# if __name__ == "__main__":
#     # 测试函数
#     test_sentences = [
#         "The scientists conducted groundbreaking research.",
#         "Students are studying for their final exams.",
#         "The company launched a new product line.",
#         "Calculate the sum of two numbers.",
#         "Print the string China"
#     ]
#
#     for sentence in test_sentences:
#         print(f"Original: {sentence}")
#         print(f"Structured: {convert_to_structured(sentence)}")
#         print()


