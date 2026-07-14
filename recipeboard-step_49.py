# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: RecipeBoard
import pytest
from recipe_board.models import Ingredient, Recipe
from recipe_board.storage import Storage


@pytest.fixture
def storage():
    return Storage()


def test_update_nonexistent_raises(storage):
    with pytest.raises(ValueError):
        storage.update_ingredient("r1", {"name": "Updated"})


def test_delete_nonexistent_raises(storage):
    with pytest.raises(KeyError):
        storage.delete_ingredient("nonexistent")


def test_update_and_delete_recipes(storage):
    r = Recipe(name="Test", ingredients=[])
    storage.add_recipe(r)
    assert len(storage.get_all_recipes()) == 1
    storage.update_recipe(r.id, {"name": "Updated"})
    assert storage.get_recipe(r.id).name == "Updated"
    storage.delete_recipe(r.id)
