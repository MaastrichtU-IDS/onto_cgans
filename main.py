from dp_cgans import DP_CGAN
import pandas as pd

tabular_data = pd.read_csv("../persistent/data/ontology/syn_patients_data_unseen_names.txt", names=["patient_id", "rare_disease", "phenotype"])

# We adjusted the original CTGAN model from SDV. Instead of looking at the distribution of individual variable, we extended to two variables and keep their corrll
model = DP_CGAN(
    epochs=2, # number of training epochs
    batch_size=1000, # the size of each batch
    log_frequency=True,
    verbose=True,
    generator_dim=(128, 128, 128),
    discriminator_dim=(128, 128, 128),
    generator_lr=2e-4,
    discriminator_lr=2e-4,
    discriminator_steps=1,
    private=False,
)

print("Start training model")
model.fit(tabular_data)

# Sample the generated synthetic data
model.sample(100)
