# Rename Libary Files

## Change Path:

```python
# Path
path_dir = "."
path_dir = path_dir.replace("\\", "//")
```

## Work
- Delete annoying spaces
- Delete the appendix
- Modify the author
- Adjusting the name structure


## Example 
```python
for runner in os.listdir(path_dir):
    if not ".py" in runner:
        start = runner.find("(")
        if ".pdf" in runner:
            new_name = f"{runner[0:start]}.pdf"
        elif ".epub" in runner:
            new_name = f"{runner[0:start]}.epub"
        else:
            print(f"Error\n\t-->{runner}")
            sys.exit(0)
        os.rename(f"{path_dir}//{runner}", f"{path_dir}//{new_name}")
```