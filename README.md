# Phone Number Generator

This script generates all possible phone numbers for specified prefixes, shuffles them, and saves the data into multiple text files. It handles large datasets by dividing the numbers into chunks and distributing them across several files to avoid memory overload.

## Features

- Generates phone numbers for multiple prefixes.
- Shuffles the generated phone numbers to ensure randomness.
- Saves the results into multiple text files, each with up to 100,000 phone numbers.
- Supports large datasets by splitting the output into smaller files for ease of storage and processing.

## Requirements

- Python 3.x
- Required libraries: `pandas`, `os`, `random`, `tqdm`

You can install `tqdm` using:

```bash
pip install tqdm
```

## Usage

### Clone the repository:

```bash
git clone https://github.com/your-username/phone-number-generator.git
cd phone-number-generator

### Run the script:

```bash
python gen_phone.py
```

The script will generate phone numbers for the following prefixes:

- `38067`
- `38096`
- `38097`
- `38098`
- `38050`
- `38099`

You can modify the prefixes by changing the `prefixes` list in the script.

The output files will be saved in the `baza_gen_phone` folder. Each file will contain up to 100,000 phone numbers, and they will be further split into subfolders with up to 1 million phone numbers.

### Example Output

```bash
baza_gen_phone/
│
├── baza_gen_phone_1/
│   ├── baza_gen_phone_1.txt
│   ├── baza_gen_phone_2.txt
│   └── ...
└── baza_gen_phone_2/
    ├── baza_gen_phone_1.txt
    ├── baza_gen_phone_2.txt
    └── ...
```

## Customization

- **Prefix List**: You can customize the list of phone number prefixes by editing the `prefixes` variable in the script.
- **Chunk Size**: Change the `max_rows_per_patch` and `max_rows_per_file` variables to adjust the number of phone numbers saved in each text file.
