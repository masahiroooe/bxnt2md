# test_boxnote_parser.py
import unittest
from boxnote import BoxNoteParser

class TestBoxNoteParser(unittest.TestCase):
    def test_parse_json(self):
        sample_json = '''
        {
            "content": [
                {"type": "text", "text": "Sample text"},
                {"type": "paragraph", "content": "Sample paragraph"},
                {"type": "list", "items": [{"value": "Item 1"}, {"value": "Item 2"}]},
                {"type": "check_list", "items": [{"value": "Task 1", "checked": true}, {"value": "Task 2", "checked": false}]}
            ]
        }
        '''
        parser = BoxNoteParser("markdown")
        result = parser.parse_json(sample_json)
        self.assertIn("Sample text", result)
        self.assertIn("Sample paragraph", result)
        self.assertIn("1. Item 1", result)

if __name__ == "__main__":
    unittest.main()
