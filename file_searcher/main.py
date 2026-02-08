import os
from pathlib import Path
from collections import Counter

def creating_file_path(path):
    base_dir = Path(__file__).parent
    return base_dir / path

def scanFiles(startDirectory, TotalLines, ScannedFiles, counter):
    print("Scaning files...")
    TotalLines=TotalLines
    ScannedFiles = ScannedFiles
    startDirectory=creating_file_path(startDirectory)
    for path, subdirs, files in os.walk(startDirectory):
        for file in files:
            if(Path(file).suffix==".txt"):
               with open(os.path.join(startDirectory,file), "r") as auto:
                for line in auto:
                    for word in line.split():
                        counter[word]+=1
                    TotalLines+=1
                ScannedFiles+=1
        for subdir in subdirs:
            TotalLines,ScannedFiles,counter = scanFiles(startDirectory/subdir,TotalLines,ScannedFiles,counter)
        return TotalLines,ScannedFiles,counter


if __name__ == "__main__":
    print("File Searcher")
    counter = Counter()
    totalLines =0
    ScannedFiles =0
    totalLines,ScannedFiles,counter = scanFiles("data",totalLines,ScannedFiles,counter)
    print("TotalLines: " + str(totalLines))
    print("Scanned files: "  + str(ScannedFiles))
    most_common_word, count = counter.most_common(1)[0]
    print(f"Most used word: {most_common_word} ({count} times)")