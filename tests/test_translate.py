# tests/test_translate.py

from time import sleep
import unittest
import asyncio
import pytest
from cappa import command
from django_ai_translate import translate_text, async_translate_text
from django_ai_translate.po_handler import load_po_file, save_po_file, get_untranslated_entries
from tqdm.asyncio import tqdm
from yaspin import yaspin

import os

from django_ai_translate.translator import translate_in_batches

@pytest.mark.asyncio
async def test_async_translation():
        file_path = os.path.join(os.path.dirname(__file__), "tests.po")
        po = load_po_file(file_path)
        entries = get_untranslated_entries(po)
        await translate_in_batches(entries, batch_size=100, target_language="english")

        save_po_file(po, file_path)

        assert True


