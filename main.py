#!/usr/bin/env python3
"""Flask calculator server and CLI interface."""

import argparse
import os
import sys

from flask import Flask, request, jsonify, send_file

from expression_parser import ExpressionParser


def create_app() -> Flask:
    """Create and configure the Flask application.

    Returns:
        Flask: Configured Flask app instance
    """
    app = Flask(__name__, static_folder='UI', static_url_path='/')
    parser = ExpressionParser()

    @app.route('/', methods=['GET'])
    def index():
        """Serve the calculator HTML UI."""
        return send_file('UI/index.html')

    @app.route('/calculate', methods=['POST'])
    def calculate():
        """Handle calculation requests via HTTP.

        Expected JSON body:
            { "expression": "1 + 2 * 3" }

        Returns:
            JSON: { "result": float } or { "error": str }
        """
        try:
            data = request.get_json()
            if not data or 'expression' not in data:
                return jsonify({'error': 'Missing expression in request'}), 400

            expression = data['expression']
            result = parser.parse(expression)
            return jsonify({'result': result})

        except ValueError as e:
            return jsonify({'error': str(e)}), 400
        except Exception as e:
            return jsonify({'error': f'Calculation error: {str(e)}'}), 500

    @app.after_request
    def handle_cors(response):
        """Handle CORS headers manually."""
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

    return app


def main() -> None:
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description='Python OOP Calculator')
    parser.add_argument(
        'expression',
        nargs='?',
        help='Expression to calculate (e.g., "1 + 2 - 4")',
    )
    parser.add_argument(
        '--server',
        action='store_true',
        help='Start Flask server on port 9090',
    )

    args = parser.parse_args()

    # If expression provided, calculate and exit
    if args.expression:
        try:
            calc_parser = ExpressionParser()
            result = calc_parser.parse(args.expression)
            print(result)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    # If --server flag or no expression, start the server
    elif args.server or not args.expression:
        app = create_app()
        print("Starting Flask server on http://localhost:9090")
        print("Press Ctrl+C to stop the server")
        app.run(host='0.0.0.0', port=9090, debug=False)


if __name__ == '__main__':
    main()
