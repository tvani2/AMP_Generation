"""Model definitions.

TransVAE (sequence VAE):

    from src.models.transvae import create_VAE, vae_data_gen, w2i, params

Requires ``data/peptide_vocab.pkl`` and ``data/peptide_weight.npy``.

Diffusion denoiser classes (DModel, MyDiffusion, …) still live in the
training/generation notebooks because phase-1 / phase-2 / leveled variants
differ slightly. They can be moved here later once unified.
"""
