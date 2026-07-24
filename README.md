# ანტიმიკრობული პეპტიდების გენერაცია ლატენტური დიფუზორით

საბაკალავრო ნაშრომი ანტიმიკრობული პეპტიდების (AMP) გენერაციაზე.

## რეპოზიტორიის სტრუქტურა

| საქაღალდე          | შიგთავსი                                                                     |
| ------------------- | ----------------------------------------------------------------------------- |
| `notebooks/`        | სრული პაიპლაინი, notebook-ები                            |
| `src/`               | გამოსაყენებელი კოდი: TransVAE მოდელი და დამხმარე ფუნქციები (`utils`)         |
| `data/raw/`          | საწყისი ცხრილები (DBAASP MIC წყვილები, GRAMPA, non-AMP მიმდევრობები და სხვ.) |
| `data/processed/`    | გასუფთავებული CSV-ები, MIC leveling ლეიბლები და ენკოდირებული ლატენტები       |
| `checkpoints/`       | VAE-ს და დიფუზორის წონები                                                    |
| `results/`           | გენერირებული პეპტიდები და შედარების ცხრილები                                 |
| `configs/`           | ექსპერიმენტების YAML შენიშვნები                                              |
| `requirements.txt`   | Python გარემოს dependency-ები                                                |

TransVAE-ს დამატებით სჭირდება ეს ორი ფაილი `data/` საქაღალდიდან:

- `data/peptide_vocab.pkl`
- `data/peptide_weight.npy`

სრული პაიპლაინი მოცემულია `notebooks/` საქაღალდეში, თითოეული notebook იწყება path-setup უჯრით, რომელიც რეპოზიტორიის root-ს ამატებს `sys.path`-ში და `src/`-დან shared კოდს აიმპორტებს. თუ Colab-ზე მუშაობთ, დააყენეთ `ROOT` თქვენს clone/Drive path-ზე სანამ დანარჩენ cell-ებს გაუშვებთ.

## Configs

ცალკეული ექსპერიმენტების პარამეტრები აღწერილია `configs/`-ში YAML ფაილების სახით, თითოეული `default.yaml`-ს იყენებს საერთო პარამეტრებისთვის და მხოლოდ ექსპერიმენტისთვის სპეციფიკურ მონაცემებს (data path-ები, checkpoint-ები, generation პარამეტრები) ამატებს. მაგალითად, `configs/baumannii_enterica.yaml` აღწერს *A. baumannii* + *S. enterica* organism-conditional ექსპერიმენტს.

## Requirements

**Core:**

- python >= 3.9
- numpy>=1.23,<2.0, pandas>=1.5
- torch>=2.0
- matplotlib>=3.7, seaborn>=0.13
- tqdm>=4.65
- scikit-learn==1.2.2

**Bioinformatics / peptides:**

- biopython>=1.81
- peptides>=0.3

**Optional:**

- wandb>=0.16 — experiment tracking
- transformers>=4.36, gdown>=5.0 — only needed for `notebooks/05_evaluation_pipeline.ipynb`
- toxinpred3, amplify — installed/cloned separately from within the evaluation notebook when needed

## გამოყენებული წყარო

Wang, Y., et al. (2024). PepDiffusion: De novo peptide design via latent diffusion models. *Science Advances*, 10(xx), eadp7171. https://doi.org/10.1126/sciadv.adp7171

კვლევის ექსპერიმენტული ნაწილისა და იმპლემენტაციისთვის საბაზისო არქიტექტურად გამოყენებულია PepDiffusion-ის ოფიციალური ღია რეპოზიტორია: https://github.com/Wangyj2023/PepDiffusion

ამინომჟავური მიმდევრობების ლატენტური სივრცის სწავლებისთვის განკუთვნილი `TransVAE.py` მოდული ინტეგრირებულია უცვლელი სახით, ხოლო ლატენტური დიფუზორის training-ისა და პეპტიდების გენერაციის სკრიპტები მოდიფიცირებულია და ადაპტირებულია ჩვენი კონკრეტული ექსპერიმენტული ამოცანების სპეციფიკის გათვალისწინებით.
