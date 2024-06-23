"""
Handles the generation of an HTML document for the market research report. This module converts the
compiled market research content into a well-formatted HTML file, suitable for presentation or
distribution. It includes styles and structure to enhance readability and presentation quality.
"""

def generate_html(report_content):
    html_output = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Comprehensive Market Research: Martial Arts Gym Software</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background-color: #f4f4f4;
            }}
            .container {{
                background-color: white;
                padding: 40px;
                border-radius: 8px;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 2px solid #3498db;
                padding-bottom: 10px;
                font-size: 2.5em;
            }}
            h2 {{
                color: #34495e;
                margin-top: 30px;
                font-size: 1.8em;
            }}
            h3 {{
                color: #2980b9;
                font-size: 1.4em;
            }}
            .section {{
                margin-bottom: 40px;
            }}
            .highlight {{
                background-color: #e8f4f8;
                border-left: 5px solid #3498db;
                padding: 20px;
                margin: 20px 0;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
            }}
            th, td {{
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }}
            th {{
                background-color: #f2f2f2;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Market Research: Martial Arts Gym Software</h1>
            <div class="section">
                {report_content}
            </div>
        </div>
    </body>
    </html>
    """
    return html_output