LDFLAGS := -L/opt/homebrew/opt/libffi/lib
CPPFLAGS := -I/opt/homebrew/opt/libffi/include
PKG_CONFIG_PATH := /opt/homebrew/opt/libffi/lib/pkgconfig

init:
	echo "⚙️  Initializing Poetry project with local libffi paths..."
	LDFLAGS=$(LDFLAGS) \
	CPPFLAGS=$(CPPFLAGS) \
	PKG_CONFIG_PATH=$(PKG_CONFIG_PATH) \
	poetry install || ( \
		echo "🔁 Installing cffi manually inside the virtual environment..."; \
		. .venv/bin/activate && \
		LDFLAGS=$(LDFLAGS) CPPFLAGS=$(CPPFLAGS) PKG_CONFIG_PATH=$(PKG_CONFIG_PATH) \
		pip install --force-reinstall --no-cache-dir cffi && \
		poetry install \
	)
	LDFLAGS=$(LDFLAGS) \
	CPPFLAGS=$(CPPFLAGS) \
	PKG_CONFIG_PATH=$(PKG_CONFIG_PATH) \
	poetry run pre-commit install

git-init:
	git init
	poetry run pre-commit install
	
lint:
	poetry run ruff check .

format:
	poetry run ruff format .

test:
	poetry run pytest

run:
	poetry run python main.py