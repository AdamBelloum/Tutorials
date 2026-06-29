Brief history of AI
From its Foundation to
         Generative AI

“A generation which ignores history
has no past – and no future.” - Robert
A Heinlein

https://events.vtools.ieee.org/m/428481

“As soon as it works, no one calls it AI
anymore.” - John McCarthy

Source: History of A.I.: Artificial Intelligence (Infographic)

https://www.livescience.com/47544-history-of-a-i-artificial-intelligence-infographic.html

“Students in every major will need to know how
to challenge or defend the appropriateness of a
given model for a given question.” -  Chronicle of
Higher Ed

• Computer programming

• Knowledge centric (human learning)
• Data centric (machine learning)
• Training (years vs Bytes)

• Big data

• Data movement
• Data processing
• Data storage

• Artificial Intelligence terminology /landscape

• AI origins
• AI milestones (perceptron – DL)
• AI between Hype/fiction/Reality
• Deep Learning
• Problem and Security (hallucination,
• Ethics (Black box,
•

Understanding AI approach

How can we make a computer
do something useful?

rules

Data

Answer

Traditional
Approach
(programming)

Training

(Answer)*

Data

Machine
Learning
(Training)

rules

Y=ax+b

A lot, a lot of
• Data ➔ BIG DATA
•

 computation power ➔ DATA CENTER

Two approaches  to make a computer do
something useful (what is the best approach?)

The types of Machine Learning

Training

(Answer)*

Training

Data

rules

Training (minimising error/ reward)
and Data (labelled or not)

1. Supervised

2. Unsupervised

3. Reinforcement learning

Sweet spot

A lot, a lot of
• Data ➔ BIG DATA
•

 computation power ➔ DATA CENTER

supervised

Unsupervised

Reinforcement learning

AI / Machine Learning / Big Data ?

“AI” is a scientific discipline that
deals with the construction and
study of algorithms that can learn
from data. Such Algorithms
operate in 2 steps:

1. building a model based on the

existing data

2. using the model make

predictions and decision
rather that following explicitly
programmed instructions “

Training

Data pre-processing

Is the data ready to be
processed?

• Not always:

• Data not in the correct format:

images, voice, text…

• Dealing with missing values
• Dealing with noise (errors) in the

data values

• Pre-processing

• Feature engineering
• Feature Selection
• …

Training

The AI / Machine Learning WorkFlow

1.

building a model based on the data

2.

using the model make predictions
and decisions rather that following
explicitly programmed instructions “

Model selection

Training
Data

1

Feature
extraction

2

Estimator
Train/fit

3

Test
Data

Feature
extraction

Model
Model

Model
Score

4
Evaluation

underfitting

Linear models

overfitting

non-linear models

Model training
(The AI / Machine Learning WorkFlow)

How to split the input
dataset into: training data
and test data?

Simple Answer ➔  There many ways
•

Simple split (train, test) ➔ (default 75%,
25%) or any proportion

• Threefold split  (train, test, validate)
• Cross-validation:
• Nested  cross-validation, Stratified cross-

validation, TimeSeriesSplit

Threefold split

Cross-validation

The Machine Learning WorkFlow

There are many Machine learning
Algorithms (Models) with different: Model
complexity, computational Complexity,
memory usage,

• Which one to use? ➔ depends on the application

• Basic models

1.

2.

3.

4.

Nearest Neighbours,

Nearest Centroid

Linear Classification and Regression

Logistic Regression

• Non-Linear models

6.

7.

8.

9.

Support Vector Machines and Kernels

Decision Trees

Random Forests

Gradient Boosting

10. Model Calibration

model

fit

Memory

Prediction

centroids

O(n*p)

O(n_classes * p)

O(n_classes * p)

Neighbours

Naïve

Kd_tree O(p*(n * log n))

O(n*p)
O(n*p)

O(n*P)
O(p*(n * log n))

n = n_samples                          p = n_features

Summary of what AI users learns

• The  AI approach:

• rules are generated through

training

• AI is a black box
• Need a lot of Data “Big Data”

•  Pre-process the Data
• Feature engineering

•  Build a Model

• Select/train/validate/deploy a

model

• How to use AI libraries

Enough to build a quickly an AI
model

• No intuition what does it mean to

• generate a dataset
• store/move/process  Big Data:

•  No intuition how basic AI

mechanisms have evolved over the
years and what are the problems
• Backpropagation (chain rule)
• Gradient (vanishing/exploding)
• Word Embedding
• Attention mechanisms
• neural networks “Architectures”
• …

Not enough to reflect and solve the problem
when the AI models don’t work

Intuition is needed when the AI models don’t
work

“Those who own data own the future”
Yuval Noah Harari

• Computer programming

• Knowledge centric (human learning)
• Data centric (machine learning)
• Training (years vs Bytes)

• Big data

• Data movement
• Data processing
• Data storage

• Artificial Intelligence terminology /landscape

• AI origins
• AI milestones (perceptron – DL)
• AI between Hype/fiction/Reality
• Deep Learning
• Problem and Security (hallucination,
• Ethics

To the AI section ➔

The MNIST dataset

50s

60s

70s

80s

90s

00s

10s

20s

Datasets in 90s

Datasets in > 2010

• Handwriting character recognition

NIST

• What Accuracy number do you

trust?

• Need a baseline (calibrated ground

truth)

SD1

SD2

SD19

MNIST EMNIST

90

92

95

98

17

LeCun,  “The MNIST DATABASE”, http://yann.lecun.com/exdb/mnist/ .

A Storage Capacity

YottaByte (YB)  = 1024 Byte
ZetaByte (ZB)  = 1021 Byte
ExaByte  (EB)  = 1018 Byte

PetaByte (PB)   = 1015 Byte

TeraByte (TB)  = 1012 Byte

GigaByte (GB) = 109   Byte

MegaByte (MB) = 106  Byte

KiloByte (KB)  = 103  Byte

capacity

R/W speed

• Storage
• Processing
• Movement

•
  1 TB HDD/~60$ - Storage technology
• 18 TB HDD/~600$ - Storage technology

• 1+ ZB - Internet size in bytes
• Radio astronomy- SKA-Phase  3+ EFlops

Byte = 8 bits

Note: Kilo is exactly 1024 ~ 1000

A Terabyte of Storage
Space: How Many …?

• Storage
• Processing
• Movement

personal usage

➢ ~200,000 average songs, High-Quality Compressed

Audio

       (~17,000 hours of music)

➢ ~256 Standard DVD Movies 120 minutes long
       (~500 hours of movies)

➢~310,000
     Standard-Resolution
     Photos

Note: 1 TB = 1,000 (103) gigabytes (GB) or 1,000,000 (106) megabytes (MB)

Souce: https://aimblog.uoregon.edu/2014/07/08/a-terabyte-of-storage-space-how-much-is-too-much/

• Storage
• Processing
• Movement

Data collected / generated
In Industry and science around 2009

Google processes
Wayback Machine has 3
PB
Facebook has 2.5 PB of
data
eBay has 6.5 PB of user
daa
CERN’s Large Hydron
           Collider -
generates

➔20 PB a day

➔100 TB/month

➔+15 TB/day)

➔50 TB/day

➔ 15 PB/year

Note: 1 TB = 1,000 (103) gigabytes (GB) or 1,000,000 (106)
megabytes (MB)
Souce: https://aimblog.uoregon.edu/2014/07/08/a-terabyte-of-storage-space-how-much-is-too-much/

Has More Bandwidth
Than the Internet—

If you're looking to transfer
hundreds of gigabytes of
data, it's still—weirdly—faster
to ship hard drives via FedEx
than it is to transfer the files
over the internet.

• Storage
• Processing
• Movement

“Cis  estimates that total internet traffic averages 167
terabits per second.

            has a fleet of 654 aircraft with a lift capacity
of 26.5 million pounds daily.

• A solid-state laptop drive weighs about 78 grams

and can hold up to a terabyte.

• FedEx is capable of transferring 150 exabytes of

data per day, or 14 petabits per second—almost a
hundred times the throughput of the internet in
2013.

ByJamie Condliffe PublishedFebruary 5, 2013

Source: http://gizmodo.com/5981713/how-fedex-has-more-bandwidth-than-the-internetand-when-thatll-change
Source: http://gizmodo.com/5981713/how-fedex-has-more-bandwidth-than-the-internetand-when-thatll-change

How much Time does it
take to move TBs over the
internet ?

moving 60 complete human
genomes from Mountain
View - Chicago.

Approximately 18 TB

      on 1G link.

• Storage
• Processing
• Movement

Credit: Robert Grossman University of Chicago Open Data Group, November 14, 2011

Credit: Cees de Laat University of Amsterdam SNE Group, super Computing, 2017

https://delaat.net/sc/sc17/demo02/index.html

• Storage
• Processing
• Movement

Over 10Gbs line

it will take ~ 26 years

How much Time does it
take to move 1 exa-byte
over the internet ?

Note: 1 exa-Byte =

      1,000 (103) petabytes
or   1,000,000 (106) terabytes
or   1,000,000, 000 (109) gigabytes
or   1,000,000, 000, 000 (1012)
                                      megabytes

AWS Snowmobile – Move Exabytes of Data to the Cloud in Weeks | AWS News Blog (amazon.com) 2016

How much time does it take
to process 1 TB?

Estimate:

read 100MB/s, write
100MB/s
no disk seeks, instant sort
341 minutes → 5.6 hours

The terabyte benchmark
winner (2008):

209 seconds (3.48
minutes)
November 2008 (*)
68 seconds

http://sortbenchmark.org/

• Storage
• Processing
• Movement

910 nodes x
(4 dual-core
processors, 4
disks,ry)

(*)https://googleblog.blogspot.com/2008/11/sorting-1pb-with-mapreduce.html

23

Does more CPUs imply
          faster execution times?

• Storage
• Processing
• Movement

• How CPU works http://www.youtube.com/watch?v=cNN_tTXABUA
• Richard Feynman Computer Heuristics Lecture http://www.youtube.com/watch?v=EKWGGDXe5MA

Using more CPUs
imply faster execution
times!

• Speedup
Best

• Superlinear
• Linear
• Sublinear
• Other?

Worst

You must learn Parallel
programming (*)
Or

Using specialized AI libraries
like TensorFlow, PyTorch

(*)Computer Science profile

• Storage
• Processing
• Movement

Linear

Super-Linear

Sub-Linear

5
3

0
3

5
2

0
2

5
1

0
1

5

p
T
/
1
T
=
S
:
p
u
d
e
e
p
S

1      5       10      15     20      25     30     35

Number of CPUs

Credit: Jon Johansson Academic ICT Copyright © 2006
University of Alberta

Do we need always need a
Supercomputer to get some
Speedup?

• Not necessary ➔ Do you have a Game computer?

• Storage
• Processing
• Movement

• Demo: Software the electrostatic properties of biological molecules

• Usage: drug discovery
• Calculation of the boundary value condition (quite slow).
• GPU : EVGA GeForce GTX 285 1GB(~ 400$)
• Programming Language: OpenCL

• Computer programming

• Knowledge centric (human learning)
• Data centric (machine learning)
• Training (years vs Bytes)

• Big data

• Data movement
• Data processing
• Data storage

• Artificial Intelligence terminology /landscape

• AI origins
• AI milestones (perceptron – DL)
• AI between Hype/fiction/Reality
• Deep Learning
• Problem and Security (hallucination,
• Ethics (Black box,
•

The Birth of Artificial; intelligence

50s

60s

70s

80s

90s

00s

10s

20s

explore the potential of Synthetic Intelligence (the term AI hadn't been coined

Vision for AI

yet).

      creation of intelligent machines

     that could reason, learn, and

       communicate like humans

Roadmap for AI research

• programming languages

• algorithms for intelligent machines

AI research labs at universities and

research institutions, MIT, Carnegie Mellon,

and Stanford

Lisp

Computational
linguistic

cognitive
psychology

information
theory

pattern
recognition

theory for nested
rectangular arrays

Birth of Artificial Intelligence

Understanding AI Terminology  landscape

ARTIFICIAL INTELLIGENCE

MACHINE LEARNING

DEEP LEARNING

Rule based systems

Game Playing

Support Vector
Machines

MLP

GAN

LSTM

CNN

RBFN

Gaussian Process
Regression

Linear Regression

Autoencoders

RNN

Random Forest

Logistic regression

Logics K-Mean Clustering

Knowledge Representation and reasoning

Propositional Calculus

Cognitive
modeling

Plannin
g

Search
Algorithm

Understanding AI Terminology  landscape

ARTIFICIAL INTELLIGENCE

MACHINE LEARNING

DEEP LEARNING

Rule based systems

Game Playing

Support Vector
Machines

MLP

GAN

LSTM

CNN

RBFN

Gaussian Process
Regression

Linear Regression

Autoencoders

RNN

Random Forest

Logistic regression

Logics K-Mean Clustering

Knowledge Representation and reasoning

Propositional Calculus

Cognitive
modeling

Plannin
g

Search
Algorithm

Deep Learning:
-
-

vanishing gradient
exploding gradient

output layer

Input layer

hidden layer

Feedforward MSE computed

Backpropagation (gradient is computed)

Fields that benefited  from AI
research

70s

80s

90s

00s

10s

20s

50s

60s

Progress in  algorithms and computing power led to the development of more
sophisticated

       Natural Langauge Processing.                And.                     Computer Vision systems.

Hidden Markov Model

probabilistic modeling of
natural language text

Convolutional Neural
Networks

 accurate object recognition
and image classification

Researchers began to use statistical methods to learn
patterns and features directly from data

Convolutional Neural Networks

50s

60s

70s

80s

90s

00s

10s

20s

LeNet5 by LeCun1998

allowed  more accurate
recognition and image
classification (99%)

• Local receptive Fields
• Weight sharing
• Subsampling
• Convolution layers

LeCun,  “Gradient-Based Learning Applied to Document Recognition”, In Proceedings of the IEEE, Vol. 86,
No. 11, pp. 2278-2324, November 1998 .

The CIFAR-10 /100 dataset

50s

60s

70s

80s

90s

00s

10s

20s

CIFAR-10 /100
(Canadian Institute for Advanced Research)
2009

• The datasets curated to

include a diverse range of
object

• categories commonly found

in everyday scenes,

• making them challenging
yet realistic testbeds for
assessing model
generalization and
robustness

Alex Krizhevsky, Vinod Nair, and Geoffrey Hinton. CIFAR-10 and CIFAR-100 datasets (toronto.edu).

Problem:

limited accuracy: inability to capture spatial hierarchies

and the high dimensionality of image data

The ImageNet challenge

50s

60s

70s

80s

90s

00s

10s

20s

ImageNet challenge – 2010

known as the ImageNet Large
Scale Visual Recognition
Challenge

The competition, held from 2010 to
2017, played a pivotal role in
advancing convolutional neural
networks

Image classification
Object detection/localisation

The evolution of the winning entries on the ImageNet Large
Scale Visual Recognition Challenge from 2010 to 2015. Since
2012, CNNs have outperformed hand-crafted descriptors and
shallow networks by a large margin. Image re-printed with
permission

Olga Russakovsky, et al. “ImageNet Large Scale Visual Recognition Challenge, 2015, International Journal of Computer
Visiondoi:10.1007/s11263-015-0816-y

Reinforcement learning

50s

60s

70s

80s

90s

00s

10s

20s

Deep Q-learning

by  Volodymyr Mnih 2013

Combining RL with deep neural
networks.

• Q-learning

• Agent and environement
• Value function prediction of the
expected cumulative future
rewards

• AlphaGo (2016): Deep RL defeating

human champions in Go.

Volodymyr Mnih et al,  “Playing Atari with Deep Reinforcement Learning”,
https://doi.org/10.48550/arXiv.1312.56022013  .

arXiv:1312.5602

Google DeepMind's Deep Q-learning playing
Atari Breakout!

The encoder-decoder architectures

50s

60s

70s

80s

90s

00s

10s

20s

 The convolutional part of image
classification networks serves as an
excellent feature extractor

• high dimensional inputs into lower

dimensions

• preserving the important features

Beyond classification

  For other applications we need to
transform the resulting features to the
needed output format.

• semantic segmentation
• natural language

processing ,

• speech recognition,

medical image analysis,
and autonomous vehicles

Olaf Ronneberger, Philipp Fischer, and Thomas Brox. "U-Net: Convolutional Networks for Biomedical Image Segmentation." In
Medical Image Computing and Computer-Assisted Intervention (MICCAI), pp. 234-241. Springer, 2015.

Generative AI

Generative AI is a
type of artificial
intelligence that can
create new data, like
text, images, or even
code based on what it
has learned

source: Cyril Hsu

(Answer)*

Data

Training

rules

A lot, a lot of
• Data ➔ BIG DATA
•
 computation
power ➔ DATA
CENTER

D
a
t
a

Audio

Video

Image

Text

Text-to-speech
Music composition
Vocal Remover

Movie trailers
Music videos
Restoration

Concept Art
Editing Photos
Creative materials

Creative writing
Translation
Summarization

Generative Adversarial Networks
(GANs)

70s

80s

90s

00s

10s

20s

50s

60s

New Hardware come to help

Portrait de Edmond Belamy

• GPUs
• TPUs (Tensor Processing Units),

has become standard practice in the
deep learning community for training
and deploying neural networks

Goodfellow et al.
introduced a framework for training
generative models by
simultaneously training two
networks:

a generator network and a
discriminator network, which
compete against each other to
improve the generation of realistic
data.

problem – Training time increased
dramatically

Ian J. Goodfellow, et al. "Generative Adversarial Nets." In Proceedings of the 27th International Conference on Neural
Information Processing Systems (NeurIPS 2014), pp. 2672-2680.

LMs - Language Model

LM is a type of NNs trained to analyze and understand sequences of text. This allows the model to perform
various tasks related to language

Text prediction
Machine translation
Text summarization
Sentiment analysis

your

paper

is

rejected

Embedding
Encoder

[0.1, 1.3]
Adult, Men, Women,
grandparent
[2.1, 4.3]
Child, girl, boy,
infant

[6.2, 1.2]

[0.3, 5.3]

NN

happy
sad
upset
sleepy
cute
…

Transformers -BERT

50s

60s

70s

80s

90s

00s

10s

20s

Transformers by Vaswani et al. 2017

A transformer model --  a neural
network that learns context by
tracking relationships in sequential
data

Attention Mechanism: models
focuses on specific parts of input
features while performing a task

Self-Attention:  model weighs the
importance of different elements in
a sequence relative to each other.

Vaswani et al.  “Attention is All You Need" 2017

Without Attention

WHAT DO YOU MEAN

f(MEAN)

YOU ARE MEAN

f(MEAN)

MEAN ABSOLUTE ERROR
f(MEAN)

Embedding Encoder

[0.1, -1.3, … , 2.13]
same
embedding

Transformers -BERT

50s

60s

70s

80s

90s

00s

10s

20s

Transformers by Vaswani et al. 2017

A transformer model --  a neural
network that learns context by
tracking relationships in sequential
data

Attention Mechanism: models
focuses on specific parts of input
features while performing a task

Self-Attention:  model weighs the
importance of different elements in
a sequence relative to each other.

Vaswani et al.  “Attention is All You Need" 2017

With Attention

WHAT DO YOU MEAN
f(MEAN | WHAT, DO, YOU)

YOU ARE MEAN
f(MEAN | YOU, ARE)

MEAN ABSOLUTE ERROR

f(MEAN | WHAT, DO, YOU)

Embedding Encoder

[0.1, -1.3, … , 2.13]
same
        [1.0,  2.6, … , 5.15]
embedding
        [3.0,  0.6, … , 3.25]

Attention Mechanism  -  explained

50s

60s

70s

80s

90s

00s

10s

20s

Money

in

the

bank

Money

in

the

bank

Positional encoding

Money in
the bank

Money in
the bank

Attention

Post-training
- Q&A data

???

Understanding AI approach

ARTIFICIAL INTELLIGENCE

MACHINE LEARNING

DEEP LEARNING

GenAI

Rule based systems

Game Playing

Support Vector
Machines

MLP

LSTM

GAN

Autoencoders

RBFN

CNN

RNN

Gaussian Process
Regression

Linear Regression

Transformers

LLM

Random Forest

Logistic regression

Logics K-Mean Clustering

Knowledge Representation and reasoning

Propositional Calculus

Cognitive
modeling

Plannin
g

Search
Algorithm

LLMs - (Large) Language Model - Emergence

50s

60s

70s

80s

90s

00s

10s

20s

Training

• LM with vast amount of parameters (e.g., 7B) trained on
massive amounts of text data (570GB ~= 30k times of
Harry Potter series)

• Better performance / Versatility/ Adaptability

• Emergence refers to the unexpected abilities that arise as

models grow in size and complexity

Y=ax+b

Emergent Abilities of Large Language
Models
https://arxiv.org/pdf/2206.07682

LLMs - GPT

• Generative Pre-trained Transformer (GPT)
• Built on the transformer architecture
• Next token prediction

LLMs - GPT to ChatGPT

Foundation

Unsupervised
Pre-training

task-specific

Supervised
Fine-tuning

RLHF (Alignment)

Reward Modeling

Reinforcement
Learning

GPT

ChatGPT

Emergence large language models
(LLMs)

70s

80s

90s

00s

10s

20s

50s

60s

2018

2019

2020

Cimon  - was the first robot sent into space to assist astronauts.
- Open AI paving the way for subsequent LLMs.
GPT
Lovot
- home mini-robot that could sense and affect mood
changes in humans.

Turing Natural Language Generation generative language
model
     (17 billion parameters.)
Deep learning algorithm outperformed radiologists in detecting
potential lung cancers - Google AI and Langone Medical Center's

AI test to identify COVID-19  - The University of Oxford
GPT-3 LLM  - Open AI released (175 billion parameters )
Omniverse   - Nvidia announced a platform to create 3D models.
AlphaFold    - DeepMind's system won the Critical Assessment of
Protein Structure Prediction protein-folding contest.

2021 …

Source : A Comprehensive Overview of Large Language Models (arxiv.org)

x

x

Generative AI

Generative AI is a type of
artificial intelligence that
can create new data, like
text, images, or even
code based on what it
has learned

Image

Concept Art
Editing Photos
Creative materials

source: Cyril Hsu

Generative AI

Generative AI is a type of
artificial intelligence that
can create new data, like
text, images, or even
code based on what it
has learned

Video

Movie trailers
Music videos
Restoration

source: Cyril Hsu

x

Prompt: A stylish woman walks down a Tokyo street filled with warm glowing neon and
animated city signage. She wears a black leather jacket, a long red dress, and black
boots, and carries a black purse…

Generative AI

Generative AI is a type of
artificial intelligence that
can create new data, like
text, images, or even
code based on what it
has learned

LLMs learn the patterns and
styles of human language and
generate different creative text
formats, like poems, code,
scripts, or even news articles.
Given the info on MNS website,
“write a poem about MNS”

A hallucination occurs when LLMs
generate seemingly plausible but
incorrect

Text

Creative writing
Translation
Summarization

source: Cyril Hsu

Networked Souls.mp4

Networked Souls (1).mp4

Generative AI

Generative AI is a type of
artificial intelligence that
can create new data, like
text, images, or even
code based on what it
has learned

Audio

Text-to-speech
Music composition
Vocal Remover

source: Cyril Hsu

Future of LLMs

Terence Tao: ChatGPT will do human-level math research by 2026

Terence Chi-Shen Tao is an
Australian mathematician
who is a professor of
mathematics at the University
of California, Los Angeles
(UCLA), where he holds the
James and Carol Collins chair.

Tao won the Fields Medal in
2006 and won the Royal
Medal and Breakthrough
Prize in Mathematics in 2014,
and is a 2006 MacArthur
Fellow.

• Computer programming

• Knowledge centric (human learning)
• Data centric (machine learning)
• Training (years vs Bytes)

• Big data

• Data movement
• Data processing
• Data storage

• Artificial Intelligence terminology /landscape

• AI origins
• AI milestones (perceptron – DL)
• AI between Hype/fiction/Reality
• Deep Learning
• Problem and Security (hallucination, …)
• Ethics (Black box)
• Prompt Engineering

50s

60s

70s

80s

90s

00s

10s

20s

Threats (LLMs)

Model Safety Prompt
injection (direct/indirect)

• Data Leaking !!!

• model perform tasks
outside its intended

Attacks: Jailbreaking, Virtualization, Sidestepping, Multi-
prompt, Multi-language attack, Role Playing, Model Duping,
Obfuscation (Token Smuggling), Accidental Context Leakage,
Code Injection, Prompt Leaking/Extraction

large language models (LLMs)
Problems

70s

80s

90s

00s

10s

20s

50s

60s

LLMS have are facing
problems

• Hallucinations
• Out of date
• No sources

Case

Context
Process
Content

How can we mitigate
Hallucination?

hallucination

large language models (LLMs)
Problems

70s

80s

90s

00s

10s

20s

50s

60s

LLMS have are facing
problems

Hallucinations
Out of date
No sources

How can we mitigate
Hallucination?

Q: A juggler can juggle 16 balls. Half of the
balls are golf balls, and half of the golf balls
are blue. How many blue golf balls are
there?
A: The answer (arabic numerals) is

(Output) The answer is 8.  (WRONG)

Note: cannot be reproduce with recent AI
LLM chat tool

large language models (LLMs)
Problems

70s

80s

90s

00s

10s

20s

50s

60s

LLMS have are facing
problems

Hallucinations
Out of date
No sources

How can we mitigate
Hallucination?

C o-pilot:  Advanced AI models  like
G P T-4 are des ig ned to handle a
wide rang e of prompts , including
vag ue or mis leading  ones, without
hallucinating .
• C ontext Unders tandings .
• P attern R ecognition.
• P robability-B ased G eneration

It’s  always important to us e thes e
models  res pons ibly and to verify
the information they provide.

large language models (LLMs)
Problems

70s

80s

90s

00s

10s

20s

50s

60s

ChatGPT 3.5

LLMS have are facing
problems

Hallucinations
Out of date
No sources

How can solve this problem?

Emergence large language models
(LLMs)

70s

80s

90s

00s

10s

50s

60s

Co-pilot 3.5

LLMS have are facing
problems

Hallucinations
Out of date
No sources

What is  the difference?

20s

Context
Process
Content

RAG: Retrieval Augmented Generation

50s

60s

70s

80s

90s

00s

10s

20s

Retrieval Augmented
Generation (RAG)
empowers LLM models
with

• dynamic,
• external information
to enhance the
relevance of the
results

Knowledge
base

---
# retrieve
relevant content

---
# User
prompt

----
# Combine them
with user prompt

LLM
---
LLM
output
----
# give
evidence
----

Current Trends-

RAG: Retrieval Augmented Generation

50s

60s

70s

80s

90s

00s

10s

20s

Yixin Hu "Evaluation Pipeline of Query-Answer System Powered by GPT-3.5 and RAG Pipeline ", Sc thesis, Computer Science joint Program UvA-
VU, the Netherlands, July  2024

LlamaIndex Sessions: Evaluating RAG with LlamaIndex (McDermott)
https://youtu.be/44h94AJgQoM?si=BGZCxYYV4le4dDmx

Data Security and privacy

50s

60s

70s

80s

90s

00s

10s

20s

Data anonymization. Is it enough?

No![*,**]

• Linkage attacks

• A priori knowledge attacks

• Composition attacks (e.g.,

second release of k-anonymized
table)

Federated Learning Threat Model

[Local   Model]

[Hospital]

[Local Model]

[Research Center]

FL Threat Model

[Global Model]

[Hospital]

[Local Model]

[Global Model]

AttaAdvers
arial
cks

[End User]

[Local Model]

[*] Narayanan, Arvind, and Vitaly Shmatikov. "How to break anonymity of the netflix prize dataset." arXiv preprint cs/0610105 (2006).
[**] Moselle, Kenneth A., Stan Robertson, and Andriy Koval. "" Real-World" De-Identification of High-Dimensional Transactional Health Datasets." ITCH. 2019.

Federated Learning Threat Model

50s

60s

70s

80s

90s

00s

10s

20s

Data anonymization. Is it enough?

No![*,**]

Linkage attacks

A priori knowledge attacks

Composition attacks (e.g.,
second release of k-
anonymized table)

Output perturbation

Regularization

Differential privacy

Flip
1st

Answer
truthfully

Flip
2nd

yes

no

Apply randomized response (M: Yes, .:
No)

[*] Narayanan, Arvind, and Vitaly Shmatikov. "How to break anonymity of the netflix prize dataset." arXiv preprint cs/0610105 (2006).
[**] Moselle, Kenneth A., Stan Robertson, and Andriy Koval. "" Real-World" De-Identification of High-Dimensional Transactional Health Datasets." ITCH. 2019.

Data Security and privacy

50s

60s

70s

80s

90s

00s

10s

20s

Photo Reconstructed Exploting Non-Privacy
Preserving Machine Learning Model

Original
Photo

Photo Reconstructed Exploting
Different Privacy Preserving
Machine Learning Model

Privacy Preservation

Definition: Providing record level
protection to every member of
the training set while gaining
useful insights about the
populations as a whole

What is not private?

Data

Communication

Infrastructure

Machine learning model output

Singh, Abhishek, et al. "DISCO: Dynamic and Invariant Sensitive Channel
Obfuscation for deep neural networks." arXiv preprint arXiv:2012.11025 (2020)

Explainable AI

50s

60s

70s

80s

90s

00s

10s

20s

An example of an adversarial
attack

RISE algorithm

Willem van der Spek " Technical Challenges and Opportunities in Explainable Artificial Intelligence", Sc thesis, Computer Sci ence joint
Program UvA-VU, the Netherlands, September 2023.

Future of LLMs

• LLMs vs Agentic LLMs

• Traditional LLMs: Chatbots, text generation, language translation, creative writing,

QA

• Agentic LLMs: Access and process information from the real world through external

tools, and use this information to make decisions and complete tasks

• Stanford created a virtual world full of ChatGPT-powered people

• The simulation ran for 2 days and showed that LLM-powered bots interact in a

human-like way

• The bots planned a party, coordinated the event, and attended the party within the

simulation

• Computer programming

• Knowledge centric (human learning)
• Data centric (machine learning)
• Training (years vs Bytes)

• Big data

• Data movement
• Data processing
• Data storage

• Artificial Intelligence terminology /landscape

• AI origins
• AI milestones (perceptron – DL)
• AI between Hype/fiction/Reality
• Deep Learning
• Problem and Security (hallucination, …)
• Ethics (Black box)
• Prompt Engineering

Source:  google trends

One way interacting
with LLMs, its
simplicity with no
need to fine-tune the
model.

Prompt engineering
is the practice of
developing and
optimizing prompts to
efficiently use language
models (LMs) for a
variety of applications

[1] 2312.16171.pdf (arxiv.org)

Text Summarization
•
• Question Answering
Text Classification
•
• Role Playing
• Code Generation

• Reasoning

•
Few-shots
• Chain-of-thought

•

•

Zero-shot Prompt

Problem: self-
consistency

Basic Tasks

Advanced  Tasks

50s

60s

70s

80s

90s

00s

10s

20s

End.

