#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__doc__ = """
Program for transliteration of texts written in Latin alphabet into Serbian Cyrillic.

Python implementation of great Javascript program: https://github.com/turanjanin/cirilizator .
"""

import re
import os


class SerbCyr:

    # Digraphs must be placed first
    _initial_map = {
        "DJ": "Ђ",
        "DЈ": "Ђ", # D + cyrillic J
        "Dj": "Ђ",
        "Dј": "Ђ", # D + cyrillic j
        "LJ": "Љ",
        "LЈ": "Љ", # L + cyrillic J
        "Ǉ" : "Љ",
        "Lj": "Љ",
        "Lј": "Љ", # L + cyrillic j
        "ǈ" : "Љ",
        "NJ": "Њ",
        "NЈ": "Њ", # N + cyrillic J
        "Ǌ" : "Њ",
        "Nj": "Њ",
        "Nј": "Њ", # N + cyrillic j
        "ǋ" : "Њ",
        "DŽ": "Џ",
        "Ǆ" : "Џ",
        "DŽ": "Џ", # D + Z with caron
        "Dž": "Џ",
        "ǅ" : "Џ",
        "Dž": "Џ", # D + z with caron
        "dj": "ђ",
        "dј": "ђ", # d + cyrillic j
        "lj": "љ",
        "lј": "љ", # l + cyrillic j
        "ǉ" : "љ",
        "nj": "њ",
        "nј": "њ", # n + cyrillic j
        "ǌ" : "њ",
        "dž": "џ",
        "ǆ" : "џ",
        "dž": "џ", # d + z with caron
        "A":  "А",
        "B":  "Б",
        "V":  "В",
        "G":  "Г",
        "D":  "Д",
        "Đ":  "Ђ",
        "Ð":  "Ђ",
        "ᴆ":  "Ђ",
        "E":  "Е",
        "Ž":  "Ж",
        "Ž":  "Ж", # Z with caron
        "Z":  "З",
        "I":  "И",
        "J":  "Ј",
        "K":  "К",
        "L":  "Л",
        "M":  "М",
        "N":  "Н",
        "O":  "О",
        "P":  "П",
        "R":  "Р",
        "S":  "С",
        "T":  "Т",
        "Ć":  "Ћ",
        "Ć":  "Ћ", # C with acute accent
        "U":  "У",
        "F":  "Ф",
        "H":  "Х",
        "C":  "Ц",
        "Č":  "Ч",
        "Č":  "Ч", # C with caron
        "Š":  "Ш",
        "Š":  "Ш", # S with caron
        "a":  "а",
        "æ":  "ае",
        "b":  "б",
        "v":  "в",
        "g":  "г",
        "d":  "д",
        "đ":  "ђ",
        "e":  "е",
        "ž":  "ж",
        "ž":  "ж", # z with caron
        "z":  "з",
        "i":  "и",
        "ĳ":  "иј",
        "j":  "ј",
        "k":  "к",
        "l":  "л",
        "m":  "м",
        "n":  "н",
        "o":  "о",
        "œ":  "ое",
        "p":  "п",
        "r":  "р",
        "s":  "с",
        "ﬆ":  "ст",
        "t":  "т",
        "ć":  "ћ",
        "ć":  "ћ", # c with acute accent
        "u":  "у",
        "f":  "ф",
        "ﬁ":  "фи",
        "ﬂ":  "фл",
        "h":  "х",
        "c":  "ц",
        "č":  "ч",
        "č":  "ч", # c with caron
        "š":  "ш",
        "š":  "ш", # s with caron
    }

    _cyrillic_to_latin = {
        'Ња' : 'Nja',
        'Ње' : 'Nje',
        'Њи' : 'Nji',
        'Њо' : 'Njo',
        'Њу' : 'Nju',
        'Ља' : 'Lja',
        'Ље' : 'Lje',
        'Љи' : 'Lji',
        'Љо' : 'Ljo',
        'Љу' : 'Lju',
        'Џа' : 'Dža',
        'Џе' : 'Dže',
        'Џи' : 'Dži',
        'Џо' : 'Džo',
        'Џу' : 'Džu',
        'А'  : 'A',
        'Б'  : 'B',
        'В'  : 'V',
        'Г'  : 'G',
        'Д'  : 'D',
        'Ђ'  : 'Đ',
        'Е'  : 'E',
        'Ж'  : 'Ž',
        'З'  : 'Z',
        'И'  : 'I',
        'Ј'  : 'J',
        'К'  : 'K',
        'Л'  : 'L',
        'Љ'  : 'LJ',
        'М'  : 'M',
        'Н'  : 'N',
        'Њ'  : 'NJ',
        'О'  : 'O',
        'П'  : 'P',
        'Р'  : 'R',
        'С'  : 'S',
        'Т'  : 'T',
        'Ћ'  : 'Ć',
        'У'  : 'U',
        'Ф'  : 'F',
        'Х'  : 'H',
        'Ц'  : 'C',
        'Ч'  : 'Č',
        'Џ'  : 'DŽ',
        'Ш'  : 'Š',
        'а'  : 'a',
        'б'  : 'b',
        'в'  : 'v',
        'г'  : 'g',
        'д'  : 'd',
        'ђ'  : 'đ',
        'е'  : 'e',
        'ж'  : 'ž',
        'з'  : 'z',
        'и'  : 'i',
        'ј'  : 'j',
        'к'  : 'k',
        'л'  : 'l',
        'љ'  : 'lj',
        'м'  : 'm',
        'н'  : 'n',
        'њ'  : 'nj',
        'о'  : 'o',
        'п'  : 'p',
        'р'  : 'r',
        'с'  : 's',
        'т'  : 't',
        'ћ'  : 'ć',
        'у'  : 'u',
        'ф'  : 'f',
        'х'  : 'h',
        'ц'  : 'c',
        'ч'  : 'č',
        'џ'  : 'dž',
        'ш'  : 'š'
    }

    _foreign_character_combinations = [
        'q',
        'w',
        'x',
        'y',
        'é',
        'á',
        'à',
        'ó',
        'ò',
        'ü',
        'ö',
        'ä',
        'ê',
        'è',
        'ú',
        'ù',
        'í',
        'ì',
        'ï',
        'ő',
        'ű',
        'ñ',
        'ş',
        'ç',
        'ğ',
        'ı',
        'ł',
        'ý',
        'ø',
        'ß',
        '&',
        '@',
        '#',
        'bb',
        'cc',
        'cs',
        'dd',
        'dh',
        'ee',
        'ff',
        'gg',
        'gy',
        'hh',
        'ie',
        'kk',
        'll',
        'ly',
        'nn',
        'ny',
        'ph',
        'pp',
        'rr',
        'sh',
        'ss',
        'sz',
        'tt',
        'uu',
        'zh',
        'zs',
        'zz',
        'ch',
        'gh',
        'th',
        '\'s',
        '\'t',
        '.com',
        '.edu',
        '.net',
        '.info',
        '.rs',
        '.org',
        '©',
        '®',
        '™'
    ]

    _triple_character_combinations = [
        "aaa", "ccc", "čč", "ćć", "eee", "fff", "hhh", "mmm",
        "ooo", "ppp", "rrr", "sss", "šš", "ttt", "uuu", "vvv", "zzz", "žž"
    ]

    # See: https://en.wikipedia.org/wiki/Zero-width_non-joiner
    _digraph_replacements = {
        "dj": {
            "dj": "d\u200Cj",
            "Dj": "D\u200Cj",
            "DJ": "D\u200CJ",
        },
        "dž": {
            "dž": "d\u200Cž",
            "Dž": "D\u200Cž",
            "DŽ": "D\u200CŽ",
        },
        "nj": {
            "nj": "n\u200Cj",
            "Nj": "N\u200Cj",
            "NJ": "N\u200CJ",
        }
    }

    C_LINE_ENDINGS = ('\r\n', '\n',)


    def __init__(self):
        self.lat_regex = re.compile('|'.join(map(re.escape, self._cyrillic_to_latin)))
        abspath = os.path.abspath(os.path.dirname(__file__))
        self._serbian_words_with_foreign_character_combinations = \
            self._read_list_from_file(os.path.join(abspath,
            'serb_words_with_foreign_combs.txt'))
        self._common_foreign_words = self._read_list_from_file(os.path.join(abspath,
            'serb_common_foreign_words.txt'))
        self._whole_foreign_words = self._read_list_from_file(os.path.join(abspath,
            'whole_foreign_words.txt'))
        self._digraph_exceptions = dict()
        self._digraph_exceptions['nj'] = self._read_list_from_file(os.path.join(abspath,
            'nj_digraph_exceptions.txt'))
        self._digraph_exceptions['dj'] = self._read_list_from_file(os.path.join(abspath,
            'dj_digraph_exceptions.txt'))
        self._digraph_exceptions['dž'] = self._read_list_from_file(os.path.join(abspath,
            'dzh_digraph_exceptions.txt'))


    # Read files with word lists
    def _read_list_from_file(self, filepath):
        with open(filepath, 'r') as f:
            tmplist = f.read().splitlines()
            for elem in tmplist:
                if elem.startswith('#') or elem.strip() == '':
                    tmplist.remove(elem)
            return [line.replace(' ', '') for line in tmplist]


    def _join(self, stri):
        s = ''
        for word in stri:
            if word not in self.C_LINE_ENDINGS:
                s = s + word + " "
            else:
                s = s.strip(' ')
                s = s + word
        return s.strip(' ')


    # Main method that converts Latin text to Cyrillic
    def text_to_cyrillic(self, text):
        if len(text.strip()) == 0:
            return text
        words = re.findall('\S+|\r\n|\n', text)

        for i in range(len(words)):
            if words[i] in self.C_LINE_ENDINGS:
                continue
            index = self._transliteration_index_of_word_starts_with(words[i], self._whole_foreign_words, "-")
            if index >= 0:
                words[i] = words[i][:index] + self._word_to_cyrillic(words[i][index:])
            else:
                if not self._looks_like_foreign_word(words[i]):
                    words[i] = self._word_to_cyrillic(words[i])
        
        return self._join(words)


    def text_to_latin(self, text):
        return self.lat_regex.sub(lambda match: self._cyrillic_to_latin[match.group(0)], text)


    def _looks_like_foreign_word(self, word):
        trimmed_word = self._trim_excessive_characters(word)
        word = trimmed_word.lower()

        if word == "":
            return False

        if self._word_starts_with(word, self._serbian_words_with_foreign_character_combinations):
            return False

        if self._word_contains_string(word, self._triple_character_combinations):
            return False

        if self._word_contains_string(word, self._foreign_character_combinations):
            return True

        if self._word_starts_with(word, self._common_foreign_words):
            return True

        if self._word_is_equal_to(word, self._whole_foreign_words):
            return True

        if self._word_contains_measurement_unit(trimmed_word):
            return True

        return False


    def _word_to_cyrillic(self, word):
        word = self._split_latin_digraphs(word)
        for key, value in self._initial_map.items():
            word = word.replace(key, value)
        return word


    def _split_latin_digraphs(self, str1):
        lowercaseStr = str1.strip().lower()

        for digraph in self._digraph_exceptions:
            if not digraph in lowercaseStr:
                continue

            for word in self._digraph_exceptions[digraph]:
                if not lowercaseStr.startswith(word):
                    continue

                # Split all possible occurrences, regardless of case
                for key in self._digraph_replacements[digraph]:
                    str1 = str1.replace(key, self._digraph_replacements[digraph][key])

                break
        return str1


    def _word_contains_string(self, word, array):
        for array_word in array:
            if array_word in word:
                return True
        return False

    def _word_is_equal_to(self, word, array):
        for array_word in array:
            if word == array_word:
                return True
        return False

    def _word_starts_with(self, word, array):
        for array_word in array:
            if word.startswith(array_word):
                return True
        return False

    def _word_contains_measurement_unit(self, word):
        unit_adjacent_to_sth = "([zafpnμmcdhKMGTPEY]?([BVWJFSHCΩATNhlmg]|m[²³]?|s[²]?|cd|Pa|Wb|Hz))"
        # Removed prefix "h" (hecto-) for meters to allow transliteration of "hm", which is
        # expression of confusion in Serbian language
        unit_optionaly_adjacent_to_sth = "(°[FC]|[kMGTPZY](B|Hz)|[pnμmcdk]m[²³]?|m[²³]|[mcdh][lg]|kg|km)"
        number = "(\d+([\.,]\d)*)"
        regExp = "^(" + number + unit_adjacent_to_sth + ")|(" \
            + number + "?(" + unit_optionaly_adjacent_to_sth + "|" \
            + unit_adjacent_to_sth + "/" + unit_adjacent_to_sth + "))$"

        return re.match(regExp, word) is not None


    """
    Retrieves index of the first character of the word that should be transliterated.
    Function examines only words that have a root that is a foreign word, followed by
    some separator character and remainder of the word which is in Serbian.
    Example: dj-evi should be transliterated as dj-еви so the function retrieves 3.
    """
    def _transliteration_index_of_word_starts_with(self, word, array, char_separator):
        word = self._trim_excessive_characters(word).lower()
        if word == "":
            return -1

        appended_foreign_words = list(map(lambda el: el + char_separator, array))

        for array_word in appended_foreign_words:
            if word.startswith(array_word):
                return len(array_word)

        return -1


    # Trims white spaces and punctuation marks from the start and the end of the word.
    def _trim_excessive_characters(self, word):
        excessive_chars = "[\\s!?,:;\.\*\\-—~`'\"„”“”‘’(){}\\[\\]<>«»\\/\\\\]"
        regexp = "^(" + excessive_chars + ")+|(" + excessive_chars + ")+$"

        return re.sub(regexp, '', word)
