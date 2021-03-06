# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
Rocket
"""

import numbers

from ..utils.entrypoints import Component
from ..utils.utils import try_set


def rocket(
        top_k_learners=2,
        second_round_trials_per_learner=5,
        random_initialization=False,
        num_initialization_pipelines=20,
        **params):
    """
    **Description**
        AutoML engine that consists of distinct, hierarchical stages of
        operation.

    :param top_k_learners: Number of learners to retain for second
        stage. (settings).
    :param second_round_trials_per_learner: Number of trials for
        retained second stage learners. (settings).
    :param random_initialization: Use random initialization only.
        (settings).
    :param num_initialization_pipelines: Number of initilization
        pipelines, used for random initialization only. (settings).
    """

    entrypoint_name = 'Rocket'
    settings = {}

    if top_k_learners is not None:
        settings['TopKLearners'] = try_set(
            obj=top_k_learners,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if second_round_trials_per_learner is not None:
        settings['SecondRoundTrialsPerLearner'] = try_set(
            obj=second_round_trials_per_learner,
            none_acceptable=True,
            is_of_type=numbers.Real)
    if random_initialization is not None:
        settings['RandomInitialization'] = try_set(
            obj=random_initialization, none_acceptable=True, is_of_type=bool)
    if num_initialization_pipelines is not None:
        settings['NumInitializationPipelines'] = try_set(
            obj=num_initialization_pipelines,
            none_acceptable=True,
            is_of_type=numbers.Real)

    component = Component(
        name=entrypoint_name,
        settings=settings,
        kind='AutoMlEngine')
    return component
