"""Base games and the Gamma -> Gamma(k, s, rho) transformation.

Importing this package registers the Python games with OpenSpiel.
"""

from games import card_guessing  # noqa: F401
from games import card_blocker  # noqa: F401
from games import suit_blocker  # noqa: F401
from games import coordinated_attack  # noqa: F401
from games import team_liars_dice  # noqa: F401
from games import augment  # noqa: F401
