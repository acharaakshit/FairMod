# 🛡️ AI Safety Moderation Classifier Evaluation

## 📜 Overview

This repository provides Jupyter notebooks for evaluating closed-source text-based AI safety moderation classifiers. The focus is on analyzing how these classifiers handle content related to various protected groups.

## 📚 Contents

- **`preprocessing.ipynb`**: 📥 Downloads a large dataset and creates sub-datasets for protected groups.
- **`augmentations.ipynb`**: 🔄 Demonstrates backtranslation of texts from English to German and back to English for data augmentation or robustness testing.
- **`uniformRandomClassifier.ipynb`**: ⚖️ Provides a fairness baseline by assigning safe or unsafe outcomes with equal probability.
- **`moderationGPT.ipynb`**: Obtains moderation results using the OpenAI ASM.
- **`clarifaiModeration.ipynb`**: Obtains moderation results using the Clarifai ASM.
- **`perspectiveModeration.ipynb`**: Obtains moderation results using the Google Perspective ASM.
- **`googleModeration.ipynb`**: Obtains moderation results using the Google PaLM2 based ASM.
- **`fairnessComputation.ipynb`**: ⚖️ Performs a comparative fairness analysis on the ASMs using demographic parity and conditional statistical parity metrics.
- **`robustness.ipynb`**: 🛠️ Performs robustness analysis on the ASMs using input perturbation techniques like backtranslations and paraphrasing.
- **`process_raw_robustness_results.ipynb`**: 🧹 Processes moderation outputs to obtain binary results (safe/unsafe). If moderation results are unavailable, processed outputs can be directly loaded from the results folder.
- **`microrobustness.ipynb`**: Conducts deeper robustness analysis, computing the percentage of safe-to-unsafe and unsafe-to-safe transitions for all ASMs.
- **`regard.ipynb`**: Performs regard sentiment analysis, classifying input texts into "positive," "negative," "neutral," and "other" categories.
- **`voyage.ipynb`**: Obtains text embeddings using the voyage-large-2-instruct model.

## 🚀 Usage

1. **Data Preprocessing**: Run `preprocessing.ipynb` to download and prepare datasets.
2. **Data Augmentation**: Use `augmentations.ipynb` for backtranslations.
3. **Fairness Baseline**: Execute `uniformRandomClassifier.ipynb` for a fairness baseline.
4. **Text Embeddings**: Run `voyage.ipynb` for embeddings using the voyage-large-2-instruct model.
5. **Moderation Results**: Use the following notebooks to obtain moderation results:
   - `moderationGPT.ipynb` for OpenAI ASM
   - `clarifaiModeration.ipynb` for Clarifai ASM
   - `perspectiveModeration.ipynb` for Google Perspective ASM
   - `googleModeration.ipynb` for Google PaLM2 based ASM
6. **Fairness Analysis**: Use `fairnessComputation.ipynb` to perform a comparative fairness analysis on the ASMs.
7. **Robustness Analysis**:
   - Use `robustness.ipynb` to analyze the robustness of the ASMs using perturbation techniques.
   - Use `microrobustness.ipynb` for a deeper analysis of safe-to-unsafe and unsafe-to-safe transitions.
8. **Processing Results**: Use `process_raw_robustness_results.ipynb` to convert moderation outputs into binary safe/unsafe results. If moderation outputs are not available, load processed results directly from the results folder.
9. **Sentiment Analysis**: Run `regard.ipynb` to classify input texts into "positive," "negative," "neutral," and "other" sentiment classes.

## 🛡️ Protected Groups

The repository includes considerations for:

- 🧠 Ideology
- 🚺 Gender
- 🌍 Race
- ♿ Disability
- 🌈 Sexual Orientation

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## 📜 License

Licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Citation

If you use our code for your research, please cite our paper:

```
@article{achara2025watching,
  title={Watching the AI Watchdogs: A Fairness and Robustness Analysis of AI Safety Moderation Classifiers},
  author={Achara, Akshit and Chhabra, Anshuman},
  journal={arXiv preprint arXiv:2501.13302},
  year={2025}
}
```
