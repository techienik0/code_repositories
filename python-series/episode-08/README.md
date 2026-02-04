# Episode 8: File Handling (Read/Write Real Data)

## 📖 Description

Learn to read and write real files on your computer - text files, CSV files, and JSON files. This is where your code meets the real world!

## 🎯 Learning Outcomes

- Read and write text files using `with` statements
- Understand file modes (read 'r', write 'w', append 'a')
- Work with CSV files using the `csv` module
- Handle JSON files for data storage
- Avoid common file handling mistakes

## 💻 Code Examples

See `main.py` for all examples from this episode, including:
- Reading files (the right way with `with` statements)
- Writing files (write vs append mode)
- Working with CSV files (csv.reader, csv.DictReader)
- Working with JSON files (json.load, json.dump)
- Common mistakes and how to avoid them

## 🎓 Project

See `project.py` for the Personal Diary App - a practical application that saves your diary entries to a JSON file and lets you search, view, and export them.

## ⚠️ Common Mistakes

1. **Forgetting to close files** - Always use `with` statement!
2. **Using wrong file path** - Know where your file is (current directory vs absolute path)
3. **Not handling FileNotFoundError** - Files might not exist, handle it!
4. **Opening file in wrong mode** - 'w' overwrites, 'a' appends - know the difference!
5. **Not including newline characters** - Use `\n` when writing multiple lines
6. **Parsing CSV manually** - Use the `csv` module, don't use `split(",")`!

## 💡 Key Concepts

- **File modes**: 'r' (read), 'w' (write/overwrite), 'a' (append)
- **with statement**: Automatically closes files, even if errors occur
- **CSV module**: Handles commas, quotes, and edge cases properly
- **JSON**: Python's `json` module converts between JSON and Python dictionaries
- **File paths**: Relative (current directory) vs absolute (full path)

## 🔥 Pro Tips

- Always use `with` statements for file operations
- Use `csv.DictReader` instead of `csv.reader` for better readability
- Use `indent=4` in `json.dump()` to make JSON files readable
- Handle `FileNotFoundError` when reading files
- Use append mode ('a') when you're not sure if file exists
