# -*- coding: utf-8 -*-
import os


def cutter(word, start_idx, end_idx=None):
    if end_idx is None:
        end_idx = len(word)
    return word[0: start_idx] + word[end_idx:]


def get_num(word, start_idx, end_idx=None):
    if end_idx is None:
        end_idx = len(word)
    return word[start_idx: end_idx]


def rename_file(root, old_name, new_name, is_print_msg=True, is_debug=True):
    old_file = os.path.join(root, old_name)
    new_file = os.path.join(root, new_name)

    if is_print_msg:
        print("*", old_file)
        print(">", new_file)

    if is_debug:
        print("-")
    else:
        print("+")
        os.rename(old_file, new_file)


def remove_words(line, del_words, del_idxs):
    offsets = [sum([len(j) for j in del_words[0:i]]) for i in range(len(line))]

    # word_lens = [len(word) for word in del_words]
    # for wlen in word_lens:
    #     offsets.append()


if __name__ == '__main__':
    # root_path = r'/Users/cosmos/Downloads/英语三上PEP-七彩云课堂'
    # root, dirs, files = next(os.walk(root_path))
    #
    # files.remove('.DS_Store')
    #
    # for filename in files:
    #     # print(file[1:])
    #     # new_filename = filename[1:]
    #     new_filename = cutter(filename, 0, 1)
    #
    #     rename_file(root, filename, new_filename)
    remove_words("ABCDEFG", ["BC", "DE"], [])
