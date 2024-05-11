# Virtual environment settings
VENV_DIR = .venv
VENV_ACTIVATE = $(VENV_DIR)/bin/activate

# Python interpreter (adjust if necessary)
PYTHON = python3

# Install dependencies
install:
	pip install -r requirements.txt

# Create virtual environment
venv:
	python3 -m venv $(VENV_DIR)

# Activate virtual environment
activate:
	@echo "Activating virtual environment..."
	@source $(VENV_ACTIVATE)

# Run scenario 1
scenario1:
	$(PYTHON) scenario1.py

# Run scenario 2
scenario2:
	$(PYTHON) scenario2.py

# Run scenario 3
scenario3:
	$(PYTHON) scenario3.py

# Run main program
main:
	$(PYTHON) main.py

# Clean up generated files
clean:
	rm -rf $(VENV_DIR) __pycache__ *.pyc

# Help message
help:
	@echo "Usage: make [target]"
	@echo "Targets:"
	@echo "  install     Install dependencies"
	@echo "  venv        Create virtual environment"
	@echo "  activate    Activate virtual environment"
	@echo "  scenario1   Run scenario 1"
	@echo "  scenario2   Run scenario 2"
	@echo "  scenario3   Run scenario 3"
	@echo "  main        Run main program"
	@echo "  clean       Clean up generated files"
	@echo "  help        Show this help message"
