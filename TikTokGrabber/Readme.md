# Link Grabber

## Idea
Loads all Tiktok links from ``list.txt`` and writes the cleaned list to ``output.txt``. 


## Code
```python
#!/usr/bin/python
output = open("output.txt", "w")
file = open("list.txt", "r")
for line in file:
    if "/video/" in line:
        output.write(f"{line}")
file.close()
output.close()
```

