# test_oracleforge.py
"""
Tests for OracleForge module.
"""

import unittest
from oracleforge import OracleForge

class TestOracleForge(unittest.TestCase):
    """Test cases for OracleForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OracleForge()
        self.assertIsInstance(instance, OracleForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OracleForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
