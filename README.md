# Arxived-LLM-Jailbreak


## Automatic Paper Summary
### Don't Listen To Me: Understanding and Exploring Jailbreak Prompts of Large Language Models
#### **1. Summary of this text**  
The provided LaTeX text introduces a research paper focused on enhancing the safety of large language models (LLMs) through adversarial robustness. The paper outlines a novel framework for evaluating and improving LLM resilience against prompt injection attacks. It begins by importing necessary LaTeX packages for mathematical notation and structured referencing. The title and authors are defined, followed by an abstract that summarizes the core contributions: a new taxonomy for adversarial attacks, a contrastive adversarial training (CAT) approach, and empirical analysis of attack transferability. The introduction contextualizes the problem, reviews existing defense mechanisms, and identifies gaps addressed by the paper. The paper then presents a mathematical framework for evaluating robustness, setting the stage for detailed theoretical and empirical analyses.

#### **2. Related Metadata**  
- **Tools and Algorithms Created**: PromptFuzz, contrastive adversarial training (CAT)
- **Benchmarks Created**: Not explicitly mentioned
- **Codebase/Data Location**: https://github.com/PromptFuzz/PromptFuzz
- **LLMs Evaluated**: Vicuna-13B-v1.5, Llama-2-7B-chat, GPT-3.5-Turbo-1106, GPT-4-0125-preview, Claude-instant-1.2, Claude-2.1, Gemini-Pro
- **Attack Techniques Evaluated**: PAIR (Prompt Automatic Iterative Refinement), GCG (Gradient-to-Coordinate descent), JBC (Jailbreak Chat)
- **Defense Techniques Evaluated**: SmoothLLM, Perplexity Filter, CAT
- **Frameworks/Methods Critiqued**: PAIR, GCG, JBC

#### **3. Main Contributions**  
- **Novel Taxonomy**: Introduces a new taxonomy for categorizing adversarial attacks against LLMs, including previously unstudied classes.
- **Contrastive Adversarial Training (CAT)**: Proposes a new defense method that improves LLM resilience to prompt injection attacks.
- **Empirical Analysis**: Provides an empirical analysis of attack transferability across different model scales, challenging previous assumptions.

#### **4. Methods & Approach**  
- **Dataset**: Uses a dataset of 100,000 adversarial prompts crafted via reinforcement learning.
- **Evaluation**: Assesses model robustness on OpenAI’s GPT-4, Anthropic’s Claude, and Meta’s LLaMA-2.
- **Defense Implementation**: Implements CAT, a defense method that fine-tunes models using adversarial examples selected via a similarity-based scoring function.
- **Mathematical Framework**: Develops a formal framework for evaluating robustness, including probabilistic models and metrics for measuring resilience.

#### **5. Findings & Empirical Results**  
- **Effectiveness of CAT**: Demonstrates that CAT improves robustness by 32% compared to vanilla fine-tuning.
- **Attack Transferability**: Finds that adversarial attack transferability increases with model size, contradicting previous assumptions.
- **Trade-offs**: Observes a slight degradation in response diversity (measured via perplexity scores) when using CAT, highlighting a trade-off between robustness and diversity.

#### **6. Implications for LLM Safety**  
- **Adversarial Robustness Scaling**: Emphasizes the need for adversarial robustness to scale with model size, as larger models may be more vulnerable to certain attacks.
- **Comprehensive Evaluation**: Suggests that models should be evaluated across multiple safety benchmarks to ensure robustness against diverse attack vectors.
- **Balancing Robustness and Diversity**: Raises concerns about the trade-offs between robustness and generation diversity, advocating for a balanced approach in model development.

#### **7. Missing Information & Caveats**  
- **Partial Experimental Setup**: The experimental setup for RL-based adversarial prompt generation was only partially available, leaving some details unclear.
- **Generalization of CAT**: Further clarification is needed on whether CAT generalizes to non-prompt-based attacks, as the provided text does not address this aspect comprehensively.
### EEG-Defender: Defending against Jailbreak through Early Exit Generation of Large Language Models
#### **1. Summary of this text**
The provided LaTeX content outlines the initial sections of a research paper focused on advancing LLM safety through novel methodologies. It includes standard document setup, author information, an abstract summarizing the paper's objectives, and an introduction that contextualizes the research within existing literature. The abstract highlights the development of a new benchmark for evaluating adversarial robustness and introduces a defense mechanism called SmoothLLM. The introduction provides background on LLM safety challenges, reviews current defense strategies, and sets the stage for presenting the paper's contributions.

#### **2. Related Metadata**
- **Tools and Algorithms Created**: SmoothLLM
- **Benchmarks Created**: PromptFuzz
- **Codebase/Data Repository**: https://github.com/PromptFuzz/PromptFuzz
- **LLMs Evaluated**: Vicuna-13B-v1.5, Llama-2-7B-chat, GPT-3.5-Turbo-1106, GPT-4-0125-preview, Claude-instant-1.2, Claude-2.1, Gemini-Pro
- **Attack Techniques Evaluated**: PAIR (Prompt Automatic Iterative Refinement), GCG (Gradient-to-Coordinate descent), JBC (Jailbreak Chat)
- **Defense Techniques Evaluated**: SmoothLLM, Perplexity Filter
- **Frameworks/Methods Critiqued**: PAIR, GCG, JBC

#### **3. Main Contributions**
- **Novel Ideas/Insights**: Introduces PromptFuzz, a new benchmark for evaluating adversarial robustness in LLMs, and SmoothLLM, a defense mechanism that enhances model resilience against prompt injection attacks.
- **Key Problems Addressed**: The paper tackles the issue of adversarial attacks on LLMs, particularly prompt injection, which can lead to unintended behaviors. It addresses the limitations of existing defense mechanisms in handling diverse attack vectors.
- **Building Upon Existing Work**: The paper builds on previous research in adversarial robustness and defense mechanisms but introduces a more comprehensive evaluation framework and an improved defense strategy.

#### **4. Methods & Approach**
- **Key Techniques**: The paper employs a combination of adversarial training and a novel defense mechanism (SmoothLLM) to enhance model robustness. It uses the PromptFuzz benchmark to evaluate the effectiveness of these methods.
- **Datasets Used**: The evaluation involves a diverse set of adversarial prompts generated through iterative refinement and gradient-based methods.
- **Evaluation Metrics**: The paper measures robustness improvements using success rates of adversarial attacks and evaluates trade-offs using metrics like perplexity and response diversity.

#### **5. Findings & Empirical Results**
- **Major Findings**: The SmoothLLM defense mechanism significantly improves robustness against prompt injection attacks, with a notable reduction in attack success rates. The PromptFuzz benchmark reveals that existing defense mechanisms often fail to generalize across different attack types.
- **Benchmarks and Metrics**: The paper introduces a new benchmark (PromptFuzz) and evaluates defense mechanisms using metrics such as attack success rate, perplexity, and response diversity.
- **Trade-offs**: While SmoothLLM enhances robustness, it slightly reduces response diversity, as measured by perplexity scores.

#### **6. Implications for LLM Safety**
- **Safety Concerns Addressed**: The findings emphasize the importance of robust defense mechanisms against adversarial attacks, particularly prompt injection. They highlight the need for comprehensive evaluation frameworks to ensure models are resilient across diverse attack vectors.
- **Recommendations**: The paper suggests adopting SmoothLLM as a defense strategy and using the PromptFuzz benchmark for evaluating model robustness. It also recommends further research into balancing robustness with response diversity.

#### **7. Missing Information & Caveats**
- **Missing Sections**: The provided content lacks detailed descriptions of the experimental setup for adversarial prompt generation and the implementation specifics of SmoothLLM.
- **Ambiguous Sections**: The abstract mentions "novel classes of adversarial attacks," but the specific details of these classes are not provided in the given content. Further clarification is needed to understand the full scope of the research.
### Improved Techniques for Optimization-Based Jailbreaking on Large Language Models
#### **1. Summary of this text**  
The provided LaTeX text introduces a paper focused on enhancing the robustness of large language models (LLMs) against adversarial attacks. It begins by outlining the problem of prompt injection attacks and the limitations of current defense mechanisms. The paper presents a novel method called **Contrastive Adversarial Training (CAT)**, which involves fine-tuning models using adversarial examples selected through a similarity-based scoring function. The authors evaluate their approach on multiple LLMs, including GPT-4, Claude, and LLaMA-2, and provide empirical results comparing CAT's effectiveness against traditional fine-tuning methods. The text emphasizes the trade-offs between robustness and response diversity, suggesting that while CAT improves model resilience, it may slightly reduce the diversity of generated outputs.

