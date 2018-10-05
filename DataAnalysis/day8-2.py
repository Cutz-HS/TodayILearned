import re
import codecs

input_File='output.txt'
output_File='output2.txt'

def clean_text(text):
    pattern=r"[a-zA-Z]"
    pattern1=r"[\(\)\[\]][가-힣]+\s?[가-힣]+?[\(\)\[\]]"
    pattern2=r"[\W]"
    pattern3=r"[\s]{2,}"
    cleaned_text=re.sub(pattern,' ', text)
    cleaned_text=re.sub(pattern1, ' ', cleaned_text)
    cleaned_text=re.sub(pattern2,' ', cleaned_text)
    cleaned_text=re.sub(pattern3, ' ', cleaned_text)
    return cleaned_text


def main():
    read_File=codecs.open(input_File, "r", encoding='utf-8')
    write_File=codecs.open(output_File, "w", encoding='utf-8')
    text=read_File.read()
    cleaned_text=clean_text(text)
    write_File.write(cleaned_text)
    read_File.close()
    write_File.close()


if __name__=='__main__':
    main()