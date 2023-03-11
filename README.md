# **Serbian language word corpus**

This directory hosts various word corpus annotated files in Serbian language, transliterated into Serbian Cyrillic script. Main information about each source is given below. 

## **Source files**

List of source files.

### **SETimes.SRPlus**

**URL**: https://github.com/reldi-data/SETimes.SRPlus/blob/master/set.sr.plus.conllu

**Transliterated file**:

- [ser.sr.plus.cyr.conllu](https://github.com/strn/spacy-sr/blob/main/ser.sr.plus.cyr.conllu)

**Note**: The resource is [An extended and updated version of the original SETimes.SR annotated corpus](https://github.com/reldi-data/SETimes.SRPlus/blob/master/README.md) The original (base) SETimes.SR annotated corpus is [here](https://vukbatanovic.github.io/SETimes.SR).

**License**: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) (see the bottom of URL)

### **UD_Serbian_Set**

**URL**: https://github.com/UniversalDependencies/UD_Serbian-SET

**Transliterated files**:

- [sr_set_cyr-ud-dev.conllu](https://github.com/strn/spacy-sr/blob/main/sr_set_cyr-ud-dev.conllu) (development)
- [sr_set_cyr-ud-test.conllu](https://github.com/strn/spacy-sr/blob/main/sr_set_cyr-ud-test.conllu) (test)
- [sr_set_cyr-ud-train.conllu](https://github.com/strn/spacy-sr/blob/main/sr_set_cyr-ud-train.conllu) (training)
  
**License**: [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://github.com/UniversalDependencies/UD_Serbian-SET/blob/master/LICENSE.txt)

### **Annotated corpus of Serbian language-related news and comments: MetaLangNEWS-COMMENTS-Sr**

**URL**: https://www.clarin.si/repository/xmlui/handle/11356/1372

**Transliterated files**:

- [sr-news-cyr.zip](https://github.com/strn/spacy-sr/blob/main/sr-news-cyr.zip)

**License**: [Creative Commons - Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

## **Transliteration**

Transliteration was performed by simple Python script `connlutrans.py` in this directory. Only sentences, word forms and lemmas were transliterated.

### **Usage**

#### Single file transliteration

`connlutrans.py -i <input_file> -o <output_file>`

#### Multiple file transliteration

`connlutrans.py -i <input_directory>/* -o <output_directory>`

Output files will be placed in output directory, with infix `-cyr` right before the extension.
