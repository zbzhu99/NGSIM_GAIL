from smarts.core.agent import AgentSpec
from smarts.core.agent_interface import AgentInterface
from smarts.core.controllers import ActionSpaceType

from smarts_imitation.utils import adapter


def get_agent_spec(neighbor_mode: str = "LANE", neighbor_num: int = 6):
    agent_spec = AgentSpec(
        interface=AgentInterface(
            max_episode_steps=None,
            waypoints=True,
            neighborhood_vehicles=True,
            ogm=False,
            rgb=False,
            lidar=False,
            action=ActionSpaceType.Imitation,
        ),
        observation_adapter=adapter.get_observation_adapter(
            neighbor_mode=neighbor_mode,
            neighbor_num=neighbor_num,
        ),
        action_adapter=adapter.get_action_adapter(),
    )

    return agent_spec
