# test_arthash.py
"""
Tests for ArtHash module.
"""

import unittest
from arthash import ArtHash

class TestArtHash(unittest.TestCase):
    """Test cases for ArtHash class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtHash()
        self.assertIsInstance(instance, ArtHash)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtHash()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
