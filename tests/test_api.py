"""Integration tests for Flask API."""

import pytest

from main import create_app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


class TestFlaskAPI:
    """Tests for the Flask API."""

    def test_index_page(self, client):
        """Test that index page loads."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Calculator' in response.data

    def test_calculate_simple_addition(self, client):
        """Test simple addition via API."""
        response = client.post(
            '/calculate',
            json={'expression': '1 + 2'},
            content_type='application/json',
        )
        assert response.status_code == 200
        assert response.json['result'] == 3

    def test_calculate_subtraction(self, client):
        """Test subtraction via API."""
        response = client.post(
            '/calculate',
            json={'expression': '5 - 3'},
            content_type='application/json',
        )
        assert response.status_code == 200
        assert response.json['result'] == 2

    def test_calculate_multiplication(self, client):
        """Test multiplication via API."""
        response = client.post(
            '/calculate',
            json={'expression': '3 * 4'},
            content_type='application/json',
        )
        assert response.status_code == 200
        assert response.json['result'] == 12

    def test_calculate_division(self, client):
        """Test division via API."""
        response = client.post(
            '/calculate',
            json={'expression': '10 / 2'},
            content_type='application/json',
        )
        assert response.status_code == 200
        assert response.json['result'] == 5

    def test_calculate_power(self, client):
        """Test power operation via API."""
        response = client.post(
            '/calculate',
            json={'expression': '2 ** 3'},
            content_type='application/json',
        )
        assert response.status_code == 200
        assert response.json['result'] == 8

    def test_calculate_sqrt(self, client):
        """Test square root via API."""
        response = client.post(
            '/calculate',
            json={'expression': 'sqrt(9)'},
            content_type='application/json',
        )
        assert response.status_code == 200
        assert response.json['result'] == 3

    def test_calculate_complex_expression(self, client):
        """Test complex expression via API."""
        response = client.post(
            '/calculate',
            json={'expression': '(1 + 2) * 3 - 4'},
            content_type='application/json',
        )
        assert response.status_code == 200
        assert response.json['result'] == 5

    def test_calculate_with_precedence(self, client):
        """Test operator precedence via API."""
        response = client.post(
            '/calculate',
            json={'expression': '2 + 3 * 4'},
            content_type='application/json',
        )
        assert response.status_code == 200
        assert response.json['result'] == 14

    def test_missing_expression(self, client):
        """Test that missing expression returns error."""
        response = client.post(
            '/calculate',
            json={},
            content_type='application/json',
        )
        assert response.status_code == 400
        assert 'error' in response.json

    def test_invalid_expression(self, client):
        """Test that invalid expression returns error."""
        response = client.post(
            '/calculate',
            json={'expression': 'not a valid expression'},
            content_type='application/json',
        )
        assert response.status_code == 400
        assert 'error' in response.json

    def test_division_by_zero_error(self, client):
        """Test that division by zero returns error."""
        response = client.post(
            '/calculate',
            json={'expression': '5 / 0'},
            content_type='application/json',
        )
        assert response.status_code == 400
        assert 'divide by zero' in response.json['error'].lower()

    def test_sqrt_negative_error(self, client):
        """Test that sqrt of negative returns error."""
        response = client.post(
            '/calculate',
            json={'expression': 'sqrt(-4)'},
            content_type='application/json',
        )
        assert response.status_code == 400
        assert 'square root' in response.json['error'].lower()

    def test_cors_headers(self, client):
        """Test that CORS headers are present."""
        response = client.get('/')
        assert 'Access-Control-Allow-Origin' in response.headers
        assert response.headers['Access-Control-Allow-Origin'] == '*'

    def test_calculate_floats(self, client):
        """Test calculations with floats."""
        response = client.post(
            '/calculate',
            json={'expression': '1.5 + 2.5'},
            content_type='application/json',
        )
        assert response.status_code == 200
        assert response.json['result'] == 4.0

    def test_calculate_unary_minus(self, client):
        """Test unary minus operator."""
        response = client.post(
            '/calculate',
            json={'expression': '-5 + 3'},
            content_type='application/json',
        )
        assert response.status_code == 200
        assert response.json['result'] == -2
