# hooks/pre_gen_project.py
def validate_slug(slug):
    import re
    if not re.match(r'^[_a-zA-Z][_a-zA-Z0-9]+$', slug):
        raise ValueError(
            f"Invalid project_slug '{slug}'. It must be a valid Python identifier."
        )

def main():
    import sys
    slug = '{{ cookiecutter.project_slug }}'
    try:
        validate_slug(slug)
    except ValueError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()