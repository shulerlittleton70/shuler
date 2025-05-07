Absolutely—here’s a polished first version of your README.md with clear disclaimers, project context, and usage notes. I also framed it to highlight that this is a personal initiative built to help your team and customers, not an official IBM/Apptio product.

🚀 Shuler Library: Python Helpers for Apptio CLDY & Studio APIs

🔍 What Is This?

The shuler library is a lightweight, modular Python toolkit designed to simplify common tasks when working with Apptio Cloudability (CLDY) APIs and Apptio Studio APIs. It provides a clean, structured way to authenticate, fetch cost reports, and manage business mappings, among other features.

❗ Important Disclaimer:

	This library is an independent personal development project and is not developed, maintained, or officially supported by IBM, Apptio, or the Cloudability product teams.

	It was created by [Your Name] to enhance team efficiency and improve customer experience when interacting with Apptio APIs in day-to-day operations.

🎯 Project Goals
	•	✅ Simplify repetitive API tasks (auth, cost reports, business mappings)
	•	✅ Improve productivity for internal teams & customers
	•	✅ Encourage modular, maintainable code for future growth
	•	✅ Remain lightweight & easy to use

🛠 Key Features
	•	Authentication:
	•	Get a Frontdoor token to access Apptio APIs.
	•	Cloudability (CLDY) Helpers:
	•	Cost reporting (get_cost_summary, more coming soon)
	•	Business mappings (list, get, create, update, delete)
	•	Studio Helpers:
	•	Data management (scaffolded for future expansion)


🚀 Quick Start Example

from shuler import frontdoor_auth
from shuler.cldy import cost_reports, business_mappings

# Authenticate
token = frontdoor_auth(client_id, client_secret, domain, env_id)

# Get cost summary
summary = cost_reports.get_cost_summary(token, view_id)

# Work with business mappings
all_mappings = business_mappings.get_business_mappings(token)
mapping_names = business_mappings.get_business_mapping_index(token)
specific_mapping = business_mappings.get_business_mapping(token, index)

🧪 Testing

Test stubs are included to confirm function availability:
	•	tests/cldy/test_cost_reports.py
	•	tests/cldy/test_business_mappings.py

(These will be expanded with mock API calls in upcoming versions.)

📌 Why I Built This

As part of my work supporting Apptio Cloudability & Studio implementations, I noticed a gap in developer-friendly tools that make it faster and easier to work with the APIs—both internally for my team and for the customers we serve.

This project was born out of that need:
	•	✅ Save time by abstracting repetitive API tasks.
	•	✅ Reduce friction for customers new to Cloudability’s APIs.
	•	✅ Promote consistency across use cases and environments.

⚠️ Not an Official Product

To reiterate:
	•	This library is not officially affiliated with IBM, Apptio, or Cloudability.
	•	Use it at your own risk.
	•	All API calls are made to official Apptio endpoints, but this tool is not covered by Apptio’s official support agreements.

📈 Planned Roadmap
	•	Flesh out cldy/cost_reports.py with full API coverage
	•	Add support for:
	•	Cost details
	•	View management
	•	CSV exports
	•	Expand tests with real API mocks
	•	Add examples & usage tips to the README
	•	Explore a SessionManager for automatic token handling

