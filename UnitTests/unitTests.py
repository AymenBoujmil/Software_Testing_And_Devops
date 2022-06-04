import sqlite3
from unittest import TestCase, main
from unittest.mock import patch
import NotesRepo


class testShowAllNotes(TestCase):
    @patch("NotesRepo.sqlite3")
    def test_Show_Notes(self, mocked_object):
        # Given
        mocked_object.connect().cursor().fetchall.return_value = [(0, "note1", "note1 details"),
                                                                  (1, "note2", "note2 details")]
        expected_notes = [(0, "note1", "note1 details"), (1, "note2", "note2 details")]
        # When
        result_notes = NotesRepo.fetchAll()
        # Then
        self.assertEqual(expected_notes, result_notes)


class testNumberOfNotes(TestCase):
    def test_Number_Notes(self):
        # Given
        notes = [1, 2, 3, 4, 5]
        expected_Result = 5

        # When
        result_Number = NotesRepo.notesNumber(notes)
        # Then
        self.assertEqual(expected_Result, result_Number)


class testShowNoteById(TestCase):
    @patch("NotesRepo.sqlite3")
    def test_Show_Note_id(self, mocked_object):
        # Given
        mocked_object.connect().cursor().fetchone.return_value = (0, "note1", "note1 details")
        expected_note = (0, "note1", "note1 details")
        # When
        result_note = NotesRepo.fetchone(0)
        # Then
        self.assertEqual(expected_note, result_note)


class TestAddNote(TestCase):
    @patch("NotesRepo.sqlite3")
    def test_Add_Note(self, mocked_object):
        # Given
        mock_execute = mocked_object.connect.return_value.cursor.return_value.execute
        # When
        NotesRepo.noteAdd('note', ' note Details')
        # Then
        mock_execute.assert_called_once()


class TestUpdateNote(TestCase):
    @patch("NotesRepo.sqlite3")
    def test_Update_Note(self, mocked_object):
        # Given
        mock_execute = mocked_object.connect.return_value.cursor.return_value.execute
        # When
        NotesRepo.noteUpdate(0, 'note', 'note Details')
        # Then
        mock_execute.assert_called_once()


class TestDelete(TestCase):
    @patch("NotesRepo.sqlite3")
    def test_deleteProduct(self, mocked_object):
        # Given
        mock_execute = mocked_object.connect.return_value.cursor.return_value.execute
        # When
        NotesRepo.noteDelete(0)
        # Then
        mock_execute.assert_called_once()


if __name__ == '__main__':
    main()
