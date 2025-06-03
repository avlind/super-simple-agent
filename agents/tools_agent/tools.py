#  Copyright (C) 2025 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import uuid

def flip_a_coin() -> str:
    """Simulates flipping a coin, returning either "Heads" or "Tails".

    Returns:
        A string indicating the the result of the coin flip.
        Example: 'Heads'
    """

    # simulate flipping a coin with equal probability of heads or tails
    result = "Heads" if uuid.uuid4().int % 2 == 0 else "Tails"
    return result


def roll_die(die_sides: int) -> str:
    """Simulates rolling a single die, the total number of sides is provided as an input to the function.

    Returns:
        A string indicating the the result of the roll of a die.
        Example: '8'
    """

    # simulate rolling a die based on the number of sides
    result = str(uuid.uuid4().int % die_sides)
    return result