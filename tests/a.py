from pyhanlp import HanLP

text = '随着人工智能2.0时代的到来与深度学习的火热发展，自然语言方面的任务越来越受到关注，并吸引了许多学术界和产业界的目光。'
nlp = HanLP.segment(text)

text = 'gposted插件（被动监控）例子：假设命中以下条件规则：那么消息模版里context.hits、context.matches的值如下：这里好像换成d 也取不到 20 ，反而取了监控获取到的loss值'

phrase = HanLP.extractPhrase(text,5)

print(HanLP.convertToPinyinList(text))
