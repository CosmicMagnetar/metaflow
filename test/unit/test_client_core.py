import unittest
from metaflow.client.core import Metaflow, MetaflowData

class TestClientCore(unittest.TestCase):
    # Setup objects for testing
    def setUp(self):
        # We pass an empty list [] so the MetaflowData constructor can iterate
        self.data = MetaflowData([]) 
        
        # Manually add fake artifacts to simulate a Metaflow Task run
        self.data._artifacts = {
            'secret_artifact': 'found me!',
            'score': 0.95,
            'name': 'start_step'
        }
        self.mf = Metaflow()

    # Test if artifacts show up in dir() for tab-completion
    def test_metaflow_data_dir_discovery(self):
        directory = dir(self.data)
        
        # Check that our dynamic artifacts are visible to dir()
        self.assertIn('secret_artifact', directory)
        self.assertIn('score', directory)
        self.assertIn('name', directory)
        
        # Check that standard internal attributes are still there
        self.assertIn('_artifacts', directory)

    # Ensure internal variables stay hidden from the user
    def test_metaflow_data_internal_filtering(self):
        directory = dir(self.data)
        
        # Internal state should not be exposed in the autocomplete menu
        self.assertNotIn('_success', directory)
        self.assertNotIn('_task_ok', directory)

    # Test the hook used for bracket completion on Metaflow()
    def test_metaflow_bracket_completion_hook(self):
        # This hook must exist on the Metaflow class specifically
        self.assertTrue(hasattr(self.mf, '_ipython_key_completions_'), 
                        "Hook missing from Metaflow class. Check your placement in core.py!")
        
        # The hook should return a list of Flow IDs
        self.assertIsInstance(self.mf._ipython_key_completions_(), list)

if __name__ == '__main__':
    unittest.main()