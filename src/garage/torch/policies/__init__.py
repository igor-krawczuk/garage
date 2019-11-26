"""PyTorch Policies."""
from garage.torch.policies.base import Policy
from garage.torch.policies.deterministic_mlp_policy import (
    DeterministicMLPPolicy)
from garage.torch.policies.gaussian_mlp_policy import GaussianMLPPolicy
from garage.torch.policies.tanh_gaussian_mlp_policy import TanhGaussianMLPPolicy
from garage.torch.policies.tanh_gaussian_mlp_policy_2 import TanhGaussianMLPPolicy2


__all__ = ['DeterministicMLPPolicy', 'GaussianMLPPolicy', 'Policy', 'TanhGaussianMLPPolicy', 'TanhGaussianMLPPolicy2']
