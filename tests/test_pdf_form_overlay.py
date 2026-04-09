from pathlib import Path

import pdf_form_tools.pdf_form_overlay as overlay
from pdf_form_tools import Rect, centered_address_box


def test_rect_inset() -> None:
    assert Rect(10, 20, 30, 40).inset(5) == Rect(15, 25, 20, 30)


def test_centered_address_box() -> None:
    rect = Rect(100, 200, 400, 120)
    assert centered_address_box(rect, top_pad=10, side_pad=20, height=50) == Rect(120, 210, 360, 50)


def test_load_font_uses_existing_system_font() -> None:
    font = overlay.load_font(18, bold=False)
    assert font is not None
    assert Path(overlay.resolve_font_path()).exists()


def test_contains_hebrew_detects_hebrew_characters() -> None:
    assert overlay.contains_hebrew("אמילי")
    assert not overlay.contains_hebrew("Emily")
