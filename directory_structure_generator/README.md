# Directory Structure Generator Script

## Description

This script is used to generate a list of the project structure in a markdown format. It is useful for README.md files.

## Usage

### Files

- `directory_structure_generator.py` : Python script to generate the project structure list
- `README.md` : Markdown file to display the project structure list
- `Structures.md` : Markdown file to display the project structure list
- `exclude.txt` : Text file to exclude the files and folders from the project structure list

### pre-execution

- Update the `exclude.txt` file with the files and folders to exclude from the project structure list

### Command

```bash
python3 directory_structure_generator.py --path <path> --language <language> --sort <sort>
```

### Arguments

- `--path` : Path to the project folder
- `--language` : Language of the project. Default is `plaintext`
- `--sort` : Sort the folders and files. Default is `False`

### Example

```bash
python3 directory_structure_generator.py --path backend-python-training-feb-24 --language python --sort True
```

## Output

### frontend-training-mp-feb24 folder structure

```js
📁 frontend-training-mp-feb24
├───📄 App.js
├───📄 AppStyles.js
├───📄 README.md
├───📄 app.json
├───📁 assets
│   ├───📄 Error_image.png
│   ├───📄 adaptive-icon.png
│   ├───📄 favicon.png
│   ├───📄 icon.png
│   └───📄 splash.png
├───📄 babel.config.js
├───📄 metrics.js
├───📄 package-lock.json
├───📄 package.json
├───📁 src
│   ├───📁 components
│   │   ├───📁 Card
│   │   │   ├───📄 Card.jsx
│   │   │   ├───📄 Counter.jsx
│   │   │   └───📄 index.jsx
│   │   ├───📁 Cart
│   │   │   ├───📄 CardProduct.jsx
│   │   │   ├───📄 CartProducts.jsx
│   │   │   ├───📄 CartSummary.jsx
│   │   │   └───📄 index.jsx
│   │   ├───📁 Error
│   │   │   ├───📄 Error.jsx
│   │   │   └───📄 index.jsx
│   │   └───📄 index.jsx
│   ├───📁 redux
│   │   ├───📄 cartSlice.jsx
│   │   ├───📄 index.jsx
│   │   └───📄 productSlice.jsx
│   ├───📁 screens
│   │   ├───📁 CartScreen
│   │   │   ├───📄 CartScreen.jsx
│   │   │   └───📄 index.jsx
│   │   ├───📁 HomeScreen
│   │   │   ├───📄 HomeScreen.jsx
│   │   │   └───📄 index.jsx
│   │   └───📄 index.jsx
│   └───📁 services
│   │   ├───📄 api.js
│   │   ├───📄 cartService.js
│   │   └───📄 productService.js
└───📄 yarn.lock
```

### How to use the script

1. Open the terminal
2. Navigate to the folder where the script is located
3. Run the script with the required arguments
4. Copy the output and paste it in the README.md file
5. Commit the changes
6. Push the changes to the repository
7. Check the README.md file in the repository
8. The project structure will be displayed in the markdown format

### How to get the script

1. Clone the repository

    ```bash
    git clone git@github.com:7oSkaaa/directory_structure_generator.git
    ```

2. Navigate to the folder where the script is located
3. Run the script with the required arguments
4. Copy the output and paste it in the README.md file
