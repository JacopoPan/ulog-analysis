# ulog-analysis

## Installation

```sh
conda create -n ulog python=3.10
conda activate ulog
pip3 install --upgrade pip
git clone https://github.com/JacopoPan/ulog-analysis.git
cd ulog-analysis/
pip3 install -e .
```

## Use

```sh
conda activate ulog
cd ulog-analysis/
python3 ulog_analysis/main.py --file [relative-path-and-filename-of-the-ulog-file]
```
