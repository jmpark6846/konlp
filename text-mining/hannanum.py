# -*- coding: utf-8 -*-
import wordgram
import fileio
import tfidf
import ready
from konlpy.tag import Hannanum
from konlpy.utils import pprint
# utf-8 decoding/encoding 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# ====================================


dict_map = wordgram.wordgram_analyze("data/")

result = wordgram.addup(dict_map)

# 모든 문서의 단어 빈도수 딕셔너리를 result.txt에 저장
fileio.write_dict_file("result.txt",result)

tf_idf_map = tfidf.tf_idf_map(dict_map)

# 모든 문서의 단어 tf-idf 값 딕셔너리를 result2.txt에 저장
fileio.write_list_file("result2.txt",tf_idf_map)