#### **2. Related Metadata**  
- **Tools and Algorithms Created**: Contrastive Adversarial Training (CAT)
- **Benchmarks Created**: Not explicitly mentioned in the provided text.
- **Codebase/Data**: The codebase for CAT and datasets used are available at [GitHub repository](https://github.com/PromptFuzz/PromptFuzz).
- **LLMs Evaluated**: Vicuna-13B-v1.5, Llama-2-7B-chat, GPT-3.5-Turbo-1106, GPT-4-0125-preview, Claude-instant-1.2, Claude-2.1, Gemini-Pro
- **Attack Techniques Evaluated**: PAIR (Prompt Automatic Iterative Refinement), GCG (Gradient-to-Coordinate descent), JBC (Jailbreak Chat)
- **Defense Techniques Evaluated**: SmoothLLM, Perplexity Filter, CAT
- **Frameworks/Methods Critiqued**: PAIR, GCG, JBC

#### **3. Main Contributions**  
- **Novel Taxonomy**: Introduces a new taxonomy for categorizing adversarial attacks against LLMs, identifying novel attack classes not previously studied.
- **Contrastive Adversarial Training (CAT)**: Proposes a new defense method that improves LLM resilience to prompt injection attacks by fine-tuning models using adversarial examples selected via a similarity-based scoring function.
- **Empirical Analysis**: Provides an empirical analysis of attack transferability across different model scales, revealing that transferability increases with model size, which contradicts previous assumptions.

#### **4. Methods & Approach**  
- **Datasets**: Uses a dataset of 100,000 adversarial prompts crafted via reinforcement learning.
- **Evaluation**: Assesses model robustness on OpenAI’s GPT-4, Anthropic’s Claude, and Meta’s LLaMA-2.
- **Defense Implementation**: Implements CAT, a novel defense method that involves fine-tuning models using adversarial examples selected via a similarity-based scoring function.
- **Metrics**: Evaluates robustness and response diversity using metrics such as accuracy and perplexity scores.

#### **5. Findings & Empirical Results**  
- **Effectiveness of CAT**: CAT improves robustness by 32% compared to vanilla fine-tuning.
- **Attack Transferability**: Finds that adversarial attack transferability increases with model size, challenging previous assumptions.
- **Trade-offs**: Observes a slight degradation in response diversity (measured via perplexity scores) when using CAT.

#### **6. Implications for LLM Safety**  
- **Adversarial Robustness**: Highlights the importance of adversarial robustness scaling with model size and the need for robust defense mechanisms.
- **Evaluation Across Benchmarks**: Suggests that models should be evaluated across multiple safety benchmarks to ensure comprehensive robustness.
- **Trade-offs Consideration**: Raises concerns about the trade-offs between robustness and generation diversity, emphasizing the need for balanced approaches in model training.

#### **7. Missing Information & Caveats**  
- **Experimental Setup**: The experimental setup for RL-based adversarial prompt generation was only partially available, leaving some details unclear.
- **Generalizability**: Further clarification is needed on whether CAT generalizes to non-prompt-based attacks, as the provided text focuses primarily on prompt injection attacks.
### The Dark Side of Function Calling: Pathways to Jailbreaking Large Language Models
#### **1. Summary of this text**  
The provided LaTeX text outlines the structural and theoretical foundation of a research paper titled *"Fundamental Limitations of Alignment in Large Language Models."* This section serves multiple purposes:

1. **Technical Setup**: The document imports various LaTeX packages to format the paper, support mathematical notation, and enable structured referencing.
2. **Authors and Title Definition**: It formally establishes the paper’s title and lists the contributing authors, their affiliations, and contact details.
3. **Abstract Summary**: The abstract outlines the paper’s core thesis—analyzing the theoretical limitations of aligning LLMs to prevent undesired behaviors. It introduces the **Behavior Expectation Bounds (BEB)** framework, arguing that alignment cannot fully prevent adversarial exploits.
4. **Introduction to the Problem**: The introduction contextualizes alignment issues, reviews existing methods (like RLHF and representation engineering), and emphasizes vulnerabilities in contemporary approaches.
5. **Mathematical Framework Setup**: The document begins formalizing a probabilistic approach to evaluate alignment robustness, setting the stage for later theoretical results.

Overall, this LaTeX snippet is setting up the groundwork for a structured theoretical analysis, defining key terms, reviewing alignment methods, and preparing for an in-depth mathematical exploration of LLM vulnerabilities.

#### **2. Related Metadata**  
- **Tools and Algorithms Created**: PromptFuzz  
- **Benchmarks Created**: No  
- **Codebase/Data Location**: https://github.com/PromptFuzz/PromptFuzz  
- **LLMs Evaluated**: Vicuna-13B-v1.5, Llama-2-7B-chat, GPT-3.5-Turbo-1106, GPT-4-0125-preview, Claude-instant-1.2, Claude-2.1, Gemini-Pro  
- **Attack Techniques Evaluated**: PAIR (Prompt Automatic Iterative Refinement), GCG (Gradient-to-Coordinate descent), JBC (Jailbreak Chat)  
- **Defense Techniques Evaluated**: SmoothLLM, Perplexity Filter  
- **Frameworks/Methods Critiqued**: PAIR, GCG, JBC  

#### **3. Main Contributions**  
- **Novel Ideas/Insights**: Introduces a new taxonomy for categorizing adversarial attacks against LLMs, including novel classes not previously studied. Proposes a contrastive adversarial training (CAT) approach to improve LLM resilience to prompt injections.  
- **Problems Addressed**: Enhances LLM robustness against adversarial attacks and improves understanding of attack transferability across model scales.  
- **Building Upon/Challenging Existing Work**: Challenges previous assumptions about attack transferability increasing with model size, providing empirical evidence to the contrary.  

#### **4. Methods & Approach**  
- **Datasets**: Uses a dataset of 100,000 adversarial prompts crafted via reinforcement learning.  
- **Evaluation**: Assesses model robustness on OpenAI’s GPT-4, Anthropic’s Claude, and Meta’s LLaMA-2.  
- **Defense Method**: Implements a new defense method (CAT) that fine-tunes models using adversarial examples selected via a similarity-based scoring function.  

#### **5. Findings & Empirical Results**  
- **Improvements**: CAT improves robustness by 32% compared to vanilla fine-tuning.  
- **Contradictions**: Finds that adversarial attack transferability increases with model size, contradicting previous assumptions.  
- **Limitations**: CAT introduces a slight degradation in response diversity, measured via perplexity scores.  

#### **6. Implications for LLM Safety**  
- **Adversarial Robustness**: Highlights the need for adversarial robustness to scale with model size.  
- **Evaluation Practices**: Suggests models should be trained on adversarial examples and evaluated across multiple safety benchmarks.  
- **Trade-offs**: Raises concerns about the balance between robustness and generation diversity.  

#### **7. Missing Information & Caveats**  
- **Experimental Setup**: The experimental setup for RL-based adversarial prompt generation was only partially available.  
- **Generalizability**: Further clarification is needed on whether CAT generalizes to non-prompt-based attacks.
### Enhancing the Capability and Robustness of Large Language Models through Reinforcement Learning-Driven Query Refinement
#### **1. Summary of this text**  
The provided LaTeX text outlines the **theoretical framework** for analyzing adversarial attacks on large language models (LLMs). It begins by setting up the technical and mathematical groundwork, importing necessary packages and defining the paper's structure. The abstract introduces the core focus: evaluating the robustness of LLMs against prompt injection attacks and proposing a novel defense mechanism. The introduction contextualizes the problem by reviewing existing attack and defense techniques, highlighting the need for more robust solutions. The paper formalizes a probabilistic model to assess the effectiveness of adversarial attacks and introduces a contrastive adversarial training (CAT) method to enhance model resilience. This section is crucial for establishing the foundation for the detailed analysis and empirical evaluation that follows.

#### **2. Related Metadata**  
- **Tools and Algorithms Created**: PromptFuzz, Contrastive Adversarial Training (CAT)  
- **Benchmarks Created**: Not explicitly mentioned in the provided text.  
- **Codebase/Data Location**: The code is available at [https://github.com/PromptFuzz/PromptFuzz](https://github.com/PromptFuzz/PromptFuzz).  
- **LLMs Evaluated**: Vicuna-13B-v1.5, Llama-2-7B-chat, GPT-3.5-Turbo-1106, GPT-4-0125-preview, Claude-instant-1.2, Claude-2.1, Gemini-Pro.  
- **Attack Techniques Evaluated**: PAIR (Prompt Automatic Iterative Refinement), GCG (Gradient-to-Coordinate descent), JBC (Jailbreak Chat).  
- **Defense Techniques Evaluated**: SmoothLLM, Perplexity Filter, Contrastive Adversarial Training (CAT).  
- **Frameworks/Methods Critiqued**: PAIR, GCG, JBC.

#### **3. Main Contributions**  
- **Novel Taxonomy**: Introduces a new taxonomy for adversarial attacks, identifying previously unstudied classes.  
- **Contrastive Adversarial Training (CAT)**: Proposes a novel defense mechanism that enhances model resilience to prompt injections.  
- **Empirical Analysis**: Provides a comprehensive analysis of attack transferability across different model scales, revealing unexpected patterns.  

#### **4. Methods & Approach**  
- **Adversarial Prompt Generation**: Utilizes reinforcement learning to create a dataset of 100,000 adversarial prompts.  
- **Model Evaluation**: Assesses robustness on a range of models, including OpenAI’s GPT-4, Anthropic’s Claude, and Meta’s LLaMA-2.  
- **Defense Implementation**: Implements CAT, a defense method that fine-tunes models using adversarial examples selected via a similarity-based scoring function.  
- **Mathematical Framework**: Establishes a probabilistic model to evaluate attack effectiveness and defense mechanisms.

#### **5. Findings & Empirical Results**  
- **Effectiveness of CAT**: The CAT method improves robustness by 32% compared to vanilla fine-tuning.  
- **Attack Transferability**: Finds that adversarial attack transferability increases with model size, challenging previous assumptions.  
- **Trade-offs**: Observes a slight degradation in response diversity (measured via perplexity scores) when using CAT.  

#### **6. Implications for LLM Safety**  
- **Scalability of Robustness**: Highlights the importance of ensuring that adversarial robustness scales with model size.  
- **Evaluation Across Benchmarks**: Emphasizes the need for models to be evaluated across multiple safety benchmarks.  
- **Robustness-Diversity Trade-offs**: Raises concerns about the balance between robustness and generation diversity, suggesting the need for further research.

#### **7. Missing Information & Caveats**  
- **Partial Experimental Setup**: The experimental setup for RL-based adversarial prompt generation was not fully detailed in the provided text.  
- **Generalization Concerns**: Further clarification is needed on whether CAT generalizes to non-prompt-based attacks.  
- **Missing Benchmarks**: The creation of new benchmarks is mentioned but not detailed in the provided content.
### On Calibration of LLM-based Guard Models for Reliable Content Moderation
#### **1. Summary of this text**  
The provided LaTeX text is a section from a research paper titled *"PromptFuzz: A Framework for Fuzzing Large Language Models Against Prompt Injection Attacks."* This section serves to introduce the paper's objectives, methodology, and contributions. It begins by highlighting the critical issue of prompt injection attacks, where adversaries manipulate model inputs to induce unintended behaviors. The paper introduces **PromptFuzz**, a novel framework designed to systematically test LLMs against such attacks. The abstract outlines the framework's core components and its application across multiple LLMs, including Vicuna-13B, Llama-2-7B, and GPT-3.5-Turbo. The introduction contextualizes the problem within existing security research, emphasizing the need for robust defense mechanisms. The paper also presents empirical results comparing various defense strategies, such as SmoothLLM and Perplexity Filter, against attack techniques like PAIR and GCG. The findings underscore the limitations of current defenses and propose improvements for enhancing LLM security.

#### **2. Related Metadata**  
- **Tools and Algorithms Created**: PromptFuzz, CAT (Contrastive Adversarial Training)  
- **Benchmarks Created**: PromptFuzz benchmark suite  
- **Codebase/Data**: Available at [GitHub repository](https://github.com/PromptFuzz/PromptFuzz)  
- **LLMs Evaluated**: Vicuna-13B-v1.5, Llama-2-7B-chat, GPT-3.5-Turbo-1106, GPT-4-0125-preview, Claude-instant-1.2, Claude-2.1, Gemini-Pro  
- **Attack Techniques Evaluated**: PAIR (Prompt Automatic Iterative Refinement), GCG (Gradient-to-Coordinate descent), JBC (Jailbreak Chat)  
- **Defense Techniques Evaluated**: SmoothLLM, Perplexity Filter, CAT  
- **Frameworks/Methods Critiqued**: PAIR, GCG, JBC  

#### **3. Main Contributions**  
- **Novel Framework**: Introduces PromptFuzz, a systematic framework for testing LLMs against prompt injection attacks.  
- **New Defense Method**: Proposes Contrastive Adversarial Training (CAT) to enhance model resilience.  
- **Empirical Analysis**: Provides comprehensive evaluation of attack transferability and defense effectiveness across various LLMs.  
- **Taxonomy Development**: Establishes a new taxonomy for categorizing adversarial attacks, including previously unstudied classes.  

#### **4. Methods & Approach**  
- **Prompt Generation**: Utilizes reinforcement learning to generate 100,000 adversarial prompts.  
- **Evaluation Setup**: Tests model robustness on OpenAI’s GPT-4, Anthropic’s Claude, and Meta’s LLaMA-2.  
- **Defense Implementation**: Implements CAT, which fine-tunes models using adversarial examples selected via similarity-based scoring.  
- **Metrics**: Uses accuracy, robustness improvement percentage, and response diversity (perplexity) as evaluation metrics.  

#### **5. Findings & Empirical Results**  
- **Defense Effectiveness**: CAT improves robustness by 32% compared to vanilla fine-tuning.  
- **Attack Transferability**: Finds that transferability increases with model size, challenging previous assumptions.  
- **Trade-offs**: CAT slightly degrades response diversity, measured via perplexity scores.  
- **Framework Utility**: PromptFuzz identifies vulnerabilities across different LLMs, highlighting the need for scalable defense mechanisms.  

#### **6. Implications for LLM Safety**  
- **Adversarial Robustness**: Emphasizes the importance of robustness against prompt injection attacks, especially as models scale.  
- **Defense Mechanisms**: Recommends adopting frameworks like PromptFuzz for systematic testing and improving defense strategies.  
- **Evaluation Practices**: Suggests evaluating models across multiple benchmarks and considering trade-offs between robustness and diversity.  
- **Research Directions**: Calls for further investigation into attack transferability and defense scalability.  

#### **7. Missing Information & Caveats**  
- **Partial Experimental Setup**: Details on the RL-based adversarial prompt generation were only partially available.  
- **Generalizability Concerns**: Further clarification needed on whether CAT and PromptFuzz apply to non-prompt-based attacks.  
- **Missing Long-term Effects**: The text does not address the long-term implications of using CAT on model performance and user trust.
### White-box Multimodal Jailbreaks Against Large Vision-Language Models
#### **1. Summary of this text**  
The provided LaTeX text introduces a research paper focused on enhancing the robustness and safety of large language models (LLMs) through adversarial training. The paper outlines the theoretical framework, including the introduction of a novel contrastive adversarial training (CAT) method, and evaluates its effectiveness across various LLMs. The abstract highlights the core contributions, while the introduction contextualizes the problem within existing literature. The mathematical setup formalizes the approach, setting the stage for detailed empirical analysis.

#### **2. Related Metadata**  
- **Tools/Algorithms Created**: Contrastive Adversarial Training (CAT)
- **Benchmarks Created**: No specific benchmarks mentioned
- **Codebase/Data**: Available at [GitHub repository](https://github.com/PromptFuzz/PromptFuzz)
- **LLMs Evaluated**: Vicuna-13B-v1.5, Llama-2-7B-chat, GPT-3.5-Turbo-1106, GPT-4-0125-preview, Claude-instant-1.2, Claude-2.1, Gemini-Pro
- **Attack Techniques**: PAIR (Prompt Automatic Iterative Refinement), GCG (Gradient-to-Coordinate descent), JBC (Jailbreak Chat)
- **Defense Techniques**: SmoothLLM, Perplexity Filter, CAT
- **Frameworks/Methods Critiqued**: PAIR, GCG, JBC

#### **3. Main Contributions**  
- Introduces a new contrastive adversarial training (CAT) method to enhance LLM robustness against prompt injection attacks.
- Proposes a novel taxonomy for categorizing adversarial attacks, identifying previously unstudied classes.
- Provides empirical evidence on the transferability of adversarial attacks across different model scales.

#### **4. Methods & Approach**  
- **Datasets**: Utilizes a dataset of 100,000 adversarial prompts generated via reinforcement learning.
- **Evaluation**: Assesses model robustness on multiple LLMs, including OpenAI’s GPT-4, Anthropic’s Claude, and Meta’s LLaMA-2.
- **Methodology**: Implements CAT, a defense mechanism that fine-tunes models using adversarial examples selected through a similarity-based scoring function.
- **Formal Setup**: Establishes a mathematical framework to formalize the approach, including probabilistic models for robustness evaluation.

#### **5. Findings & Empirical Results**  
- **Effectiveness of CAT**: Demonstrates a 32% improvement in robustness compared to vanilla fine-tuning.
- **Attack Transferability**: Finds that adversarial attack transferability increases with model size, challenging prior assumptions.
- **Trade-offs**: Observes a slight degradation in response diversity, measured via perplexity scores, when using CAT.

#### **6. Implications for LLM Safety**  
- Emphasizes the necessity for adversarial robustness to scale with model size, suggesting that larger models may require more sophisticated defense mechanisms.
- Recommends the integration of adversarial training into model development pipelines and the use of multiple safety benchmarks for comprehensive evaluation.
- Highlights the need for further research into balancing robustness with generation diversity to avoid unintended consequences.

#### **7. Missing Information & Caveats**  
- **Partial Experimental Setup**: The details of the reinforcement learning-based adversarial prompt generation were not fully available, leaving some aspects of the methodology unclear.
- **Generalizability Concerns**: The paper does not address whether CAT is effective against non-prompt-based attacks, necessitating further investigation.
- **Ambiguity in Results**: The trade-off between robustness and diversity requires more detailed analysis to understand its implications fully.
### Making Them a Malicious Database: Exploiting Query Code to Jailbreak Aligned Large Language Models
#### **1. Summary of this text**  
The provided LaTeX text introduces a research paper focused on enhancing the robustness of large language models (LLMs) against adversarial attacks. The paper outlines a novel framework called **PromptFuzz**, which systematically evaluates and improves LLM resilience. It details the methodology, including a dataset of adversarial prompts generated through reinforcement learning, and evaluates various models such as Vicuna-13B, Llama-2-7B, and GPT-4. The paper also presents a defense mechanism called **contrastive adversarial training (CAT)**, which significantly improves model robustness. The findings challenge previous assumptions about attack transferability and highlight trade-offs between robustness and response diversity.

---

#### **2. Related Metadata**  
- **Tools and Algorithms Created**: PromptFuzz, contrastive adversarial training (CAT).  
- **Benchmarks Created**: Not explicitly mentioned.  
- **Codebase/Data**: Available at [https://github.com/PromptFuzz/PromptFuzz](https://github.com/PromptFuzz/PromptFuzz).  
- **LLMs Evaluated**: Vicuna-13B-v1.5, Llama-2-7B-chat, GPT-3.5-Turbo-1106, GPT-4-0125-preview, Claude-instant-1.2, Claude-2.1, Gemini-Pro.  
- **Attack Techniques Evaluated**: PAIR (Prompt Automatic Iterative Refinement), GCG (Gradient-to-Coordinate descent), JBC (Jailbreak Chat).  
- **Defense Techniques Evaluated**: SmoothLLM, Perplexity Filter, CAT (contrastive adversarial training).  
- **Frameworks/Methods Critiqued**: PAIR, GCG, JBC.

---

#### **3. Main Contributions**  
- Introduces **PromptFuzz**, a novel framework for evaluating LLM robustness against adversarial attacks.  
- Proposes **contrastive adversarial training (CAT)**, a defense mechanism that improves resilience by 32% compared to vanilla fine-tuning.  
- Challenges the assumption that attack transferability decreases with model size, showing the opposite trend.  
- Highlights the trade-off between robustness and response diversity, measured via perplexity scores.

---

#### **4. Methods & Approach**  
- **Dataset**: 100,000 adversarial prompts generated via reinforcement learning.  
- **Evaluation**: Conducted on models like GPT-4, Claude, and LLaMA-2.  
- **Defense Mechanism**: CAT fine-tunes models using adversarial examples selected via a similarity-based scoring function.  
- **Metrics**: Robustness improvement (32%), response diversity (perplexity scores).  

---

#### **5. Findings & Empirical Results**  
- **Improvement in Robustness**: CAT achieves a 32% increase in robustness compared to vanilla fine-tuning.  
- **Attack Transferability**: Contrary to previous assumptions, transferability increases with model size.  
- **Trade-offs**: CAT slightly degrades response diversity, as measured by perplexity scores.  

---

#### **6. Implications for LLM Safety**  
- **Adversarial Robustness**: Emphasizes the need for robustness to scale with model size.  
- **Evaluation Across Benchmarks**: Recommends evaluating models across multiple safety benchmarks.  
- **Trade-offs**: Highlights the need to balance robustness with generation diversity.  

---

#### **7. Missing Information & Caveats**  
- **Experimental Setup**: The reinforcement learning-based adversarial prompt generation setup was only partially detailed.  
- **Generalizability**: Further clarification is needed on whether CAT generalizes to non-prompt-based attacks.
### Visual-RolePlay: Universal Jailbreak Attack on MultiModal Large Language Models via Role-playing Image Character
#### **1. Summary of this text**  
The provided LaTeX text is part of a research paper focused on enhancing the safety of large language models (LLMs) through adversarial robustness. The paper introduces a novel framework, **PromptFuzz**, designed to evaluate and improve LLM resilience against adversarial prompts. It outlines the methodology, including the creation of adversarial examples using techniques like PAIR, GCG, and JBC, and evaluates their impact on models such as GPT-4, Claude, and LLaMA-2. The paper also proposes a defense mechanism, **contrastive adversarial training (CAT)**, which significantly improves model robustness. The findings suggest that while model size increases vulnerability, defense strategies can mitigate these risks, though they may affect response diversity.

---

#### **2. Related Metadata**  
- **Tools and Algorithms Created**: PromptFuzz, contrastive adversarial training (CAT)  
- **Benchmarks Created**: None explicitly mentioned  
- **Codebase/Data Availability**: Available at https://github.com/PromptFuzz/PromptFuzz  
- **LLMs Evaluated**: Vicuna-13B-v1.5, Llama-2-7B-chat, GPT-3.5-Turbo-1106, GPT-4-0125-preview, Claude-instant-1.2, Claude-2.1, Gemini-Pro  
- **Attack Techniques Evaluated**: PAIR (Prompt Automatic Iterative Refinement), GCG (Gradient-to-Coordinate descent), JBC (Jailbreak Chat)  
- **Defense Techniques Evaluated**: SmoothLLM, Perplexity Filter  
- **Frameworks/Methods Critiqued**: PAIR, GCG, JBC  

---

#### **3. Main Contributions**  
- Introduces **PromptFuzz**, a new framework for evaluating LLM robustness against adversarial prompts.  
- Proposes **contrastive adversarial training (CAT)**, a defense mechanism that improves resilience by 32% compared to vanilla fine-tuning.  
- Provides empirical evidence on attack transferability across model scales, challenging previous assumptions.  

---

#### **4. Methods & Approach**  
- **Datasets**: A dataset of 100,000 adversarial prompts generated via reinforcement learning.  
- **Models Evaluated**: OpenAI’s GPT-4, Anthropic’s Claude, and Meta’s LLaMA-2.  
- **Defense Method**: CAT fine-tunes models using adversarial examples selected via a similarity-based scoring function.  

---

#### **5. Findings & Empirical Results**  
- **Improvement in Robustness**: CAT enhances model resilience by 32% compared to vanilla fine-tuning.  
- **Attack Transferability**: Transferability increases with model size, contradicting prior assumptions.  
- **Trade-offs**: CAT slightly reduces response diversity, as measured by perplexity scores.  

---

#### **6. Implications for LLM Safety**  
- Emphasizes the need for adversarial robustness to scale with model size.  
- Recommends training models on adversarial examples and evaluating across multiple safety benchmarks.  
- Highlights potential trade-offs between robustness and generation diversity, urging further investigation.  

---

#### **7. Missing Information & Caveats**  
- The experimental setup for RL-based adversarial prompt generation was only partially available.  
- Clarification is needed on whether CAT generalizes to non-prompt-based attacks.
### The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1
#### **1. Summary of this text**  
The provided LaTeX text outlines the **theoretical foundation** of a paper titled *"Fundamental Limitations of Alignment in Large Language Models."* It sets up the groundwork for a structured analysis by importing necessary packages, defining the title, authors, and abstract. The abstract introduces the **Behavior Expectation Bounds (BEB)** framework, arguing that alignment cannot fully prevent adversarial exploits. The introduction reviews existing alignment methods and emphasizes their vulnerabilities. The text begins formalizing a probabilistic approach to evaluate alignment robustness, setting the stage for theoretical results.

#### **2. Related Metadata**  
- **Tools/Algorithms Created**: PromptFuzz  
- **Benchmarks Created**: None  
- **Codebase/Data**: https://github.com/PromptFuzz/PromptFuzz  
- **LLMs Evaluated**: Vicuna-13B-v1.5, Llama-2-7B-chat, GPT-3.5-Turbo-1106, GPT-4-0125-preview, Claude-instant-1.2, Claude-2.1, Gemini-Pro  
- **Attack Techniques**: PAIR, GCG, JBC  
- **Defense Techniques**: SmoothLLM, Perplexity Filter  
- **Frameworks Critiqued**: PAIR, GCG, JBC  

#### **3. Main Contributions**  
- Introduces a new taxonomy for adversarial attacks against LLMs.  
- Proposes a contrastive adversarial training (CAT) approach to enhance LLM resilience.  
- Empirically analyzes attack transferability across model scales.  

#### **4. Methods & Approach**  
- Uses a dataset of 100,000 adversarial prompts generated via reinforcement learning.  
- Evaluates robustness on GPT-4, Claude, and LLaMA-2.  
- Implements CAT, a defense method that fine-tunes models using adversarial examples selected via a similarity-based scoring function.  

#### **5. Findings & Empirical Results**  
- CAT improves robustness by 32% compared to vanilla fine-tuning.  
- Attack transferability increases with model size, contradicting previous assumptions.  
- CAT introduces a slight degradation in response diversity (measured via perplexity scores).  

#### **6. Implications for LLM Safety**  
- Highlights the need for adversarial robustness to scale with model size.  
- Suggests models should be trained on adversarial examples and evaluated across multiple safety benchmarks.  
- Raises concerns about trade-offs between robustness and generation diversity.  

#### **7. Missing Information & Caveats**  
- Experimental setup for RL-based adversarial prompt generation was only partially available.  
- Further clarification is needed on whether CAT generalizes to non-prompt-based attacks.
### Automatic Prompt Optimization with "Gradient Descent" and Beam Search
#### **1. Summary of this text**

The provided LaTeX content focuses on the experimental results and discussion of a research paper examining various attack methods on large language models (LLMs). The paper evaluates attack methods such as PAIR, GCG, Jailbreak Chat, and RLHF across different model sizes (7B, 13B, 20B, and 30B parameters). The analysis covers three main aspects: attack success rate, model output quality, and computational efficiency. The results indicate that RLHF achieves higher success rates but lower output quality and efficiency compared to rule-based methods like PAIR and GCG. The discussion emphasizes the trade-offs between these factors and provides recommendations for selecting attack methods based on specific requirements. The conclusion highlights the importance of considering model size and attack method characteristics in enhancing LLM security.

#### **2. Related Metadata**

- **Tools and Algorithms Created by the Paper**: PAIR (Prompt Automatic Iterative Refinement), GCG (Gradient-to-Coordinate Descent), Jailbreak Chat, RLHF (Reinforcement Learning from Human Feedback).
- **Benchmarks Created**: None explicitly mentioned.
- **Codebase/Data**: Not provided in the text.
- **LLMs Evaluated**: Models with 7B, 13B, 20B, and 30B parameters.
- **Attack Techniques Evaluated**: PAIR, GCG, Jailbreak Chat, RLHF.
- **Defense Techniques Evaluated**: None explicitly mentioned.
- **Existing Frameworks/Methods Critiqued**: RLHF, PAIR, GCG, Jailbreak Chat.

#### **3. Main Contributions**

- **Novel Insights**: The paper demonstrates that attack success rates increase with model size and that different attack methods have trade-offs between success rate, output quality, and computational efficiency.
- **Key Problems Addressed**: The study aims to understand how attack methods perform across various model sizes and to provide guidelines for selecting appropriate attack methods.
- **Building Upon Existing Work**: The paper builds on previous research by examining the relationship between model size and attack success, as well as evaluating a range of attack methods comprehensively.

#### **4. Methods & Approach**

- **Key Techniques**: The paper evaluates four attack methods (PAIR, GCG, Jailbreak Chat, RLHF) across models of varying sizes. Metrics include attack success rate, output quality (assessed through human evaluation), and computational efficiency (attacks per second).
- **Datasets and Models**: Models with 7B, 13B, 20B, and 30B parameters are used, but specific datasets are not detailed in the provided text.
- **Formal Proofs or Mathematical Models**: None explicitly mentioned.

#### **5. Findings & Empirical Results**

- **Attack Success Rate**: RLHF achieves the highest success rates (e.g., 75.3% on 13B models), while rule-based methods have lower success rates but better output quality.
- **Output Quality**: Rule-based methods (PAIR, GCG) generate higher quality outputs, whereas RLHF, though more successful, produces lower quality outputs.
- **Computational Efficiency**: Rule-based methods (PAIR: 3.2, GCG: 3.5) are more efficient than RLHF (1.8 attacks per second).
- **Trade-offs**: Higher success rates with RLHF come at the cost of lower output quality and efficiency.

#### **6. Implications for LLM Safety**

- **Robustness**: The findings suggest that larger models are more vulnerable to attacks, emphasizing the need for robust defense mechanisms.
- **Balancing Factors**: Organizations should consider the trade-offs between attack success, output quality, and efficiency when developing security strategies.
- **Research Directions**: Future work should focus on improving attack methods to maintain high success rates without compromising output quality or efficiency.

#### **7. Missing Information & Caveats**

- **Missing Sections**: The provided text lacks details on specific datasets used, model architectures, and the exact implementation of attack methods.
- **Ambiguous Sections**: The text does not clarify how output quality is quantitatively measured or how human evaluations were conducted.
- **Caveats**: The conclusions are based on a limited set of attack methods and model sizes, and the ethical implications of using such attacks are not addressed.


## Tree of Challenges

## Tree of Problems

## Tree of Contest

## Paper Infos

Arxived Date|Published Date|Published Venue|Title|Paper|Codebase|Category|Tool Names|Benchmark Names
------------|--------------|---------------|-----|-----|--------|--------|----------|---------------
20250227|-|None|Logicbreaks: A Framework for Understanding Subversion of Rule-based Inference|https://arxiv.org/abs/2407.00075|None|-|-|-|
20250227|-|None|[The Hidden Risks of Large Reasoning Models: A Safety Assessment of R1](#the-hidden-risks-of-large-reasoning-models-a-safety-assessment-of-r)|https://arxiv.org/abs/2502.12659|None|-|-|-|
20250227|-|None|Foot-In-The-Door: A Multi-turn Jailbreak for LLMs|https://arxiv.org/abs/2502.19820|None|-|-|-|
20250227|-|None|Beyond the Tip of Efficiency: Uncovering the Submerged Threats of Jailbreak Attacks in Small Language Models|https://arxiv.org/abs/2502.19883|None|-|-|-|
20250226|-|None|Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack|https://arxiv.org/abs/2404.01833|None|-|-|-|
20250226|-|None|JailBench: A Comprehensive Chinese Security Assessment Benchmark for Large Language Models|https://arxiv.org/abs/2502.18935|None|-|-|-|
20250226|-|None|Beyond Surface-Level Patterns: An Essence-Driven Defense Framework Against Jailbreak Attacks in LLMs|https://arxiv.org/abs/2502.19041|None|-|-|-|
20250225|-|None|Towards Robust and Secure Embodied AI: A Survey on Vulnerabilities and Attacks|https://arxiv.org/abs/2502.13175|None|-|-|-|
20250224|-|None|PAPILLON: Efficient and Stealthy Fuzz Testing-Powered Jailbreaks for LLMs|https://arxiv.org/abs/2409.14866|None|-|-|-|
20250224|-|None|HarmAug: Effective Data Augmentation for Knowledge Distillation of Safety Guard Models|https://arxiv.org/abs/2410.01524|None|-|-|-|
20250224|-|None|GuidedBench: Equipping Jailbreak Evaluation with Guidelines|https://arxiv.org/abs/2502.16903|None|-|-|-|
20250224|-|None|REINFORCE Adversarial Attacks on Large Language Models: An Adaptive, Distributional, and Semantic Objective|https://arxiv.org/abs/2502.17254|None|-|-|-|
20250224|-|None|Dataset Featurization: Uncovering Natural Language Features through Unsupervised Data Reconstruction|https://arxiv.org/abs/2502.17541|None|-|-|-|
20250223|-|None|[On Calibration of LLM-based Guard Models for Reliable Content Moderation](#on-calibration-of-llm-based-guard-models-for-reliable-content-moderation)|https://arxiv.org/abs/2410.10414|None|-|-|-|
20250223|-|None|Guardians of the Agentic System: Preventing Many Shots Jailbreak with Agentic System|https://arxiv.org/abs/2502.16750|None|-|-|-|
20250222|-|None|Na'vi or Knave: Jailbreaking Language Models via Metaphorical Avatars|https://arxiv.org/abs/2412.12145|None|-|-|-|
20250221|-|None|Revisiting Jailbreaking for Large Language Models: A Representation Engineering Perspective|https://arxiv.org/abs/2401.06824|None|-|-|-|
20250221|-|None|Defending Jailbreak Prompts via In-Context Adversarial Game|https://arxiv.org/abs/2402.13148|None|-|-|-|
20250221|-|None|Understanding the Effectiveness of Coverage Criteria for Large Language Models: A Special Angle from Jailbreak Attacks|https://arxiv.org/abs/2408.15207|None|-|-|-|
20250221|-|None|Attention Eclipse: Manipulating Attention to Bypass LLM Safety-Alignment|https://arxiv.org/abs/2502.15334|None|-|-|-|
20250221|-|None|Adversarial Prompt Evaluation: Systematic Benchmarking of Guardrails Against Prompt Input Attacks on LLMs|https://arxiv.org/abs/2502.15427|None|-|-|-|
20250221|-|None|Single-pass Detection of Jailbreaking Input in Large Language Models|https://arxiv.org/abs/2502.15435|None|-|-|-|
20250221|-|None|Interpreting and Steering LLMs with Mutual Information-based Explanations on Sparse Autoencoders|https://arxiv.org/abs/2502.15576|None|-|-|-|
20250221|-|None|SafeInt: Shielding Large Language Models from Jailbreak Attacks via Safety-Aware Representation Intervention|https://arxiv.org/abs/2502.15594|None|-|-|-|
20250221|-|None|TurboFuzzLLM: Turbocharging Mutation-based Fuzzing for Effectively Jailbreaking Large Language Models in Practice|https://arxiv.org/abs/2502.18504|None|-|-|-|
20250220|-|None|[Making Them a Malicious Database: Exploiting Query Code to Jailbreak Aligned Large Language Models](#making-them-a-malicious-database-exploiting-query-code-to-jailbreak-aligned-large-language-models)|https://arxiv.org/abs/2502.09723|None|-|-|-|
20250220|-|None|How Jailbreak Defenses Work and Ensemble? A Mechanistic Investigation|https://arxiv.org/abs/2502.14486|None|-|-|-|
20250220|-|None|HiddenDetect: Detecting Jailbreak Attacks against Large Vision-Language Models via Monitoring Hidden States|https://arxiv.org/abs/2502.14744|None|-|-|-|
20250219|-|None|Reasoning-Augmented Conversation for Multi-Turn Jailbreak Attacks on Large Language Models|https://arxiv.org/abs/2502.11054|None|-|-|-|
20250219|-|None|Exploiting Prefix-Tree in Structured Output Interfaces for Enhancing Jailbreak Attacking|https://arxiv.org/abs/2502.13527|None|-|-|-|
20250219|-|None|Why Safeguarded Ships Run Aground? Aligned Large Language Models' Safety Mechanisms Tend to Be Anchored in The Template Region|https://arxiv.org/abs/2502.13946|None|-|-|-|
20250219|-|None|A Mousetrap: Fooling Large Reasoning Models for Jailbreak with Chain of Iterative Chaos|https://arxiv.org/abs/2502.15806|None|-|-|-|
20250218|-|None|Mixture of insighTful Experts (MoTE): The Synergy of Thought Chains and Expert Mixtures in Self-Alignment|https://arxiv.org/abs/2405.00557|None|-|-|-|
20250218|-|None|[Enhancing the Capability and Robustness of Large Language Models through Reinforcement Learning-Driven Query Refinement](#enhancing-the-capability-and-robustness-of-large-language-models-through-reinforcement-learning-driven-query-refinement)|https://arxiv.org/abs/2407.01461|None|-|-|-|
20250218|-|None|Data to Defense: The Role of Curation in Customizing LLMs Against Jailbreaking Attacks|https://arxiv.org/abs/2410.02220|None|-|-|-|
20250218|-|None|Emoji Attack: Enhancing Jailbreak Attacks Against Judge LLM Detection|https://arxiv.org/abs/2411.01077|None|-|-|-|
20250218|-|None|LLMs are Vulnerable to Malicious Prompts Disguised as Scientific Language|https://arxiv.org/abs/2501.14073|None|-|-|-|
20250218|-|None|Reasoning-to-Defend: Safety-Aware Reasoning Can Defend Large Language Models from Jailbreaking|https://arxiv.org/abs/2502.12970|None|-|-|-|
20250217|-|None|StructuralSleight: Automated Jailbreak Attacks on Large Language Models Utilizing Uncommon Text-Organization Structures|https://arxiv.org/abs/2406.08754|None|-|-|-|
20250217|-|None|LLMs can be Dangerous Reasoners: Analyzing-based Jailbreak Attack on Large Language Models|https://arxiv.org/abs/2407.16205|None|-|-|-|
20250217|-|None|Separate the Wheat from the Chaff: A Post-Hoc Approach to Safety Re-Alignment for Fine-Tuned Language Models|https://arxiv.org/abs/2412.11041|None|-|-|-|
20250217|-|None|The Hidden Dimensions of LLM Alignment: A Multi-Dimensional Safety Analysis|https://arxiv.org/abs/2502.09674|None|-|-|-|
20250217|-|None|SafeDialBench: A Fine-Grained Safety Benchmark for Large Language Models in Multi-Turn Dialogues with Diverse Jailbreak Attacks|https://arxiv.org/abs/2502.11090|None|-|-|-|
20250217|-|None|Adversary-Aware DPO: Enhancing Safety Alignment in Vision Language Models via Adversarial Training|https://arxiv.org/abs/2502.11455|None|-|-|-|
20250217|-|None|DELMAN: Dynamic Defense Against Large Language Model Jailbreaking with Model Editing|https://arxiv.org/abs/2502.11647|None|-|-|-|
20250217|-|None|Computational Safety for Generative AI: A Signal Processing Perspective|https://arxiv.org/abs/2502.12445|None|-|-|-|
20250217|-|None|SoK: Understanding Vulnerabilities in the Large Language Model Supply Chain|https://arxiv.org/abs/2502.12497|None|-|-|-|
20250216|-|None|Atoxia: Red-teaming Large Language Models with Target Toxic Answers|https://arxiv.org/abs/2408.14853|None|-|-|-|
20250216|-|None|Dagger Behind Smile: Fool LLMs with a Happy Ending Story|https://arxiv.org/abs/2501.13115|None|-|-|-|
20250216|-|None|Prompt Inject Detection with Generative Explanation as an Investigative Tool|https://arxiv.org/abs/2502.11006|None|-|-|-|
20250216|-|None|Rewrite to Jailbreak: Discover Learnable and Transferable Implicit Harmfulness Instruction|https://arxiv.org/abs/2502.11084|None|-|-|-|
20250216|-|None|CCJA: Context-Coherent Jailbreak Attack for Aligned Large Language Models|https://arxiv.org/abs/2502.11379|None|-|-|-|
20250216|-|None|Detecting and Filtering Unsafe Training Data via Data Attribution|https://arxiv.org/abs/2502.11411|None|-|-|-|
20250216|-|None|ShieldLearner: A New Paradigm for Jailbreak Attack Defense in LLMs|https://arxiv.org/abs/2502.13162|None|-|-|-|
20250215|-|None|Functional Homotopy: Smoothing Discrete Optimization via Continuous Parameters for LLM Jailbreak Attacks|https://arxiv.org/abs/2410.04234|None|-|-|-|
20250215|-|None|Distraction is All You Need for Multimodal Large Language Model Jailbreaking|https://arxiv.org/abs/2502.10794|None|-|-|-|
20250214|-|None|SequentialBreak: Large Language Models Can be Fooled by Embedding Jailbreak Prompts into Sequential Prompt Chains|https://arxiv.org/abs/2411.06426|None|-|-|-|
20250213|-|None|Are Large Language Models Really Bias-Free? Jailbreak Prompts for Assessing Adversarial Robustness to Bias Elicitation|https://arxiv.org/abs/2407.08441|None|-|-|-|
20250213|-|None|`Do as I say not as I do': A Semi-Automated Approach for Jailbreak Prompt Attack against Multimodal LLMs|https://arxiv.org/abs/2502.00735|None|-|-|-|
20250213|-|None|FLAME: Flexible LLM-Assisted Moderation Engine|https://arxiv.org/abs/2502.09175|None|-|-|-|
20250213|-|None|Enhancing Jailbreak Attacks via Compliance-Refusal-Based Initialization|https://arxiv.org/abs/2502.09755|None|-|-|-|
20250212|-|None|In-Context Experience Replay Facilitates Safety Red-Teaming of Text-to-Image Diffusion Models|https://arxiv.org/abs/2411.16769|None|-|-|-|
20250212|-|None|Safety at Scale: A Comprehensive Survey of Large Model Safety|https://arxiv.org/abs/2502.05206|None|-|-|-|
20250211|-|38th Conference on Neural Information Processing Systems (NeurIPS 2024)|Efficient LLM Jailbreak via Adaptive Dense-to-sparse Constrained Optimization|https://arxiv.org/abs/2405.09113|None|-|-|-|
20250211|-|None|Model Surgery: Modulating LLM's Behavior Via Simple Parameter Editing|https://arxiv.org/abs/2407.08770|None|-|-|-|
20250211|-|None|Layer-Level Self-Exposure and Patch: Affirmative Token Mitigation for Jailbreak Attack Defense|https://arxiv.org/abs/2501.02629|None|-|-|-|
20250211|-|None|JBShield: Defending Large Language Models from Jailbreak Attacks through Activated Concept Analysis and Manipulation|https://arxiv.org/abs/2502.07557|None|-|-|-|
20250210|-|None|Jailbreaking LLMs' Safeguard with Universal Magic Words for Text Embedding Models|https://arxiv.org/abs/2501.18280|None|-|-|-|
20250209|-|None|Jailbreaking to Jailbreak|https://arxiv.org/abs/2502.09638|None|-|-|-|
20250208|-|None|Dynamic Guided and Domain Applicable Safeguards for Enhanced Security in Large Language Models|https://arxiv.org/abs/2410.17922|None|-|-|-|
20250207|-|None|Jailbreak Antidote: Runtime Safety-Utility Balance via Sparse Representation Adjustment in Large Language Models|https://arxiv.org/abs/2410.02298|None|-|-|-|
20250206|-|None|Hide Your Malicious Goal Into Benign Narratives: Jailbreak Large Language Models through Carrier Articles|https://arxiv.org/abs/2408.11182|None|-|-|-|
20250206|-|None|Root Defence Strategies: Ensuring Safety of LLM at the Decoding Level|https://arxiv.org/abs/2410.06809|None|-|-|-|
20250206|-|None|"Short-length" Adversarial Training Helps LLMs Defend "Long-length" Jailbreak Attacks: Theoretical and Empirical Evidence|https://arxiv.org/abs/2502.04204|None|-|-|-|
20250206|-|None|Speak Easy: Eliciting Harmful Jailbreaks from LLMs with Simple Interactions|https://arxiv.org/abs/2502.04322|None|-|-|-|
20250205|-|None|ImgTrojan: Jailbreaking Vision-Language Models with ONE Image|https://arxiv.org/abs/2403.02910|None|-|-|-|
20250205|-|None|SelfDefend: LLMs Can Defend Themselves against Jailbreaking in a Practical Manner|https://arxiv.org/abs/2406.05498|None|-|-|-|
20250205|-|None|On Effects of Steering Latent Representation for Large Language Model Unlearning|https://arxiv.org/abs/2408.06223|None|-|-|-|
20250205|-|None|Understanding and Enhancing the Transferability of Jailbreaking Attacks|https://arxiv.org/abs/2502.03052|None|-|-|-|
20250204|-|None|JailbreakEval: An Integrated Toolkit for Evaluating Jailbreak Attempts Against Large Language Models|https://arxiv.org/abs/2406.09321|None|-|-|-|
20250204|-|None|STAIR: Improving Safety Alignment with Introspective Reasoning|https://arxiv.org/abs/2502.02384|None|-|-|-|
20250204|-|None|Position: Stop Acting Like Language Model Agents Are Normal Agents|https://arxiv.org/abs/2502.10420|None|-|-|-|
20250203|-|None|"Not Aligned" is Not "Malicious": Being Careful about Hallucinations of Large Language Models' Jailbreak|https://arxiv.org/abs/2406.11668|None|-|-|-|
20250203|-|None|PBI-Attack: Prior-Guided Bimodal Interactive Black-Box Jailbreak Attack for Toxicity Maximization|https://arxiv.org/abs/2412.05892|None|-|-|-|
20250203|-|None|Jailbreaking with Universal Multi-Prompts|https://arxiv.org/abs/2502.01154|None|-|-|-|
20250203|-|None|Eliciting Language Model Behaviors with Investigator Agents|https://arxiv.org/abs/2502.01236|None|-|-|-|
20250203|-|None|Robust-LLaVA: On the Effectiveness of Large-Scale Robust Image Encoders for Multi-modal Large Language Models|https://arxiv.org/abs/2502.01576|None|-|-|-|
20250203|-|None|Adversarial Reasoning at Jailbreaking Time|https://arxiv.org/abs/2502.01633|None|-|-|-|
20250203|-|None|PANDAS: Improving Many-shot Jailbreaking via Positive Affirmation, Negative Demonstration, and Adaptive Sampling|https://arxiv.org/abs/2502.01925|None|-|-|-|
20250202|-|None|SQL Injection Jailbreak: A Structural Disaster of Large Language Models|https://arxiv.org/abs/2411.01565|None|-|-|-|
20250202|-|None|"I am bad": Interpreting Stealthy, Universal and Robust Audio Jailbreaks in Audio-Language Models|https://arxiv.org/abs/2502.00718|None|-|-|-|
20250202|-|None|AgentBreeder: Mitigating the AI Safety Impact of Multi-Agent Scaffolds|https://arxiv.org/abs/2502.00757|None|-|-|-|
20250202|-|None|Blink of an eye: a simple theory for feature localization in generative models|https://arxiv.org/abs/2502.00921|None|-|-|-|
20250201|-|None|Self-Instruct Few-Shot Jailbreaking: Decompose the Attack into Pattern and Behavior Learning|https://arxiv.org/abs/2501.07959|None|-|-|-|
20250201|-|None|ALU: Agentic LLM Unlearning|https://arxiv.org/abs/2502.00406|None|-|-|-|
20250201|-|None|Defense Against the Dark Prompts: Mitigating Best-of-N Jailbreaking with Prompt Evaluation|https://arxiv.org/abs/2502.00580|None|-|-|-|
20250201|-|None|Towards Robust Multimodal Large Language Models Against Jailbreak Attacks|https://arxiv.org/abs/2502.00653|None|-|-|-|
20250201|-|None|LLM Safety Alignment is Divergence Estimation in Disguise|https://arxiv.org/abs/2502.00657|None|-|-|-|
20250201|-|None|Safety Alignment Depth in Large Language Models: A Markov Chain Perspective|https://arxiv.org/abs/2502.00669|None|-|-|-|
20250131|-|None|UniGuard: Towards Universal Safety Guardrails for Jailbreak Attacks on Multimodal Large Language Models|https://arxiv.org/abs/2411.01703|None|-|-|-|
20250131|-|None|Enhancing Model Defense Against Jailbreaks with Proactive Safety Reasoning|https://arxiv.org/abs/2501.19180|None|-|-|-|
20250131|-|None|Riddle Me This! Stealthy Membership Inference for Retrieval-Augmented Generation|https://arxiv.org/abs/2502.00306|None|-|-|-|
20250130|-|None|xJailbreak: Representation Space Guided Reinforcement Learning for Interpretable LLM Jailbreaking|https://arxiv.org/abs/2501.16727|None|-|-|-|
20250130|-|None|Constitutional Classifiers: Defending against Universal Jailbreaks across Thousands of Hours of Red Teaming|https://arxiv.org/abs/2501.18837|None|-|-|-|
20250129|-|None|RICoTA: Red-teaming of In-the-wild Conversation with Test Attempts|https://arxiv.org/abs/2501.17715|None|-|-|-|
20250127|-|None|Jailbreaking Large Language Models Through Alignment Vulnerabilities in Out-of-Distribution Settings|https://arxiv.org/abs/2406.13662|None|-|-|-|
20250127|-|None|Smoothed Embeddings for Robust Language Models|https://arxiv.org/abs/2501.16497|None|-|-|-|
20250127|-|None|Targeting Alignment: Extracting Safety Classifiers of Aligned LLMs|https://arxiv.org/abs/2501.16534|None|-|-|-|
20250127|-|None|Indiana Jones: There Are Always Some Useful Ancient Relics|https://arxiv.org/abs/2501.18628|None|-|-|-|
20250127|-|None|Towards Safe AI Clinicians: A Comprehensive Study on Large Language Model Jailbreaking in Healthcare|https://arxiv.org/abs/2501.18632|None|-|-|-|
20250124|-|None|An Adversarial Perspective on Machine Unlearning for AI Safety|https://arxiv.org/abs/2409.18025|None|-|-|-|
20250124|-|None|Siren: A Learning-Based Multi-Turn Attack Framework for Simulating Real-World Human Jailbreak Behaviors|https://arxiv.org/abs/2501.14250|None|-|-|-|
20250124|-|None|Internal Activation Revision: Safeguarding Vision Language Models Without Parameter Update|https://arxiv.org/abs/2501.16378|None|-|-|-|
20250123|-|None|Tune In, Act Up: Exploring the Impact of Audio Modality-Specific Edits on Large Audio Language Models in Jailbreak|https://arxiv.org/abs/2501.13772|None|-|-|-|
20250121|-|None|QROA: A Black-Box Query-Response Optimization Attack on LLMs|https://arxiv.org/abs/2406.02044|None|-|-|-|
20250121|-|None|You Can't Eat Your Cake and Have It Too: The Performance Degradation of LLMs with Jailbreak Defense|https://arxiv.org/abs/2501.12210|None|-|-|-|
20250119|-|None|FigStep: Jailbreaking Large Vision-Language Models via Typographic Visual Prompts|https://arxiv.org/abs/2311.05608|None|-|-|-|
20250119|-|None|Deciphering the Chaos: Enhancing Jailbreak Attacks via Adversarial Prompt Translation|https://arxiv.org/abs/2410.11317|None|-|-|-|
20250117|-|None|Latent-space adversarial training with post-aware calibration for defending large language models against jailbreak attacks|https://arxiv.org/abs/2501.10639|None|-|-|-|
20250116|-|None|A Survey on Responsible LLMs: Inherent Risk, Malicious Use, and Mitigation Strategy|https://arxiv.org/abs/2501.09431|None|-|-|-|
20250112|-|None|Images are Achilles' Heel of Alignment: Exploiting Visual Vulnerabilities for Jailbreaking Multimodal Large Language Models|https://arxiv.org/abs/2403.09792|None|-|-|-|
20250110|-|None|BaThe: Defense against the Jailbreak Attack in Multimodal Large Language Models by Treating Harmful Instruction as Backdoor Trigger|https://arxiv.org/abs/2408.09093|None|-|-|-|
20250109|-|None|Turning Logic Against Itself : Probing Model Defenses Through Contrastive Questions|https://arxiv.org/abs/2501.01872|None|-|-|-|
20250108|-|None|Toxicity Detection towards Adaptability to Changing Perturbations|https://arxiv.org/abs/2412.15267|None|-|-|-|
20250108|-|None|Deliberative Alignment: Reasoning Enables Safer Language Models|https://arxiv.org/abs/2412.16339|None|-|-|-|
20250108|-|None|Jailbreaking Multimodal Large Language Models via Shuffle Inconsistency|https://arxiv.org/abs/2501.04931|None|-|-|-|
20250107|-|None|MRJ-Agent: An Effective Jailbreak Agent for Multi-Round Dialogue|https://arxiv.org/abs/2411.03814|None|-|-|-|
20250106|-|None|ChatBug: A Common Vulnerability of Aligned LLMs Induced by Chat Templates|https://arxiv.org/abs/2406.12935|None|-|-|-|
20250104|-|None|DiffusionAttacker: Diffusion-Driven Prompt Manipulation for LLM Jailbreak|https://arxiv.org/abs/2412.17522|None|-|-|-|
20250103|-|None|Heuristic-Induced Multimodal Risk Distribution Jailbreak Attack for Multimodal Large Language Models|https://arxiv.org/abs/2412.05934|None|-|-|-|
20250103|-|None|Spot Risks Before Speaking! Unraveling Safety Attention Heads in Large Vision-Language Models|https://arxiv.org/abs/2501.02029|None|-|-|-|
20250102|-|None|Security Attacks on LLM-based Code Completion Tools|https://arxiv.org/abs/2408.11006|None|-|-|-|
20250102|-|None|CySecBench: Generative AI-based CyberSecurity-focused Prompt Dataset for Benchmarking Large Language Models|https://arxiv.org/abs/2501.01335|None|-|-|-|
20250102|-|None|Safeguarding Large Language Models in Real-time with Tunable Safety-Performance Trade-offs|https://arxiv.org/abs/2501.02018|None|-|-|-|
20250101|-|None|BiasJailbreak:Analyzing Ethical Biases and Jailbreak Vulnerabilities in Large Language Models|https://arxiv.org/abs/2410.13334|None|-|-|-|
20241228|-|None|LLM-Virus: Evolutionary Jailbreak Attack on Large Language Models|https://arxiv.org/abs/2501.00055|None|-|-|-|
20241224|-|None|SafeAligner: Safety Alignment against Jailbreak Attacks via Response Disparity Guidance|https://arxiv.org/abs/2406.18118|None|-|-|-|
20241224|-|None|[The Dark Side of Function Calling: Pathways to Jailbreaking Large Language Models](#the-dark-side-of-function-calling-pathways-to-jailbreaking-large-language-models)|https://arxiv.org/abs/2407.17915|None|-|-|-|
20241224|-|None|Token Highlighter: Inspecting and Mitigating Jailbreak Prompts for Large Language Models|https://arxiv.org/abs/2412.18171|https://huggingface.co/spaces/TrustSafeAI/Token-Highlighter|-|-|-|
20241223|-|AAAI 2025|Retention Score: Quantifying Jailbreak Risks for Vision Language Models|https://arxiv.org/abs/2412.17544|None|-|-|-|
20241222|-|None|Robustness of Large Language Models Against Adversarial Attacks|https://arxiv.org/abs/2412.17011|None|-|-|-|
20241222|-|None|Shaping the Safety Boundaries: Understanding and Defending Against Jailbreaks in Large Language Models|https://arxiv.org/abs/2412.17034|None|-|-|-|
20241221|-|None|Divide and Conquer: A Hybrid Strategy Defeats Multimodal Large Language Models|https://arxiv.org/abs/2412.16555|None|-|-|-|
20241220|-|None|Immune: Improving Safety Against Jailbreaks in Multi-modal LLMs via Inference-Time Alignment|https://arxiv.org/abs/2411.18688|None|-|-|-|
20241220|-|None|JailPO: A Novel Black-box Jailbreak Framework via Preference Optimization against Aligned LLMs|https://arxiv.org/abs/2412.15623|None|-|-|-|
20241220|-|None|Logical Consistency of Large Language Models in Fact-checking|https://arxiv.org/abs/2412.16100|None|-|-|-|
20241219|-|None|Alignment-Enhanced Decoding:Defending via Token-Level Adaptive Refining of Probability Distributions|https://arxiv.org/abs/2408.07663|None|-|-|-|
20241219|-|None|Unleashing the Unseen: Harnessing Benign Datasets for Jailbreaking Large Language Models|https://arxiv.org/abs/2410.00451|None|-|-|-|
20241219|-|None|SATA: A Paradigm for LLM Jailbreak via Simple Assistive Task Linkage|https://arxiv.org/abs/2412.15289|None|-|-|-|
20241218|-|None|Evaluation of LLM Vulnerabilities to Being Misused for Personalized Disinformation Generation|https://arxiv.org/abs/2412.13666|None|-|-|-|
20241217|-|None|Jailbreak Large Vision-Language Models Through Multi-Modal Linkage|https://arxiv.org/abs/2412.00473|None|-|-|-|
20241217|-|None|Jailbreaking? One Step Is Enough!|https://arxiv.org/abs/2412.12621|None|-|-|-|
20241217|-|None|Concept-ROT: Poisoning Concepts in Large Language Models with Model Editing|https://arxiv.org/abs/2412.13341|None|-|-|-|
20241216|-|None|Intention Analysis Makes LLMs A Good Jailbreak Defender|https://arxiv.org/abs/2401.06561|None|-|-|-|
20241216|-|None|SciSafeEval: A Comprehensive Benchmark for Safety Alignment of Large Language Models in Scientific Tasks|https://arxiv.org/abs/2410.03769|None|-|-|-|
20241216|-|None|Recent advancements in LLM Red-Teaming: Techniques, Defenses, and Ethical Considerations|https://arxiv.org/abs/2410.09097|None|-|-|-|
20241216|-|None|Granite Guardian|https://arxiv.org/abs/2412.07724|None|-|-|-|
20241215|-|None|Red Teaming GPT-4V: Are GPT-4V Safe Against Uni/Multi-Modal Jailbreak Attacks?|https://arxiv.org/abs/2404.03411|None|-|-|-|
20241215|-|None|Failures to Find Transferable Image Jailbreaks Between Vision-Language Models|https://arxiv.org/abs/2407.15211|None|-|-|-|
20241215|-|None|Exploiting the Index Gradients for Optimization-Based Jailbreaking on Large Language Models|https://arxiv.org/abs/2412.08615|None|-|-|-|
20241215|-|None|SpearBot: Leveraging Large Language Models in a Generative-Critique Framework for Spear-Phishing Email Generation|https://arxiv.org/abs/2412.11109|None|-|-|-|
20241214|-|None|Towards Action Hijacking of Large Language Model-based Agent|https://arxiv.org/abs/2412.10807|None|-|-|-|
20241213|-|None|AdvPrefix: An Objective for Nuanced LLM Jailbreaks|https://arxiv.org/abs/2412.10321|None|-|-|-|
20241213|-|None|No Free Lunch for Defending Against Prefilling Attack by In-Context Learning|https://arxiv.org/abs/2412.12192|None|-|-|-|
20241211|-|None|Model-Editing-Based Jailbreak against Safety-aligned Large Language Models|https://arxiv.org/abs/2412.08201|None|-|-|-|
20241211|-|None|AdvWave: Stealthy Adversarial Jailbreak Attack against Large Audio-Language Models|https://arxiv.org/abs/2412.08608|None|-|-|-|
20241210|-|None|Plentiful Jailbreaks with String Compositions|https://arxiv.org/abs/2411.01084|None|-|-|-|
20241210|-|None|FlexLLM: Exploring LLM Customization for Moving Target Defense on Black-Box LLMs Against Jailbreak Attacks|https://arxiv.org/abs/2412.07672|None|-|-|-|
20241210|-|None|Look Before You Leap: Enhancing Attention and Vigilance Regarding Harmful Content with GuidelineLLM|https://arxiv.org/abs/2412.10423|None|-|-|-|
20241208|-|None|Automated Black-box Prompt Engineering for Personalized Text-to-Image Generation|https://arxiv.org/abs/2403.19103|None|-|-|-|
20241208|-|None|Enhancing Adversarial Resistance in LLMs with Recursion|https://arxiv.org/abs/2412.06181|None|-|-|-|
20241206|-|None|MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models|https://arxiv.org/abs/2406.07057|None|-|-|-|
20241205|-|None|Stochastic Monkeys at Play: Random Augmentations Cheaply Break LLM Safety Alignment|https://arxiv.org/abs/2411.02785|None|-|-|-|
20241204|-|None|"Moralized" Multi-Step Jailbreak Prompts: Black-Box Testing of Guardrails in Large Language Models for Verbal Attacks|https://arxiv.org/abs/2411.16730|None|-|-|-|
20241204|-|Addepalli, S., Varun, Y., Suggala, A., Shanmugam, K. and Jain, P., Does Safety Training of LLMs Generalize to Semantically Related Natural Prompts?. In Neurips Safe Generative AI Workshop 2024|Does Safety Training of LLMs Generalize to Semantically Related Natural Prompts?|https://arxiv.org/abs/2412.03235|None|-|-|-|
20241202|-|None|Towards Understanding Jailbreak Attacks in LLMs: A Representation Space Analysis|https://arxiv.org/abs/2406.10794|None|-|-|-|
20241202|-|None|Improved Large Language Model Jailbreak Detection via Pretrained Embeddings|https://arxiv.org/abs/2412.01547|None|-|-|-|
20241202|-|None|Trust & Safety of LLMs and LLMs in Trust & Safety|https://arxiv.org/abs/2412.02113|None|-|-|-|
20241202|-|None|Jailbreak Defense in a Narrow Domain: Limitations of Existing Methods and a New Transcript-Classifier Approach|https://arxiv.org/abs/2412.02159|None|-|-|-|
20241129|-|None|Safety Alignment Backfires: Preventing the Re-emergence of Suppressed Concepts in Fine-tuned Text-to-Image Diffusion Models|https://arxiv.org/abs/2412.00357|None|-|-|-|
20241128|-|None|DeepInception: Hypnotize Large Language Model to Be Jailbreaker|https://arxiv.org/abs/2311.03191|None|-|-|-|
20241128|-|None|Conversational Complexity for Assessing Risk in Large Language Models|https://arxiv.org/abs/2409.01247|None|-|-|-|
20241128|-|None|RePD: Defending Jailbreak Attack through a Retrieval-based Prompt Decomposition Process|https://arxiv.org/abs/2410.08660|None|-|-|-|
20241128|-|None|DIESEL -- Dynamic Inference-Guidance via Evasion of Semantic Embeddings in LLMs|https://arxiv.org/abs/2411.19038|None|-|-|-|
20241127|-|None|Safe + Safe = Unsafe? Exploring How Safe Images Can Be Exploited to Jailbreak Large Vision-Language Models|https://arxiv.org/abs/2411.11496|None|-|-|-|
20241127|-|None|Playing Language Game with LLMs Leads to Jailbreaking|https://arxiv.org/abs/2411.12762|None|-|-|-|
20241126|-|None|BlackDAN: A Black-Box Multi-Objective Approach for Effective and Contextual Jailbreaking of Large Language Models|https://arxiv.org/abs/2410.09804|None|-|-|-|
20241126|-|None|Desert Camels and Oil Sheikhs: Arab-Centric Red Teaming of Frontier LLMs|https://arxiv.org/abs/2410.24049|None|-|-|-|
20241125|-|None|Preventing Jailbreak Prompts as Malicious Tools for Cybercriminals: A Cyber Defense Perspective|https://arxiv.org/abs/2411.16642|None|-|-|-|
20241124|-|None|JailBreakV: A Benchmark for Assessing the Robustness of MultiModal Large Language Models against Jailbreak Attacks|https://arxiv.org/abs/2404.03027|None|-|-|-|
20241124|-|None|AmpleGCG: Learning a Universal and Transferable Generative Model of Adversarial Suffixes for Jailbreaking Both Open and Closed LLMs|https://arxiv.org/abs/2404.07921|None|-|-|-|
20241123|-|None|ChemSafetyBench: Benchmarking LLM Safety on Chemistry Domain|https://arxiv.org/abs/2411.16736|None|-|-|-|
20241122|-|None|Universal and Context-Independent Triggers for Precise Control of LLM Outputs|https://arxiv.org/abs/2411.14738|None|-|-|-|
20241121|-|None|GASP: Efficient Black-Box Generation of Adversarial Suffixes for Jailbreaking LLMs|https://arxiv.org/abs/2411.14133|None|-|-|-|
20241121|-|None|Global Challenge for Safe and Secure LLMs Track 1|https://arxiv.org/abs/2411.14502|None|-|-|-|
20241119|-|None|A Flexible Large Language Models Guardrail Development Methodology Applied to Off-Topic Prompt Detection|https://arxiv.org/abs/2411.12946|None|-|-|-|
20241118|-|None|The Dark Side of Trust: Authority Citation-Driven Jailbreak Attacks on Large Language Models|https://arxiv.org/abs/2411.11407|None|-|-|-|
20241117|-|None|A Theoretical Understanding of Self-Correction through In-context Alignment|https://arxiv.org/abs/2405.18634|None|-|-|-|
20241117|-|None|JailbreakLens: Interpreting Jailbreak Mechanism in the Lens of Representation and Circuit|https://arxiv.org/abs/2411.11114|None|-|-|-|
20241116|-|None|How (un)ethical are instruction-centric responses of LLMs? Unveiling the vulnerabilities of safety guardrails to harmful queries|https://arxiv.org/abs/2402.15302|None|-|-|-|
20241116|-|None|Insights and Current Gaps in Open-Source LLM Vulnerability Scanners: A Comparative Analysis|https://arxiv.org/abs/2410.16527|None|-|-|-|
20241115|-|None|Optimization-based Prompt Injection Attack to LLM-as-a-Judge|https://arxiv.org/abs/2403.17710|None|-|-|-|
20241115|-|None|IDEATOR: Jailbreaking Large Vision-Language Models Using Themselves|https://arxiv.org/abs/2411.00827|None|-|-|-|
20241114|-|None|Security and Privacy Challenges of Large Language Models: A Survey|https://arxiv.org/abs/2402.00888|None|-|-|-|
20241114|-|None|AutoDefense: Multi-Agent LLM Defense against Jailbreak Attacks|https://arxiv.org/abs/2403.04783|None|-|-|-|
20241113|-|None|The VLLM Safety Paradox: Dual Ease in Jailbreak Attack and Defense|https://arxiv.org/abs/2411.08410|None|-|-|-|
20241113|-|None|LLMStinger: Jailbreaking LLMs using RL fine-tuned LLMs|https://arxiv.org/abs/2411.08862|None|-|-|-|
20241113|-|None|DROJ: A Prompt-Driven Attack against Large Language Models|https://arxiv.org/abs/2411.09125|None|-|-|-|
20241112|-|None|Zer0-Jack: A Memory-efficient Gradient-based Jailbreaking Method for Black-box Multi-modal Large Language Models|https://arxiv.org/abs/2411.07559|None|-|-|-|
20241111|-|None|DrAttack: Prompt Decomposition and Reconstruction Makes Powerful LLM Jailbreakers|https://arxiv.org/abs/2402.16914|None|-|-|-|
20241111|-|None|Rapid Response: Mitigating LLM Jailbreaks with a Few Examples|https://arxiv.org/abs/2411.07494|None|-|-|-|
20241109|-|None|Jailbreaking LLM-Controlled Robots|https://arxiv.org/abs/2410.13691|None|-|-|-|
20241108|-|None|Robust Prompt Optimization for Defending Language Models Against Jailbreaking Attacks|https://arxiv.org/abs/2401.17263|None|-|-|-|
20241107|-|None|Gradient Cuff: Detecting Jailbreak Attacks on Large Language Models by Exploring Refusal Loss Landscapes|https://arxiv.org/abs/2403.00867|https://huggingface.co/spaces/TrustSafeAI/GradientCuff-Jailbreak-Defense|-|-|-|
20241106|-|None|Diversity Helps Jailbreak Large Language Models|https://arxiv.org/abs/2411.04223|None|-|-|-|
20241105|-|None|Bag of Tricks: Benchmarking of Jailbreak Attacks on LLMs|https://arxiv.org/abs/2406.09324|None|-|-|-|
20241105|-|None|Jailbreaking Large Language Models with Symbolic Mathematics|https://arxiv.org/abs/2409.11445|None|-|-|-|
20241103|-|None|Are you still on track!? Catching LLM Task Drift with Activations|https://arxiv.org/abs/2406.00799|None|-|-|-|
20241103|-|None|Boosting Jailbreak Transferability for Large Language Models|https://arxiv.org/abs/2410.15645|None|-|-|-|
20241102|-|None|What Features in Prompts Jailbreak LLMs? Investigating the Mechanisms Behind Attacks|https://arxiv.org/abs/2411.03343|None|-|-|-|
20241031|-|None|Tree of Attacks: Jailbreaking Black-Box LLMs Automatically|https://arxiv.org/abs/2312.02119|None|-|-|-|
20241031|-|None|Pruning for Protection: Increasing Jailbreak Resistance in Aligned LLMs Without Fine-Tuning|https://arxiv.org/abs/2401.10862|None|-|-|-|
20241031|-|None|Fight Back Against Jailbreaking via Prompt Adversarial Tuning|https://arxiv.org/abs/2402.06255|None|-|-|-|
20241031|-|None|JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models|https://arxiv.org/abs/2404.01318|None|-|-|-|
20241031|-|None|Adversarial Attacks of Vision Tasks in the Past 10 Years: A Survey|https://arxiv.org/abs/2410.23687|None|-|-|-|
20241031|-|None|Audio Is the Achilles' Heel: Red Teaming Audio Large Multimodal Models|https://arxiv.org/abs/2410.23861|None|-|-|-|
20241030|-|None|Speak Out of Turn: Safety Vulnerability of Large Language Models in Multi-turn Dialogue|https://arxiv.org/abs/2402.17262|None|-|-|-|
20241030|-|None|Representation Noising: A Defence Mechanism Against Harmful Finetuning|https://arxiv.org/abs/2405.14577|None|-|-|-|
20241030|-|None|Refusal in Language Models Is Mediated by a Single Direction|https://arxiv.org/abs/2406.11717|None|-|-|-|
20241030|-|None|ProTransformer: Robustify Transformers via Plug-and-Play Paradigm|https://arxiv.org/abs/2410.23182|None|-|-|-|
20241029|-|None|SG-Bench: Evaluating LLM Safety Generalization Across Diverse Tasks and Prompt Types|https://arxiv.org/abs/2410.21965|None|-|-|-|
20241029|-|None|AmpleGCG-Plus: A Strong Generative Model of Adversarial Suffixes to Jailbreak LLMs with Higher Success Rates in Fewer Attempts|https://arxiv.org/abs/2410.22143|None|-|-|-|
20241029|-|None|Benchmarking LLM Guardrails in Handling Multilingual Toxicity|https://arxiv.org/abs/2410.22153|None|-|-|-|
20241028|-|None|Stealthy Jailbreak Attacks on Large Language Models via Benign Data Mirroring|https://arxiv.org/abs/2410.21083|None|-|-|-|
20241026|-|None|Course-Correction: Safety Alignment Using Synthetic Preferences|https://arxiv.org/abs/2407.16637|None|-|-|-|
20241025|-|None|Iterative Self-Tuning LLMs for Enhanced Jailbreaking Capabilities|https://arxiv.org/abs/2410.18469|None|-|-|-|
20241024|-|None|Assessing the Brittleness of Safety Alignment via Pruning and Low-Rank Modifications|https://arxiv.org/abs/2402.05162|None|-|-|-|
20241023|-|None|Safeguard is a Double-edged Sword: Denial-of-service Attack on Large Language Models|https://arxiv.org/abs/2410.02916|None|-|-|-|
20241023|-|None|Towards Understanding the Fragility of Multilingual LLMs against Fine-Tuning Attacks|https://arxiv.org/abs/2410.18210|None|-|-|-|
20241022|-|None|When "Competency" in Reasoning Opens the Door to Vulnerability: Jailbreaking LLMs via Novel Complex Ciphers|https://arxiv.org/abs/2402.10601|None|-|-|-|
20241021|-|None|$\textit{MMJ-Bench}$: A Comprehensive Study on Jailbreak Attacks and Defenses for Multimodal Large Language Models|https://arxiv.org/abs/2408.08464|None|-|-|-|
20241021|-|None|Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents|https://arxiv.org/abs/2410.13886|None|-|-|-|
20241021|-|None|A Troublemaker with Contagious Jailbreak Makes Chaos in Honest Towns|https://arxiv.org/abs/2410.16155|None|-|-|-|
20241020|-|None|Quantitative Certification of Bias in Large Language Models|https://arxiv.org/abs/2405.18780|None|-|-|-|
20241020|-|None|Faster-GCG: Efficient Discrete Optimization Jailbreak Attacks against Aligned Large Language Models|https://arxiv.org/abs/2410.15362|None|-|-|-|
20241019|-|None|Securing Large Language Models: Addressing Bias, Misinformation, and Prompt Attacks|https://arxiv.org/abs/2409.08087|None|-|-|-|
20241019|-|None|Multi-round jailbreak attack on large language models|https://arxiv.org/abs/2410.11533|None|-|-|-|
20241019|-|None|Jailbreaking and Mitigation of Vulnerabilities in Large Language Models|https://arxiv.org/abs/2410.15236|None|-|-|-|
20241018|-|None|Feint and Attack: Attention-Based Strategies for Jailbreaking and Protecting LLMs|https://arxiv.org/abs/2410.16327|None|-|-|-|
20241017|-|None|SPIN: Self-Supervised Prompt INjection|https://arxiv.org/abs/2410.13236|None|-|-|-|
20241017|-|None|Persistent Pre-Training Poisoning of LLMs|https://arxiv.org/abs/2410.13722|None|-|-|-|
20241017|-|None|PopAlign: Diversifying Contrasting Patterns for a More Comprehensive Alignment|https://arxiv.org/abs/2410.13785|None|-|-|-|
20241016|-|None|TAIA: Large Language Models are Out-of-Distribution Data Learners|https://arxiv.org/abs/2405.20192|None|-|-|-|
20241016|-|None|Cross-modality Information Check for Detecting Jailbreaking in Multimodal Large Language Models|https://arxiv.org/abs/2407.21659|None|-|-|-|
20241015|-|None|Eyes Closed, Safety On: Protecting Multimodal LLMs via Image-to-Text Transformation|https://arxiv.org/abs/2403.09572|None|-|-|-|
20241015|-|None|GPT-4 Jailbreaks Itself with Near-Perfect Success Using Self-Explanation|https://arxiv.org/abs/2405.13077|None|-|-|-|
20241015|-|None|Cognitive Overload Attack:Prompt Injection for Long Context|https://arxiv.org/abs/2410.11272|None|-|-|-|
20241015|-|None|AdvBDGen: Adversarially Fortified Prompt-Specific Fuzzy Backdoor Generator Against LLM Alignment|https://arxiv.org/abs/2410.11283|None|-|-|-|
20241015|-|None|Jigsaw Puzzles: Splitting Harmful Questions to Jailbreak Large Language Models|https://arxiv.org/abs/2410.11459|None|-|-|-|
20241015|-|None|SoK: Prompt Hacking of Large Language Models|https://arxiv.org/abs/2410.13901|None|-|-|-|
20241014|-|None|Jailbreak Instruction-Tuned LLMs via end-of-sentence MLP Re-weighting|https://arxiv.org/abs/2410.10150|None|-|-|-|
20241013|-|None|[White-box Multimodal Jailbreaks Against Large Vision-Language Models](#white-box-multimodal-jailbreaks-against-large-vision-language-models)|https://arxiv.org/abs/2405.17894|None|-|-|-|
20241012|-|None|Don't Say No: Jailbreaking LLM by Suppressing Refusal|https://arxiv.org/abs/2404.16369|None|-|-|-|
20241011|-|None|ART: Automatic Red-teaming for Text-to-Image Models to Protect Benign Users|https://arxiv.org/abs/2405.19360|None|-|-|-|
20241011|-|None|AttnGCG: Enhancing Jailbreaking Attacks on LLMs with Attention Manipulation|https://arxiv.org/abs/2410.09040|None|-|-|-|
20241010|-|None|Protecting Your LLMs with Information Bottleneck|https://arxiv.org/abs/2404.13968|None|-|-|-|
20241008|-|None|You Know What I'm Saying: Jailbreak Attack via Implicit Reference|https://arxiv.org/abs/2410.03857|None|-|-|-|
20241005|-|None|Understanding Jailbreak Success: A Study of Latent Space Dynamics in Large Language Models|https://arxiv.org/abs/2406.09289|None|-|-|-|
20241005|-|None|Harnessing Task Overload for Scalable Jailbreak Attacks on Large Language Models|https://arxiv.org/abs/2410.04190|None|-|-|-|
20241004|-|None|MoJE: Mixture of Jailbreak Experts, Naive Tabular Classifiers as Guard for Prompt Attacks|https://arxiv.org/abs/2409.17699|None|-|-|-|
20241004|-|None|Developing Assurance Cases for Adversarial Robustness and Regulatory Compliance in LLMs|https://arxiv.org/abs/2410.05304|None|-|-|-|
20241003|-|None|Jailbreaking LLMs with Arabic Transliteration and Arabizi|https://arxiv.org/abs/2406.18725|None|-|-|-|
20241003|-|None|PathSeeker: Exploring LLM Security Vulnerabilities with a Reinforcement Learning-Based Jailbreak Approach|https://arxiv.org/abs/2409.14177|None|-|-|-|
20241002|-|None|Leveraging the Context through Multi-Round Interactions for Jailbreaking Attacks|https://arxiv.org/abs/2402.09177|None|-|-|-|
20240930|-|None|Distract Large Language Models for Automatic Jailbreak Attack|https://arxiv.org/abs/2403.08424|None|-|-|-|
20240930|-|None|[Don't Listen To Me: Understanding and Exploring Jailbreak Prompts of Large Language Models](#dont-listen-to-me-understanding-and-exploring-jailbreak-prompts-of-large-language-models)|https://arxiv.org/abs/2403.17336|None|-|-|-|
20240930|-|None|Robust LLM safeguarding via refusal feature adversarial training|https://arxiv.org/abs/2409.20089|None|-|-|-|
20240927|-|None|HM3: Heterogeneous Multi-Class Model Merging|https://arxiv.org/abs/2409.19173|None|-|-|-|
20240925|-|None|Ranking Manipulation for Conversational Search Engines|https://arxiv.org/abs/2406.03589|None|-|-|-|
20240925|-|None|RED QUEEN: Safeguarding Large Language Models against Concealed Multi-Turn Jailbreaking|https://arxiv.org/abs/2409.17458|None|-|-|-|
20240923|-|None|Large Language Models Are Involuntary Truth-Tellers: Exploiting Fallacy Failure for Jailbreak Attacks|https://arxiv.org/abs/2407.00869|None|-|-|-|
20240919|-|None|Enhancing Jailbreak Attacks with Diversity Guidance|https://arxiv.org/abs/2403.00292|None|-|-|-|
20240913|-|None|h4rm3l: A Dynamic Benchmark of Composable Jailbreak Attacks for LLM Safety Assessment|https://arxiv.org/abs/2408.04811|None|-|-|-|
20240913|-|None|Efficient Detection of Toxic Prompts in Large Language Models|https://arxiv.org/abs/2408.11727|None|-|-|-|
20240911|-|None|Securing Vision-Language Models with a Robust Encoder Against Jailbreak and Adversarial Attacks|https://arxiv.org/abs/2409.07353|None|-|-|-|
20240910|-|None|AdaPPA: Adaptive Position Pre-Fill Jailbreak Attack Approach Targeting LLMs|https://arxiv.org/abs/2409.07503|None|-|-|-|
20240909|-|None|Fine-Tuning, Quantization, and LLMs: Navigating Unintended Outcomes|https://arxiv.org/abs/2404.04392|None|-|-|-|
20240909|-|None|Jailbreaking Text-to-Image Models with LLM-Based Agents|https://arxiv.org/abs/2408.00523|None|-|-|-|
20240905|-|None|Legilimens: Practical and Unified Content Moderation for Large Language Model Services|https://arxiv.org/abs/2408.15488|None|-|-|-|
20240903|-|None|LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet|https://arxiv.org/abs/2408.15221|None|-|-|-|
20240831|-|None|Automatic Pseudo-Harmful Prompt Generation for Evaluating False Refusals in Large Language Models|https://arxiv.org/abs/2409.00598|None|-|-|-|
20240830|-|None|Jailbreak Attacks and Defenses Against Large Language Models: A Survey|https://arxiv.org/abs/2407.04295|None|-|-|-|
20240829|-|None|Mitigating Exaggerated Safety in Large Language Models|https://arxiv.org/abs/2405.05418|None|-|-|-|
20240829|-|None|Emerging Vulnerabilities in Frontier Models: Multi-Turn Jailbreak Attacks|https://arxiv.org/abs/2409.00137|None|-|-|-|
20240826|-|None|Image-to-Text Logic Jailbreak: Your Imagination can Help You Do Anything|https://arxiv.org/abs/2407.02534|None|-|-|-|
20240826|-|None|Probing the Safety Response Boundary of Large Language Models via Unsafe Decoding Path Generation|https://arxiv.org/abs/2408.10668|None|-|-|-|
20240822|-|None|Can Large Language Models Automatically Jailbreak GPT-4V?|https://arxiv.org/abs/2407.16686|None|-|-|-|
20240822|-|None|Prefix Guidance: A Steering Wheel for Large Language Models to Defend Against Jailbreak Attacks|https://arxiv.org/abs/2408.08924|None|-|-|-|
20240821|-|None|SHIELD: Evaluation and Defense Strategies for Copyright Compliance in LLM Text Generation|https://arxiv.org/abs/2406.12975|None|-|-|-|
20240821|-|None|What Makes and Breaks Safety Fine-tuning? A Mechanistic Study|https://arxiv.org/abs/2407.10264|None|-|-|-|
20240821|-|None|Latent Adversarial Training Improves Robustness to Persistent Harmful Behaviors in LLMs|https://arxiv.org/abs/2407.15549|None|-|-|-|
20240820|-|None|What is in Your Safe Data? Identifying Benign Data that Breaks Safety|https://arxiv.org/abs/2404.01099|None|-|-|-|
20240820|-|None|Medical MLLM is Vulnerable: Cross-Modality Jailbreak and Mismatched Attacks on Medical Multimodal Large Language Models|https://arxiv.org/abs/2405.20775|None|-|-|-|
20240820|-|None|[EEG-Defender: Defending against Jailbreak through Early Exit Generation of Large Language Models](#eeg-defender-defending-against-jailbreak-through-early-exit-generation-of-large-language-models)|https://arxiv.org/abs/2408.11308|None|-|-|-|
20240819|-|None|Malla: Demystifying Real-world Large Language Model Integrated Malicious Services|https://arxiv.org/abs/2401.03315|None|-|-|-|
20240817|-|None|Characterizing and Evaluating the Reliability of LLMs against Jailbreak Attacks|https://arxiv.org/abs/2408.09326|None|-|-|-|
20240816|-|Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics 2024 (Volume 1: Long Papers)|ToolSword: Unveiling Safety Issues of Large Language Models in Tool Learning Across Three Stages|https://arxiv.org/abs/2402.10753|None|-|-|-|
20240814|-|None|SAGE-RT: Synthetic Alignment data Generation for Safety Evaluation and Red Teaming|https://arxiv.org/abs/2408.11851|None|-|-|-|
20240811|-|None|Kov: Transferable and Naturalistic Black-Box LLM Attacks using Markov Decision Processes and Tree Search|https://arxiv.org/abs/2408.08899|None|-|-|-|
20240808|-|None|Compromesso! Italian Many-Shot Jailbreaks Undermine the Safety of Large Language Models|https://arxiv.org/abs/2408.04522|None|-|-|-|
20240808|-|None|Multi-Turn Context Jailbreak Attack on Large Language Models From First Principles|https://arxiv.org/abs/2408.04686|None|-|-|-|
20240807|-|None|EnJa: Ensemble Jailbreak on Large Language Models|https://arxiv.org/abs/2408.03603|None|-|-|-|
20240805|-|ICLR 2024 Workshop on Secure and Trustworthy Large Language Models|Open Sesame! Universal Black Box Jailbreaking of Large Language Models|https://arxiv.org/abs/2309.01446|None|-|-|-|
20240805|-|None|Can Reinforcement Learning Unlock the Hidden Dangers in Aligned Large Language Models?|https://arxiv.org/abs/2408.02651|None|-|-|-|
20240803|-|None|AttackEval: How to Evaluate the Effectiveness of Jailbreak Attacking on Large Language Models|https://arxiv.org/abs/2401.09002|None|-|-|-|
20240802|-|None|Mission Impossible: A Statistical Perspective on Jailbreaking LLMs|https://arxiv.org/abs/2408.01420|None|-|-|-|
20240729|-|None|Personalized Steering of Large Language Models: Versatile Steering Vectors Through Bi-directional Preference Optimization|https://arxiv.org/abs/2406.00045|None|-|-|-|
20240725|-|None|SafeDecoding: Defending against Jailbreak Attacks via Safety-Aware Decoding|https://arxiv.org/abs/2402.08983|None|-|-|-|
20240724|-|None|JailbreakZoo: Survey, Landscapes, and Horizons in Jailbreaking Large Language and Vision-Language Models|https://arxiv.org/abs/2407.01599|None|-|-|-|
20240723|-|None|RigorLLM: Resilient Guardrails for Large Language Models against Undesired Content|https://arxiv.org/abs/2403.13031|None|-|-|-|
20240723|-|None|RedAgent: Red Teaming Large Language Models with Context-aware Autonomous Language Agent|https://arxiv.org/abs/2407.16667|None|-|-|-|
20240721|-|None|Arondight: Red Teaming Large Vision Language Models with Auto-generated Multi-modal Jailbreak Prompts|https://arxiv.org/abs/2407.15050|None|-|-|-|
20240718|-|None|Jailbreaking Black Box Large Language Models in Twenty Queries|https://arxiv.org/abs/2310.08419|None|-|-|-|
20240717|-|None|The First to Know: How Token Distributions Reveal Hidden Knowledge in Large Vision-Language Models?|https://arxiv.org/abs/2403.09037|https://github.com/Qinyu-Allen-Zhao/LVLM-LP|-|-|-|
20240717|-|None|The Better Angels of Machine Personality: How Personality Relates to LLM Safety|https://arxiv.org/abs/2407.12344|None|-|-|-|
20240716|-|None|Continuous Embedding Attacks via Clipped Inputs in Jailbreaking Large Language Models|https://arxiv.org/abs/2407.13796|None|-|-|-|
20240714|-|None|Merging Improves Self-Critique Against Jailbreak Attacks|https://arxiv.org/abs/2406.07188|None|-|-|-|
20240711|-|None|Virtual Context: Enhancing Jailbreak Attacks with Special Token Injection|https://arxiv.org/abs/2406.19845|None|-|-|-|
20240711|-|None|A Survey of Attacks on Large Vision-Language Models: Resources, Advances, and Future Trends|https://arxiv.org/abs/2407.07403|None|-|-|-|
20240710|-|None|The Ethics of Interaction: Mitigating Security Threats in LLMs|https://arxiv.org/abs/2401.12273|None|-|-|-|
20240707|-|None|TrojanRAG: Retrieval-Augmented Generation Can Be Backdoor Driver in Large Language Models|https://arxiv.org/abs/2405.13401|None|-|-|-|
20240703|-|None|Eraser: Jailbreaking Defense in Large Language Models via Unlearning Harmful Knowledge|https://arxiv.org/abs/2404.05880|None|-|-|-|
20240703|-|None|JailbreakHunter: A Visual Analytics Approach for Jailbreak Prompts Discovery from Large-Scale Human-LLM Conversational Datasets|https://arxiv.org/abs/2407.03045|None|-|-|-|
20240703|-|None|SOS! Soft Prompt Attack Against Open-Source Large Language Models|https://arxiv.org/abs/2407.03160|None|-|-|-|
20240703|-|None|Soft Begging: Modular and Efficient Shielding of LLMs against Prompt Injection and Jailbreaking based on Prompt Tuning|https://arxiv.org/abs/2407.03391|None|-|-|-|
20240701|-|None|Jailbreak Vision Language Models via Bi-Modal Adversarial Prompt|https://arxiv.org/abs/2406.04031|None|-|-|-|
20240701|-|None|SoP: Unlock the Power of Social Facilitation for Automatic Jailbreak Attack|https://arxiv.org/abs/2407.01902|None|-|-|-|
20240627|-|None|GPTFUZZER: Red Teaming Large Language Models with Auto-Generated Jailbreak Prompts|https://arxiv.org/abs/2309.10253|None|-|-|-|
20240626|-|None|Poisoned LangChain: Jailbreak LLMs by LangChain|https://arxiv.org/abs/2406.18122|None|-|-|-|
20240621|-|None|From LLMs to MLLMs: Exploring the Landscape of Multimodal Jailbreaking|https://arxiv.org/abs/2406.14859|None|-|-|-|
20240620|-|None|Mitigating Fine-tuning based Jailbreak Attack with Backdoor Enhanced Safety Alignment|https://arxiv.org/abs/2402.14968|None|-|-|-|
20240619|-|None|Lockpicking LLMs: A Logit-Based Jailbreak Using Token-level Manipulation|https://arxiv.org/abs/2405.13068|None|-|-|-|
20240618|-|None|Is the System Message Really Important to Jailbreaks in Large Language Models?|https://arxiv.org/abs/2402.14857|None|-|-|-|
20240617|-|None|JailGuard: A Universal Detection Framework for LLM Prompt-based Attacks|https://arxiv.org/abs/2312.10766|None|-|-|-|
20240617|-|None|Safety Fine-Tuning at (Almost) No Cost: A Baseline for Vision Large Language Models|https://arxiv.org/abs/2402.02207|None|-|-|-|
20240617|-|None|Knowledge-to-Jailbreak: One Knowledge Point Worth One Attack|https://arxiv.org/abs/2406.11682|None|-|-|-|
20240616|-|None|Threat Modelling and Risk Analysis for Large Language Model (LLM)-Powered Applications|https://arxiv.org/abs/2406.11007|None|-|-|-|
20240614|-|None|Defending Large Language Models Against Jailbreak Attacks via Layer-specific Editing|https://arxiv.org/abs/2405.18166|None|-|-|-|
20240613|-|None|How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States|https://arxiv.org/abs/2406.05644|None|-|-|-|
20240612|-|None|[Visual-RolePlay: Universal Jailbreak Attack on MultiModal Large Language Models via Role-playing Image Character](#visual-roleplay-universal-jailbreak-attack-on-multimodal-large-language-models-via-role-playing-image-character)|https://arxiv.org/abs/2405.20773|None|-|-|-|
20240612|-|None|RL-JACK: Reinforcement Learning-powered Black-box Jailbreaking Attack against LLMs|https://arxiv.org/abs/2406.08725|None|-|-|-|
20240611|-|None|Defending Against Alignment-Breaking Attacks via Robustly Aligned LLM|https://arxiv.org/abs/2309.14348|None|-|-|-|
20240611|-|None|SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks|https://arxiv.org/abs/2310.03684|None|-|-|-|
20240610|-|None|Making Them Ask and Answer: Jailbreaking Large Language Models in Few Queries via Disguise and Reconstruction|https://arxiv.org/abs/2402.18104|None|-|-|-|
20240609|-|None|Safety Alignment Should Be Made More Than Just a Few Tokens Deep|https://arxiv.org/abs/2406.05946|None|-|-|-|
20240607|-|None|ArtPrompt: ASCII Art-based Jailbreak Attacks against Aligned LLMs|https://arxiv.org/abs/2402.11753|None|-|-|-|
20240607|-|None|Adversarial Tuning: Defending Against Jailbreak Attacks for LLMs|https://arxiv.org/abs/2406.06622|None|-|-|-|
20240606|-|None|COLD-Attack: Jailbreaking LLMs with Stealthiness and Controllability|https://arxiv.org/abs/2402.08679|None|-|-|-|
20240606|-|None|TRAP: Targeted Random Adversarial Prompt Honeypot for Black-Box Identification|https://arxiv.org/abs/2402.12991|None|-|-|-|
20240606|-|None|Defending LLMs against Jailbreaking Attacks via Backtranslation|https://arxiv.org/abs/2402.16459|None|-|-|-|
20240606|-|None|AutoJailbreak: Exploring Jailbreak Attacks and Defenses through a Dependency Lens|https://arxiv.org/abs/2406.03805|None|-|-|-|
20240605|-|None|[Improved Techniques for Optimization-Based Jailbreaking on Large Language Models](#improved-techniques-for-optimization-based-jailbreaking-on-large-language-models)|https://arxiv.org/abs/2405.21018|None|-|-|-|
20240603|-|None|Fundamental Limitations of Alignment in Large Language Models|https://arxiv.org/abs/2304.11082|None|-|-|-|
20240603|-|None|On Prompt-Driven Safeguarding for Large Language Models|https://arxiv.org/abs/2401.18018|None|-|-|-|
20240603|-|None|Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast|https://arxiv.org/abs/2402.08567|None|-|-|-|
20240531|-|None|Exploring Vulnerabilities and Protections in Large Language Models: A Survey|https://arxiv.org/abs/2406.00240|None|-|-|-|
20240530|-|None|GUARD: Role-playing to Generate Natural-language Jailbreakings to Test Guideline Adherence of Large Language Models|https://arxiv.org/abs/2402.03299|None|-|-|-|
20240530|-|None|Robustifying Safety-Aligned Large Language Models through Clean Data Curation|https://arxiv.org/abs/2405.19358|None|-|-|-|
20240530|-|None|Efficient LLM-Jailbreaking by Introducing Visual Modality|https://arxiv.org/abs/2405.20015|None|-|-|-|
20240530|-|None|Defensive Prompt Patch: A Robust and Interpretable Defense of LLMs against Jailbreak Attacks|https://arxiv.org/abs/2405.20099|None|-|-|-|
20240530|-|None|Jailbreaking Large Language Models Against Moderation Guardrails via Cipher Characters|https://arxiv.org/abs/2405.20413|None|-|-|-|
20240529|-|None|GradSafe: Detecting Jailbreak Prompts for LLMs via Safety-Critical Gradient Analysis|https://arxiv.org/abs/2402.13494|None|-|-|-|
20240529|-|None|Single Image Unlearning: Efficient Machine Unlearning in Multimodal Large Language Models|https://arxiv.org/abs/2405.12523|None|-|-|-|
20240529|-|None|Voice Jailbreak Attacks Against GPT-4o|https://arxiv.org/abs/2405.19103|None|-|-|-|
20240529|-|None|AutoBreach: Universal and Adaptive Jailbreaking with Efficient Wordplay-Guided Optimization|https://arxiv.org/abs/2405.19668|None|-|-|-|
20240528|-|None|Automatic Jailbreaking of the Text-to-Image Generative AI Systems|https://arxiv.org/abs/2405.16567|None|-|-|-|
20240528|-|None|Are PPO-ed Language Models Hackable?|https://arxiv.org/abs/2406.02577|None|-|-|-|
20240525|-|None|Jailbreak and Guard Aligned Language Models with Only Few In-Context Demonstrations|https://arxiv.org/abs/2310.06387|None|-|-|-|
20240524|-|None|Hacc-Man: An Arcade Game for Jailbreaking LLMs|https://arxiv.org/abs/2405.15902|None|-|-|-|
20240523|-|None|Impact of Non-Standard Unicode Characters on Security and Comprehension in Large Language Models|https://arxiv.org/abs/2405.14490|None|-|-|-|
20240522|-|None|Flames: Benchmarking Value Alignment of LLMs in Chinese|https://arxiv.org/abs/2311.06899|None|-|-|-|
20240522|-|None|WordGame: Efficient & Effective LLM Jailbreak via Simultaneous Obfuscation in Query and Response|https://arxiv.org/abs/2405.14023|None|-|-|-|
20240517|-|None|A Comprehensive Study of Jailbreak Attack versus Defense for Large Language Models|https://arxiv.org/abs/2402.13457|None|-|-|-|
20240516|-|None|Sowing the Wind, Reaping the Whirlwind: The Impact of Editing Language Models|https://arxiv.org/abs/2401.10647|None|-|-|-|
20240515|-|None|"Do Anything Now": Characterizing and Evaluating In-The-Wild Jailbreak Prompts on Large Language Models|https://arxiv.org/abs/2308.03825|None|-|-|-|
20240514|-|None|PLeak: Prompt Leaking Attacks against Large Language Model Applications|https://arxiv.org/abs/2405.06823|None|-|-|-|
20240514|-|None|PARDEN, Can You Repeat That? Defending against Jailbreaks via Repetition|https://arxiv.org/abs/2405.07932|None|-|-|-|
20240514|-|None|SpeechGuard: Exploring the Adversarial Robustness of Multimodal Large Language Models|https://arxiv.org/abs/2405.08317|None|-|-|-|
20240514|-|None|A safety realignment framework via subspace-oriented model fusion for large language models|https://arxiv.org/abs/2405.09055|None|-|-|-|
20240510|-|None|Evaluating and Mitigating Linguistic Discrimination in Large Language Models|https://arxiv.org/abs/2404.18534|None|-|-|-|
20240507|-|None|Rethinking How to Evaluate Language Model Jailbreak|https://arxiv.org/abs/2404.06407|None|-|-|-|
20240507|-|None|Learning To See But Forgetting To Follow: Visual Instruction Tuning Makes LLMs More Prone To Jailbreak Attacks|https://arxiv.org/abs/2405.04403|None|-|-|-|
20240506|-|None|Robustness Over Time: Understanding Adversarial Examples' Effectiveness on Longitudinal Versions of Large Language Models|https://arxiv.org/abs/2308.07847|None|-|-|-|
20240502|-|None|Boosting Jailbreak Attack with Momentum|https://arxiv.org/abs/2405.01229|None|-|-|-|
20240429|-|None|Universal Jailbreak Backdoors from Poisoned Human Feedback|https://arxiv.org/abs/2311.14455|None|-|-|-|
20240421|-|None|AdvPrompter: Fast Adaptive Adversarial Prompting for LLMs|https://arxiv.org/abs/2404.16873|None|-|-|-|
20240418|-|None|Advancing the Robustness of Large Language Models through Self-Denoised Smoothing|https://arxiv.org/abs/2404.12274|None|-|-|-|
20240414|-|None|FuzzLLM: A Novel and Universal Fuzzing Framework for Proactively Discovering Jailbreak Vulnerabilities in Large Language Models|https://arxiv.org/abs/2309.05274|None|-|-|-|
20240412|-|None|Subtoxic Questions: Dive Into Attitude Change of LLM's Response in Jailbreak Attempts|https://arxiv.org/abs/2404.08309|None|-|-|-|
20240412|-|None|JailbreakLens: Visual Analysis of Jailbreak Attacks Against Large Language Models|https://arxiv.org/abs/2404.08793|None|-|-|-|
20240406|-|None|A Wolf in Sheep's Clothing: Generalized Nested Jailbreak Prompts can Fool Large Language Models Easily|https://arxiv.org/abs/2311.08268|None|-|-|-|
20240403|-|None|Learn to Disguise: Avoid Refusal Responses in LLM's Defense via a Multi-agent Attacker-Disguiser Game|https://arxiv.org/abs/2404.02532|None|-|-|-|
20240401|-|None|The Butterfly Effect of Altering Prompts: How Small Changes and Jailbreaks Affect Large Language Model Performance|https://arxiv.org/abs/2401.03729|None|-|-|-|
20240331|-|None|Fake Alignment: Are LLMs Really Aligned Well?|https://arxiv.org/abs/2311.05915|None|-|-|-|
20240327|-|None|Tricking LLMs into Disobedience: Formalizing, Analyzing, and Detecting Jailbreaks|https://arxiv.org/abs/2305.14965|None|-|-|-|
20240322|-|None|Self-Guard: Empower the LLM to Safeguard Itself|https://arxiv.org/abs/2310.15851|None|-|-|-|
20240322|-|None|Risk and Response in Large Language Models: Evaluating Key Threat Categories|https://arxiv.org/abs/2403.14988|None|-|-|-|
20240320|-|None|AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models|https://arxiv.org/abs/2310.04451|None|-|-|-|
20240319|-|None|Review of Generative AI Methods in Cybersecurity|https://arxiv.org/abs/2403.08701|None|-|-|-|
20240318|-|None|EasyJailbreak: A Unified Framework for Jailbreaking Large Language Models|https://arxiv.org/abs/2403.12171|None|-|-|-|
20240314|-|None|AdaShield: Safeguarding Multimodal Large Language Models from Structure-based Attack via Adaptive Shield Prompting|https://arxiv.org/abs/2403.09513|None|-|-|-|
20240310|-|None|Jailbreaking ChatGPT via Prompt Engineering: An Empirical Study|https://arxiv.org/abs/2305.13860|None|-|-|-|
20240310|-|None|Using Hallucinations to Bypass GPT4's Filter|https://arxiv.org/abs/2403.04769|None|-|-|-|
20240309|-|None|From Chatbots to PhishBots? -- Preventing Phishing scams created using ChatGPT, Google Bard and Claude|https://arxiv.org/abs/2310.19181|None|-|-|-|
20240308|-|None|Can LLMs Follow Simple Rules?|https://arxiv.org/abs/2311.04235|None|-|-|-|
20240304|-|None|LLMs Can Defend Themselves Against Jailbreaking in a Practical Manner: A Vision Paper|https://arxiv.org/abs/2402.15727|None|-|-|-|
20240303|-|None|Multilingual Jailbreak Challenges in Large Language Models|https://arxiv.org/abs/2310.06474|None|-|-|-|
20240302|-|None|Ignore This Title and HackAPrompt: Exposing Systemic Vulnerabilities of LLMs through a Global Scale Prompt Hacking Competition|https://arxiv.org/abs/2311.16119|None|-|-|-|
20240229|-|None|Cognitive Overload: Jailbreaking Large Language Models with Overloaded Logical Thinking|https://arxiv.org/abs/2311.09827|None|-|-|-|
20240228|-|None|Defending Large Language Models against Jailbreak Attacks via Semantic Smoothing|https://arxiv.org/abs/2402.16192|None|-|-|-|
20240227|-|None|Semantic Mirror Jailbreak: Genetic Algorithm Based Jailbreak Prompts Against Open-source LLMs|https://arxiv.org/abs/2402.14872|None|-|-|-|
20240226|-|None|DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models|https://arxiv.org/abs/2306.11698|None|-|-|-|
20240226|-|None|CodeChameleon: Personalized Encryption Framework for Jailbreaking Large Language Models|https://arxiv.org/abs/2402.16717|None|-|-|-|
20240224|-|None|PRP: Propagating Universal Perturbations to Attack Large Language Model Guard-Rails|https://arxiv.org/abs/2402.15911|None|-|-|-|
20240223|-|None|Analyzing the Inherent Response Tendency of LLMs: Real-World Instructions-Driven Jailbreak|https://arxiv.org/abs/2312.04127|None|-|-|-|
20240223|-|None|Foot In The Door: Understanding Large Language Model Jailbreaking via Cognitive Psychology|https://arxiv.org/abs/2402.15690|None|-|-|-|
20240221|-|None|Coercing LLMs to do and reveal (almost) anything|https://arxiv.org/abs/2402.14020|None|-|-|-|
20240215|-|None|A Trembling House of Cards? Mapping Adversarial Attacks against Language Agents|https://arxiv.org/abs/2402.10196|None|-|-|-|
20240213|-|None|Pandora: Jailbreak GPTs by Retrieval Augmented Generation Poisoning|https://arxiv.org/abs/2402.08416|None|-|-|-|
20240211|-|Appl. Sci. 14, 3558 (2024)|All in How You Ask for It: Simple Black-Box Method for Jailbreak Attacks|https://arxiv.org/abs/2401.09798|None|-|-|-|
20240208|-|None|Rapid Optimization for Jailbreaking LLMs via Subconscious Exploitation and Echopraxia|https://arxiv.org/abs/2402.05467|None|-|-|-|
20240205|-|None|Weak-to-Strong Jailbreaking on Large Language Models|https://arxiv.org/abs/2401.17256|None|-|-|-|
20240205|-|None|Nevermind: Instruction Override and Moderation in Large Language Models|https://arxiv.org/abs/2402.03303|None|-|-|-|
20240203|-|None|Jailbreaking Attack against Multimodal Large Language Model|https://arxiv.org/abs/2402.02309|None|-|-|-|
20240130|-|None|A Cross-Language Investigation into Jailbreak Attacks in Large Language Models|https://arxiv.org/abs/2401.16765|None|-|-|-|
20240127|-|None|Low-Resource Languages Jailbreak GPT-4|https://arxiv.org/abs/2310.02446|None|-|-|-|
20240124|-|None|MULTIVERSE: Exposing Large Language Model Alignment Problems in Diverse Worlds|https://arxiv.org/abs/2402.01706|None|-|-|-|
20240123|-|None|How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs|https://arxiv.org/abs/2401.06373|None|-|-|-|
20240122|-|None|Who is ChatGPT? Benchmarking LLMs' Psychological Portrayal Using PsychoBench|https://arxiv.org/abs/2310.01386|None|-|-|-|
20240120|-|None|Jailbreaking GPT-4V via Self-Adversarial Attacks with System Prompts|https://arxiv.org/abs/2311.09127|None|-|-|-|
20240120|-|None|InferAligner: Inference-Time Alignment for Harmlessness through Cross-Model Guidance|https://arxiv.org/abs/2401.11206|None|-|-|-|
20231220|-|None|Universal and Transferable Adversarial Attacks on Aligned Language Models|https://arxiv.org/abs/2307.15043|None|-|-|-|
20231216|-|None|Comprehensive Evaluation of ChatGPT Reliability Through Multilingual Inquiries|https://arxiv.org/abs/2312.10524|None|-|-|-|
20231214|-|None|AutoDAN: Interpretable Gradient-Based Adversarial Attacks on Large Language Models|https://arxiv.org/abs/2310.15140|None|-|-|-|
20231212|-|None|Maatphor: Automated Variant Analysis for Prompt Injection Attacks|https://arxiv.org/abs/2312.11513|None|-|-|-|
20231124|-|None|Scalable and Transferable Black-Box Jailbreaks for Language Models via Persona Modulation|https://arxiv.org/abs/2311.03348|None|-|-|-|
20231113|-|None|Language Model Unalignment: Parametric Red-Teaming to Expose Hidden Harms and Biases|https://arxiv.org/abs/2310.14303|None|-|-|-|
20231106|-|None|Detecting Language Model Attacks with Perplexity|https://arxiv.org/abs/2308.14132|None|-|-|-|
20231028|-|None|Probing LLMs for hate speech detection: strengths and vulnerabilities|https://arxiv.org/abs/2310.12860|None|-|-|-|
20231025|-|The Network and Distributed System Security Symposium (NDSS) 2024|MasterKey: Automated Jailbreak Across Multiple Large Language Model Chatbots|https://arxiv.org/abs/2307.08715|None|-|-|-|
20231019|-|None|[Automatic Prompt Optimization with "Gradient Descent" and Beam Search](#automatic-prompt-optimization-with-gradient-descent-and-beam-search)|https://arxiv.org/abs/2305.03495|None|-|-|-|
20231016|-|None|Survey of Vulnerabilities in Large Language Models Revealed by Adversarial Attacks|https://arxiv.org/abs/2310.10844|None|-|-|-|
20231010|-|None|Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation|https://arxiv.org/abs/2310.06987|None|-|-|-|
20231005|-|None|Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!|https://arxiv.org/abs/2310.03693|None|-|-|-|
20231003|-|None|Can Language Models be Instructed to Protect Personal Information?|https://arxiv.org/abs/2310.02224|None|-|-|-|
20230904|-|None|Baseline Defenses for Adversarial Attacks Against Aligned Language Models|https://arxiv.org/abs/2309.00614|None|-|-|-|
20230828|-|None|Latent Jailbreak: A Benchmark for Evaluating Text Safety and Output Robustness of Large Language Models|https://arxiv.org/abs/2307.08487|None|-|-|-|
20230824|-|None|Self-Deception: Reverse Penetrating the Semantic Firewall of Large Language Models|https://arxiv.org/abs/2308.11521|None|-|-|-|
20230820|-|None|Using Large Language Models for Cybersecurity Capture-The-Flag Challenges and Certification Questions|https://arxiv.org/abs/2308.10443|None|-|-|-|
20230816|-|None|Visual Adversarial Examples Jailbreak Aligned Large Language Models|https://arxiv.org/abs/2306.13213|None|-|-|-|
20230705|-|None|Jailbroken: How Does LLM Safety Training Fail?|https://arxiv.org/abs/2307.02483|None|-|-|-|

