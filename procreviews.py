from pygg import *
from wuutils import *
from collections import *
f = file("reviews.md") 
pat = re.compile("\w+\d+")

reviews = []
d = {}
uni = ""

for l in f:
  if l.startswith("# "):
    topic = l[2:].strip()
    d = defaultdict(list)
    reviews.append((topic, d))
    uni = ""
  elif l.startswith("##"):
    try:
      uni = pat.search(l).group().strip()
    except Exception as e:
      print(l)
      uni = l[2:].strip().lower()
  else:
    d[uni].append(l.strip())

data = []
for i, (topic, d) in enumerate(reviews):
  for uni in d:
    review = " ".join(d[uni])
    nwords = len(review.split())
    if nwords == 0: continue
    data.append(dict(
      i = i,
      uni = uni,
      topic = topic,
      y = nwords
    ))

postfix = """
data$topic = factor(data$topic, levels=c(%s))
""" % ",".join([esc(topic) for (topic, _) in reviews])
p = ggplot(data, aes(x='topic', y='y'))#, color='uni', fill='uni'))
p += geom_point(alpha=0.8)
p += geom_boxplot()
p += axis_labels("Class", "Review Len", "discrete")
p += coord_flip()
p += legend_bottom
ggsave("review_nwords.png", p, postfix=postfix, width=6, height=5)

data = []
for i, (topic, d) in enumerate(reviews):
  data.append(dict(
    i = i,
    topic=topic,
    n = len(d)))

postfix = """
data$topic = factor(data$topic, levels=c(%s))
""" % ",".join([esc(topic) for (topic, _) in reviews])
p = ggplot(data, aes(x='topic', y='n'))#, color='uni', fill='uni'))
p += geom_bar(stat=esc("identity"), width=0.5, color=esc("gray"), fill=esc("gray"))
p += geom_text(aes(x=esc("Multidim indexes"), y=20, label=esc("A1") ))
p += geom_text(aes(x=esc("Cascades"), y=20, label=esc("A2+Proposal") ))
p += geom_text(aes(x=esc("Batch Dataflow"), y=20, label=esc("A3") ))
p += geom_text(aes(x=esc("Streaming Research"), y=20, label=esc("A4") ))
p += geom_text(aes(x=esc("IVM"), y=20, label=esc("Draft") ))
p += geom_text(aes(x=esc("OCC and MVCC"), y=20, label=esc("A5") ))
p += axis_labels("Class", "# Reviews", "discrete", "continuous")
p += coord_flip()
p += ylim(lim=[0, 25])
p += legend_bottom
ggsave("review_nreviews.png", p, postfix=postfix, width=6, height=5)


