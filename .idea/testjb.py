import jieba

seg_list = jieba.cut("我想过过过儿过过的生活", cut_all=True)
print("full mode: " + "/".join(seg_list))
seg_list = jieba.cut("用毒毒毒蛇毒蛇会不会被毒毒死", cut_all=False)
print("full mode: " + "$".join(seg_list))
seg_list = jieba.cut_for_search("用毒毒毒蛇毒蛇会不会被毒毒死")
print("--".join(seg_list))

