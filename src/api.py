from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

from src.bodmas_calc import Bodmas

calculator = Bodmas()


class CalculatorHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        parsed_url = urlparse(self.path)

        if parsed_url.path == "/health":

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(
                b'{"status":"unhealthy"}'
            )

        elif parsed_url.path == "/calculate":

            query = parse_qs(parsed_url.query)
            expression = query.get("expression", [None])[0]

            if expression is None:

                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                self.wfile.write(
                    b'{"error":"expression is required"}'
                )

                return

            try:

                result = calculator.calculate(expression)

                response = (
                    f'{{"result":{result}}}'
                ).encode()

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                self.wfile.write(response)

            except (ValueError, ZeroDivisionError, IndexError):

                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                self.wfile.write(
                    b'{"error":"invalid expression"}'
                )

        else:

            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(
                b'{"error":"not found"}'
            )


if __name__ == "__main__":

    server = HTTPServer(
        ("0.0.0.0", 8080),
        CalculatorHandler
    )

    print("Calculator API running on port 8080")

    server.serve_forever()
