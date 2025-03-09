import unittest
from unittest.mock import Mock, patch
from docker_optimizer import DockerOptimizer

class TestDockerOptimizer(unittest.TestCase):
    @patch('docker.DockerClient')
    def setUp(self, MockDockerClient):
        self.mock_client = MockDockerClient()
        self.optimizer = DockerOptimizer(self.mock_client)

    def test_get_containers(self):
        self.optimizer.get_containers()
        self.mock_client.containers.list.assert_called_once_with(all=True)

    def test_get_container_stats(self):
        mock_container = Mock()
        self.optimizer.get_container_stats(mock_container)
        mock_container.stats.assert_called_once_with(stream=False)

    def test_update_container_config(self):
        mock_container = Mock()
        mock_config = {'Memory': 512}
        self.optimizer.update_container_config(mock_container, mock_config)
        mock_container.update.assert_called_once_with(mock_config)

if __name__ == '__main__':
    unittest.main()