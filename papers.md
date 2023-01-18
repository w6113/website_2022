---
layout: page
---

<!--
# Paper Reviews

You are expected to write and submit a paper review of the readings before each class, and answer some questions about the readings.  The review should be akin to a conference paper review.  The purpose of the readings is to provide an illustrative example of the research area.  You are encouraged but not required to read the supplemental readings to better understand the materials.  

You can discuss questions and ask for clarifications with your colleagues and/or on piazza.  You are expected to formulate your own opinion of the reading(s) and write the review yourself.  See for a description of what we expect in paper reviews.  

We may select a random review to read and discuss in class.  This serves to highlight important characteristics of reading papers and writing good reviews.


### Submission

Overview

* Reviews are due **10AM EST one day before lecture** (except for the Indexes paper which is due on Tue, 9/15).  
* Late submissions are given a score of 0 without prior approval.  
* You may miss submissions for up to **4 lectures**.
* To submit:
  * [**Go to the class wiki**](https://github.com/w6113/w6113.github.io/wiki) and click on the appropriate topic
  * Read the instructions at the top
  * Click "Edit" in the upper right. 
  * Add your review
-->

### Reading Tips

Ask the following questions while readings

* What is the context of this work?
  * What was the unmet need or opportunity?  Does it make sense?
  * What were existing approaches and why do they work or not work?
  * What is the simplest example that highlights the problem that this approach works best for?
  * Does the paper (and its contributions) matter?
  * What are the actual hypotheses?
* Approach
  * How do they seek to validate their hypotheses? Do they make sense?
  * Is the evaluation cursory or deep?
  * Do you believe their results?
  * Are the results presented well?


Papers on how to read papers

* [How to Read a Paper - S. Keshav](https://dl.acm.org/doi/pdf/10.1145/1273445.1273458)
* [How to Read a Research Compendium - Nüst et al.](https://arxiv.org/pdf/1806.09525.pdf)

Some papers on reviewing papers

* [Review AntiPatterns (written for FSE 14 PC)](https://homes.cs.washington.edu/~mernst/advice/review-antipatterns-devanbu.txt)
* [Ethics of Peer Review](https://ori.hhs.gov/sites/default/files/prethics.pdf)
* [How NOT to review a paper](https://sigmodrecord.org/publications/sigmodRecord/0812/p100.open.cormode.pdf)
* [Conference Reviewing Considered Harmful](https://homes.cs.washington.edu/~tom/support/confreview.pdf): A view on how reviewing works in practice.



# The Papers

<a name='review1' />
### Review

Required

* [Architecture of RDBMS Survey](./files/papers/archdbsys-fntdb07.pdf)
* [What goes around comes around](./files/papers/whatgoesaround-stonebraker.pdf) (skim)


Further Reading

* [Query Evaluation Techniques for Large Databases](https://dl.acm.org/doi/pdf/10.1145/152610.152611)


<a name='indexes' />
### Indexes    

Required

* Required Background: [Generalized Search Trees for Database Systems](./files/papers/gist-vldb95.pdf)
* Main Topic: [Case for Learned Indexes](https://courses.cs.washington.edu/courses/csep544/21sp/papers/kraska-case-for-learned-index-sigmod-2018.pdf)  ([youtube talk](https://www.youtube.com/watch?v=MM33CvATm_M))



Further reading 

* Classic Indexes
  * [R-Trees: A Dynamic Index Structure for Spatial Searching](./files/papers/rtree-gut84.pdf)
  * [An Experimental Evaluation and Investigation of Waves of Misery in R-trees](https://www.vldb.org/pvldb/vol15/p478-aref.pdf)
  * [Survey: Modern B-Tree Techniques](./files/papers/btreesurvey-graefe.pdf)
  * [The Log-structured merge-tree (LSM-tree)](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C10&q=The+log-structured+merge-tree+%28LSM-tree%29&btnG=)
* Generating New Index Designs using ML
  * [The Next 50 Years in Database Indexing](https://dl.acm.org/doi/abs/10.14778/3494124.3494136)
  * [The Data Calculator](https://faculty.cc.gatech.edu/~jarulraj/courses/8803-f18/papers/data_calculator.pdf) ([youtube talk](https://www.youtube.com/watch?v=uFtkA3CEWY0))
* Learned Indexes
  * [Revenge of Interpolation Search](https://pages.cs.wisc.edu/~jignesh/publ/Revenge_of_the_Interpolation_Search.pdf)
  * [Qd-tree](https://dl.acm.org/doi/10.1145/3318464.3389770)
  * [Tsunami: Learned Multi-dim Indexes](https://arxiv.org/pdf/2006.13282.pdf?TB_iframe=true&width=370.8&height=658.8)


<a name='join' />
### Joins   

Required

* Required Background: [Worst Case Optimal Joins](https://columbiadb.github.io/files/papers/optimaljoin.pdf) Sections 1, 2, 4.2
* Main Topic: [SkinnerDB: Regret-Bounded Query Evaluation via Reinforcement Learning](https://arxiv.org/pdf/1901.05152.pdf)

Further reading

* Large-than-memory Joins
  * [Shapiro: Join Processing in Database Systems with Large Main Memories](./files/papers/gracejoin-shapiro.pdf)
* Adaptive Joins
  * [Ripple Joins for Online Aggregation](http://www.cs.cmu.edu/~natassa/courses/15-823/F02/papers/decision-ripple-sigmod99.pdf)
* Distributed Joins
  * The Classic [R\* Optimizer](https://www.seas.upenn.edu/~zives/05s/cis650/papers/r-star.pdf) Sections 5 onward
  * [The Gamma database machine project](https://wiki.epfl.ch/edicpublic/documents/Candidacy%20exam/gamma.pdf)
  * [TrackJoin](./files/papers/trackjoin-sigmod14.pdf)
  * [Parallel Database systems: the future of high performance database systems](./files/papers/paralleldbsystems-dewitt.pdf)
  * [Pushing Data-Induced Predicates Through Joins in Big-Data Clusters](http://www.vldb.org/pvldb/vol13/p252-orr.pdf)



<a name='qopt' />
### Query Optimization

Readings

* Required Background: [Orca: A Modular Query Optimizer Architecture for Big Data](./files/papers/orca.pdf)
* Required Background: [What We Found Running the Join Order Benchmark](https://db.in.tum.de/~leis/papers/lookingglass.pdf)
* Main Topic: [Bao: Learning to Steer Query Optizers](https://arxiv.org/pdf/2004.03814.pdf)

Further reading 

* [Designing an Open Framework for Query Optimization and Compilation](https://www.vldb.org/pvldb/vol15/p2389-jungmair.pdf)
* Classics Optimizer Design
  * [Volcano Optimizer](./files/papers/volcanooptimizer-icde93.pdf)
  * [Cascades](./files/papers/cascades-graefe.pdf)
  * [Dynamic programming strikes back](https://dl.acm.org/doi/pdf/10.1145/1376616.1376672)
* Optimizers in Industry
  * [PostgreSQL Optimizer Documentation](https://www.postgresql.org/docs/current/geqo.html)
  * [Cockroach blogpost: How we built a cost-based SQL optimizer](https://www.cockroachlabs.com/blog/building-cost-based-sql-optimizer/)
  * [Book: Inside the SQLServer Query Optimizer](./files/papers/inside-the-sql-server-query-optimizer.pdf)
* Learned Optimizers
  * [Learning to Optimize Join Queries With Deep Reinforcement Learning](https://arxiv.org/pdf/1808.03196.pdf)
  * [Selectivity Estimation using Probabilistic Models](https://ai.stanford.edu/~koller/Papers/Getoor+al:SIGMOD01.pdf)
  * [Leo - DB2's Learning Optimizer](https://www.vldb.org/conf/2001/P019.pdf)

<!--* [CH Benchmark](https://db.in.tum.de/research/projects/CHbenCHmark/index.shtml?lang=en)-->


<a name="costest"/>
### Cost Estimation

Required 

* Required Background: [What We Found Running the Join Order Benchmark](https://db.in.tum.de/~leis/papers/lookingglass.pdf)
* Main Topic: [Are We Ready For Learned Cardinality Estimation?](https://arxiv.org/pdf/2012.06743.pdf)


Further Reading

* [DeepDB](https://arxiv.org/pdf/1909.00607.pdf)
* [Learned Cardinalities](https://www.cidrdb.org/cidr2019/papers/p101-kipf-cidr19.pdf)
* [Cardinality Estimation in DBMS: A Comprehensive Benchmark Evaluation](https://www.vldb.org/pvldb/vol15/p752-zhu.pdf)
* [Learned Cardinality Estimation: An In-depth Study](https://dl.acm.org/doi/pdf/10.1145/3514221.3526154)
* [Learning Optimizer for Shared Clouds](http://www.vldb.org/pvldb/vol12/p210-wu.pdf)


<a name="cc"/>
### Concurrency Control

Required

* Required Background: TBA
* Main Topic: TBA

Further Reading

* [Concurrency Control in Distributed Database Systems](./files/papers/bernstein-csur1981.pdf)
* [Seeing is Believing](https://drive.google.com/file/d/1we7ok4C8ra2-6fP1yT7EJ-Rv9LSGCiUt/view)
* [On Optimistic Methods for Concurrency Control](http://sites.fas.harvard.edu/~cs265/papers/kung-1981.pdf)
* [An Empirical Evaluation of In-Memory Multi-Version Concurrency Control](http://www.vldb.org/pvldb/vol10/p781-Wu.pdf) 
* [Optimistic Lock Coupling](https://web.archive.org/web/20220306194839id_/http://sites.computer.org/debull/A19mar/p73.pdf)



<a name="memstore"/>
### Main-memory Query Execution

Required 

* Required Background: [Efficiently Compiling Efficient Query Plans for Modern Hardware](./files/papers/p539-neumann.pdf)
* Main Topic: [Morsel-Driven Query Execution](./files/papers/morsel.pdf)

Further Reading

* Vectorization
  * [MonetDB/X100: Hyper-Pipelining Query Execution](./files/papers/monetdb-cidr05.pdf)
  * [Blog Post: 40x faster hash joiner with vectorized execution](https://www.cockroachlabs.com/blog/vectorized-hash-joiner/)
* Compilation
  * [How to Architect a Query Compiler, Revisited](./files/papers/tahboub-sigmod18.pdf)
  * [Generating code for holistic query evaluation](./files/papers/krikellas-icde2010.pdf)
  * [Spark's Scala expression compiler code](https://github.com/apache/spark/blob/master/sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/expressions/codegen/CodeGenerator.scala)
  * [MemSQL's blogpost](http://highscalability.com/blog/2016/9/7/code-generation-the-inner-sanctum-of-database-performance.html)
* Compilation in other data intensive domains
  * [Halide](https://dspace.mit.edu/handle/1721.1/85943)
* In-Memory Systems
  * [Leanstore](./files/papers/leanstore.pdf)


Some things to think about when reading

* For disk-based systems, when would query compilation be useful?



<a name='dataflow1' />
### Data Flow

Required

* Required Background: TBA
* Main Topic: [Naiad: A Timely Dataflow System](https://www.microsoft.com/en-us/research/wp-content/uploads/2013/11/naiad_sosp2013.pdf) ([Video introduction](https://www.youtube.com/watch?v=yOnPmVf4YWo), [commercial software](https://materialize.io/))

Further Reading

* [(Survey) State of the Art in Large scale Data Flow](./files/papers/kossmann-sotadistdbs.pdf)
* Classics
  * [Encapsulation of parallelism in the volcano query processing system](./files/papers/volcanoparallelism-89.pdf)
  * [SEDA: An Architecture for Well-Conditioned, Scalable Internet Services](http://www.sosp.org/2001/papers/welsh.pdf)
  * [CIEL](https://www.cs.princeton.edu/courses/archive/fall13/cos518/papers/ciel.pdf)
  * [RDDs](https://sfu-db.github.io/dbsystems/Papers/nsdi12-final138.pdf)
* Big Data Era 
  * [MapReduce](https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf)
  * [SparkSQL](https://sfu-db.github.io/dbsystems/Papers/SparkSQLSigmod2015.pdf)
  * [Spark (mainly examples)](http://static.usenix.org/events/hotcloud10/tech/full_papers/Zaharia.pdf)
  * [DryadLinq](http://michaelisard.com/pubs/sigmod09.pdf)
  * [Discretized Streams](https://people.csail.mit.edu/matei/papers/2013/sosp_spark_streaming.pdf)
* More Timely Dataflow
  * [Earlier CIDR paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2013/01/differentialdataflow.pdf)
  * [Timely Dataflow Code](https://github.com/TimelyDataflow/timely-dataflow)
  * [Scalability! But at what COST?](https://www.usenix.org/system/files/conference/hotos15/hotos15-paper-mcsherry.pdf)



Some notes to guide your reading and thinking.  

* This paper focuses primarily on what Naiad provides and how it works.  But which are actually _necessary_?  Which are nice-to-haves?  Why?  How does it contrast with other papers we have read (spark, spark streaming, recursive queries)?  Can it do things other systems cannot?   
* What makes this paper easy or hard to read?  Note those, and other questions you have, in the comments, and we can discuss in class
* We will go over some of the technical details of how execution operates



<a name="mlindb" />
### In-DBMS ML

Required

* Required Background: [MAD Skills: New Analysis Practices for Big Data](http://db.cs.berkeley.edu/papers/vldb09-madskills.pdf)
* Main Topic: [Towards a Unified Architecture for in-RDBMS Analytics](https://cs.stanford.edu/people/chrismre/papers/bismarck.pdf)


Further Reading

* [Technical Debt in ML Systems](https://ckaestne.medium.com/technical-debt-in-machine-learning-systems-62035b82b6de)
* [Operationalizing Machine Learning: An Interview Study](#)
* [Incrementally Maintaining Classification using an RDBMS](http://www.vldb.org/pvldb/vol4/p302-koc.pdf)


<a name="mljoin" />
### In-DBMS ML over Joins


Required

* Required Background: [Dan Olteanu's VLDB 2020 Keynote](https://www.youtube.com/watch?v=0ic0jMjOpM0) and [skim the paper](http://www.vldb.org/pvldb/vol13/p3502-olteanu.pdf)
* Main Topic: [Learning Generalized Linear Models Over Normalized Data](http://pages.cs.wisc.edu/~jignesh/publ/GLMs-over-joins.pdf)

Further Reading

* [JoinBoost: Gradient Boosted Trees over Joins](#)
* [Towards Linear Algebra over Normalized Data](http://www.vldb.org/pvldb/vol10/p1214-chen.pdf)




<a name='udfs' />
### Hybrid Caching/UDFs    

Required

* Required Background: [Optimization of Queries with User-defined Predicates](http://www.vldb.org/conf/1996/P087.PDF)
* Main Topic: [User-Defined Operators](https://www.vldb.org/pvldb/vol15/p1119-sichert.pdf)

Further Readings

* [Froid: Optimizing Imperative Programs in RDBMSes](./files/papers/froid.pdf) ([Research Talk](https://www.youtube.com/watch?v=Xyvpcf2RtO4))
* [YeSQL: “You extend SQL”](https://www.vldb.org/pvldb/vol15/p2270-foufoulas.pdf)
* [Tuplex: Data Science in Python at Native Code Speed](http://cs.brown.edu/~lspiegel/files/Tuplex_Preprint2020.pdf)
* [Exploiting Correlations for Expensive Predicate Evaluation](https://arxiv.org/pdf/1411.3374.pdf)
* [Probabilistic Predicates](https://www.microsoft.com/en-us/research/publication/accelerating-machine-learning-queries-with-probabilistic-predicates/)
* [Compiling PL/SQL Away](https://arxiv.org/pdf/1909.03291.pdf)
* [Hybrid Caching](./files/papers/caching-sigmod1996.pdf)
* [Flare: Optimizing Apache Spark with Native Compilation](https://www.usenix.org/system/files/osdi18-essertel.pdf)


### Data Quality

Required

* Required Background: [From Cleaning Before ML to Cleaning For ML](http://sites.computer.org/debull/A21mar/p24.pdf)
* Main Topic: [Can Foundation Models Wrangle Your Data?](https://arxiv.org/abs/2205.09911)

Further Reading:

* [HoloClean](https://arxiv.org/pdf/1702.00820.pdf)
* [Complaint-Driven Training Data Debugging](https://dl.acm.org/doi/pdf/10.1145/3533028.3533305)


<a name="datamarkets"/>
### Data Markets

Required

* Required Background: [Revising Online Data Markets in 2022](http://raulcastrofernandez.com/papers/7_31CRstatusofDataMarkets_final.pdf)
* Main Topic: TBA

Further Reading

* [Data Station](https://dl.acm.org/doi/abs/10.14778/3551793.3551861)
* [Aurum](https://dspace.mit.edu/bitstream/handle/1721.1/137860/icde18-aurum.pdf?sequence=2&isAllowed=y)
* [Kitana](#)
* [Selective Data Acquisition in the Wild for Model Charging](https://www.vldb.org/pvldb/vol15/p1466-li.pdf)
* Data Markets in the Wild
  * Snowflake, Amazon, etc



<a name="optional" />
## Unscheduled Topics


<a name="sysr"/>
### System R Overview 

Readings 

* Required: <a href="./files/papers/systemr-retrospective.pdf">System R Retrospective</a>
* Optional: <a href="./files/papers/ingres-retrospective.pdf">Ingres Design</a>


Questions to consider

* System R was an impressive research and engineering effort, and the reading is a retrospective of the 6 year project.  
* The paper discusses "the Convoy Problem".  Discuss the problem:  What is it?  Why does it exist?
* The paper discusses many many topics.  Identify and pick one aspect (different than the convoy problem) that you are particularly impressed with.  Discuss what and why.


<a name='postgres' />
### INGRES/POSTGRES    

Readings

* Required: [Design of Postgres (Initial design)](./files/papers/postgres-retrospective.pdf)
* Optional: [The Postgres Next-Generation DBMS (Midterm design)](./files/papers/postgres-nextgen-cacm.pdf)
* Optional: [Design of INGRES](./files/papers/ingres-retrospective.pdf)
  * Worth skimming: QUEL, leveraging UNIX, concurrency control arguments
* Optional: [The Landsharks are on the Squawk Box - Stonebraker Turing Award Lecture](https://cacm.acm.org/magazines/2016/2/197423-the-land-sharks-are-on-the-squawk-box/fulltext)


Questions to consider

* What were the main goals for the Postgres system and why do you think they chose those goals?  Do they make sense?
* Pick one of the (many) ideas in the paper that most interests you.  Why is it interesting?   Does the proposed design hold water?  Feel free to read related work.





<a name='oltp' />
### OLTP Stores    


* [OLTP Through the Looking Glass, and What We Found There](./files/papers/oltpperf-sigmod08.pdf)
* [Hekaton: SQL Server’s Memory-Optimized OLTP Engine](./files/papers/hekaton-sigmod13.pdf)
* [The End of an Architectural Era](http://nms.csail.mit.edu/~stavros/pubs/hstore.pdf)


<a name='colstore' />
### Column Stores    

Readings

* [C-Store: A Column-oriented DBMS ](./files/papers/cstore-vldb05.pdf)
* [MonetDB/X100: Hyper-Pipelining Query Execution](./files/papers/monetdb-cidr05.pdf)
* [Integrating Compression and Execution in Column-Oriented Database Systems](./files/papers/abadi-sigmod2006.pdf)
* [An Experimental Study of Bitmap Compression vs. Inverted List Compression](./files/papers/sidm338-wangA.pdf)
* [Column-Stores vs. Row-Stores: How Different Are They Really?](http://www.cs.umd.edu/~abadi/papers/abadi-sigmod08.pdf)
* [Survey: The Design and Implementation of Modern Column-Oriented Database Systems](https://stratos.seas.harvard.edu/files/stratos/files/columnstoresfntdbs.pdf)
* [Blog Post: 40x faster hash joiner with vectorized execution](https://www.cockroachlabs.com/blog/vectorized-hash-joiner/)



<a name="clouddb" />
### Cloud-scale Analytics

* [Dremel Test-of-Time Keynote](https://www.youtube.com/watch?v=9GutzPX6ufo)
* [The Snowflake Elastic Data Warehouse](./files/papers/snowflake.pdf)
* [Dremel: A Decade of Interactive SQL Analysis at Web Scale](http://www.vldb.org/pvldb/vol13/p3461-melnik.pdf)
* [Original Dremel paper](https://dl.acm.org/doi/pdf/10.14778/1920841.1920886)
* [Dewitt's Cloud DB talk slides](./files/papers/dewittclouddbtalk.pptx)
* [Choosing a Cloud DBMS](./files/papers/choosingclouddb.pdf)



<a name="rep"/>
### DB and Query Representations

* [QueryFormer: A Tree Transformer Model for Query Plan Representation](https://www.vldb.org/pvldb/vol15/p1658-zhao.pdf)
* [TURL: Table Understanding through Representation Learning](https://research.google/pubs/pub52020/)
* [Sato: Contextual Semantic Type Detection in Tables](https://arxiv.org/abs/1911.06311)


<a name="replication" />
### Distributed Consistency under Replication

* [The original Raft paper](https://raft.github.io/raft.pdf)
* [Viewstamped Replication Revisited](http://pmg.csail.mit.edu/papers/vr-revisited.pdf)
* [Living Without Atomic Clocks blog post](https://www.cockroachlabs.com/blog/living-without-atomic-clocks/)
* [Raft Refloated](http://www.cl.cam.ac.uk/~ms705/pub/papers/2015-osr-raft.pdf) 
* [Google's Paxos Made LIve](https://research.google.com/archive/paxos_made_live.html)
* [Anna: A Crazy Fast, Super-Scalable, Flexibly Consistent KVS](https://rise.cs.berkeley.edu/blog/anna-kvs/)


<a name='matviews' />
### Materialized Views    



* [Survey: Materialized Views](./files/papers/matview-survey.pdf) Ch 1,2,4
* [Noria: dynamic, partially-stateful data-flow for high-performance web applications](https://pdos.csail.mit.edu/papers/noria:osdi18.pdf)

Further Reading

* Materialized Views
  * [CrocodileDB: Efficient Database Execution through Intelligent Deferment](http://cidrdb.org/cidr2020/papers/p14-shang-cidr20.pdf)
* Applications as Materialized Views
  * [Convex](https://www.youtube.com/watch?v=iizcidmSwJ4CMU)
  * [Do-It-Yourself Database-Driven Web Applications](https://www.skylineuniversity.ac.ae/pdf/database/Database%20driven%20web%20sites.pdf)
  * [DVMS](#)
  * [QUILT](https://dl.acm.org/doi/pdf/10.1145/2642918.2647387)
  * [Building data-centric apps with a reactive relational database](https://riffle.systems/essays/prelude/)


<a name="incmatviews" />
### Incrementally Maintaining Materialized Views

* [DBToaster](https://dbtoaster.github.io/papers/pvldb2012-dbtoaster.pdf) ([Talk](https://dbtoaster.github.io/papers/ecocloud2013-dbtoaster-mn.pdf), [theory](https://dbtoaster.github.io/papers/pods2010-ring.pdf))
* [Intermittent Query Processing](http://www.vldb.org/pvldb/vol12/p1427-tang.pdf)


<a name="stream" />
### Streaming

* [Aurora](http://cs.brown.edu/research/aurora/vldb03_journal.pdf)
* [Flink](http://www.vldb.org/pvldb/vol10/p1718-carbone.pdf)


<a name='datalog' />
### Datalog and Recursion   

Readings

* Required: [Datalog and Recursive Query Processing](https://www.nowpublishers.com/article/Details/DBS-017) Chapters 2, 3
* Optional: [Evita Raced: Metacompilation for Declarative Networks](http://www.vldb.org/pvldb/1/1453978.pdf): query optimization AS datalog

Questions

* When you assess the reading, compare against other formal and informal data query languages we have encountered.  



<a name='lineage' />
### Lineage   


* [Provenance Semirings](http://db.cis.upenn.edu/DL/07/pods07.pdf)
* [SMOKE: Fine-grained Lineage at Interactive Speed](http://www.vldb.org/pvldb/vol11/p719-psallidas.pdf)
* [Application of provenance to vis](https://www.dropbox.com/s/fkp5hk1gp4lrg9h/smoke-hilda18.pdf?dl=0)

Question to comment on:

* Provenance goes beyond what they mention in the paper and is _everywhere_.  Point out a concept/functionality in the real (or digital) world that can be recast as provenance and provenance queries.  Describe it.

<a name='lineage2' />
### Lineage Systems

Read one of the two required papers:

* [SMOKE: Fine-grained Lineage at Interactive Speed](http://www.vldb.org/pvldb/vol11/p719-psallidas.pdf)
* [Perm: Processing provenance and data on the same data model through query rewriting](https://www.zora.uzh.ch/id/eprint/24446/2/main.pdf)
* [GPROM: Middleware implementation for PERM](https://par.nsf.gov/servlets/purl/10082097)
* [Provenance for Interactive Visualizations](https://www.dropbox.com/s/32aid7isd2arx47/smoke-hilda18-cr.pdf?dl=0)
* [Titian: Data Provenance Support in Spark](http://www.vldb.org/pvldb/vol9/p216-interlandi.pdf)




<!--
<a name='mockpc' />
### MockPC  

Readings:

* Your assigned papers
-->







<!--
<a name='sampling' /> 
### Visualization/Sampling

* Required: [BlinkDB](https://sameeragarwal.github.io/blinkdb_eurosys13.pdf)
* Optional: [Dynamic Sample Selection for Approximate Query Processing](http://www-cs-students.stanford.edu/~babcock/papers/sampling.pdf)
-->

<a name="serverless"/>
### Serverless Querying

* Required: [Cloudburst: Stateful Functions-as-a-Service](https://arxiv.org/abs/2001.04592)
  * Using a distributed KV-store to autoscale stateful functions
* Optional: [Starling: A Scalable Query Engine on Cloud Function Services](https://arxiv.org/pdf/1911.11727.pdf)
  * Running OLAP on serverless
* Optional: [Serverless Computing: One Step Forward, Two Steps Back](http://cidrdb.org/cidr2019/papers/p119-hellerstein-cidr19.pdf)
* Optional: [Autoscaling Tiered Cloud Storage in Anna](https://dsf.berkeley.edu/jmh/papers/anna_vldb_19.pdf)
  * The discributed KV-store used in Cloudburst



<a name='selftuning' /> 
### Self-tuning DBs  

* Required: [Self-Tuning Database Systems: A Decade of Progress ](./files/papers/selftuning-chaudhuri-vldb07.pdf)
* Optional: [Automatically Indexing Millions of Databases in Microsoft Azure SQL Database](https://www.microsoft.com/en-us/research/uploads/prod/2019/02/autoindexing_azuredb.pdf)
* Optional: [Query-based Workload Forecasting for Self-Driving Database Management Systems](https://www.cs.cmu.edu/~dvanaken/papers/forecasting-sigmod18.pdf)
* Optional: [Database Cracking](https://stratos.seas.harvard.edu/files/IKM_CIDR07.pdf)



<a name='aqp' />
### Approximate Query Processing

* [BlinkDB](https://sameeragarwal.github.io/blinkdb_eurosys13.pdf)
* [Pfunk-H](https://columbiaviz.github.io/files/papers/pfunk.pdf)
* [Sample+Seek](https://columbiaviz.github.io/files/papers/sigmod16sampleseek.pdf)
* [WanderJoin](https://columbiaviz.github.io/files/papers/wanderjoin.pdf)
* [Rapid Approximate Aggregation with Distribution-Sensitive Interval Guarantees](https://arxiv.org/pdf/2008.03891.pdf)

<a name='stream' />
### Windows and Streaming

* [The Dataflow Model](http://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf)
* [Continuous Query Language](http://ilpubs.stanford.edu:8090/758/1/2003-67.pdf) 


<a name='scans' />
### Fast Scans

* [Column Sketches](https://stratos.seas.harvard.edu/files/stratos/files/sketches.pdf)
* [BitWeaving](http://www.cs.wisc.edu/~jignesh/publ/BitWeaving.pdf)
* [WideTables](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.650.2556&rep=rep1&type=pdf)
* [Vectorizing Database Column Scans with Complex Predicates](http://www.adms-conf.org/2013/muller_adms13.pdf)


<!--
<a name='lineage3' />
### Using Lineage

* Optional: [Querying and Creating Visualizations by Analogy](http://www.cs.utah.edu/~juliana/pub/tvcg-analogy2007.pdf)
* Optional: [VisTrails: Enabling Interactive Multiple-View Visualizations](https://vgc.poly.edu/~juliana/pub/vistrails-vis2005.pdf)
-->

<a name='datacubes' />
### Data Cubes    

* [Data Cube](./files/papers/datacube-jimgray.pdf)
* [Implementing Data Cubes Efficiently](http://ilpubs.stanford.edu:8090/102/1/1995-34.pdf)
* [Gaussian Cubes: Real-Time Modeling for Visual Exploration of Large Multidimensional Datasets](https://cscheid.net/static/papers/infovis_gaussian_cubes_2016.pdf)

<a name="obliv"/>
### Oblivious Databases

* [ObliDB](http://www.vldb.org/pvldb/vol13/p169-eskandarian.pdf)
* [Efficient Oblivious Database Joins](http://www.vldb.org/pvldb/vol13/p2132-krastnikov.pdf)
* [SMCQL: Secure Querying for Federated Databases](http://users.eecs.northwestern.edu/~jennie/pubs/smcql.pdf)

<a name='eddies' />
### Adaptive Query Processing

Readings

* [Micro Adaptivity in Vectorwise](https://dl.acm.org/doi/pdf/10.1145/2463676.2465292)
* [Eddies: Continuously Adaptive Query Processing](./files/papers/eddies-sigmod00.pdf)
* [Adaptive Execution of Compiled Queries](https://db.in.tum.de/~leis/papers/adaptiveexecution.pdf)

Further Reading

* [Survey: Adaptive Query Processing](https://www.nowpublishers.com/article/Details/DBS-001)
* [TelegraphCQ: Continuous Dataflow Processing for an Uncertain World](http://db.csail.mit.edu/madden/html/TCQcidr03.pdf)
* [Worst Case Optimal Joins](https://columbiadb.github.io/files/papers/optimaljoin.pdf)

<a name="explanation" />
### Explanation

Readings

* Required: [Scorpion: Explaining away outliers in aggregate queries](http://sirrice.github.io/files/papers/scorpion-vldb13.pdf)
* Required: [DIFF: A Relational Interface for Large-Scale Data Explanation](http://www.vldb.org/pvldb/vol12/p419-abuzaid.pdf)

Further Reading

* [Explaining differences in multidimensional aggregates](./files/papers/olapdiff-sunita.pdf)
* [Rain: Complaint-driven Training Data Debugging for Query 2.0](https://arxiv.org/pdf/2004.05722.pdf)
* Related codebases
  * https://github.com/PiotrZakrzewski/macrobase-diff
  * https://datools.readthedocs.io/en/latest/



<!--
<a name="pvd"/>
### Physical Database Design
-->

