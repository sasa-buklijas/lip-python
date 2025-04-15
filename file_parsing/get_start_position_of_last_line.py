import sys
import json


def main():
    file_name = sys.argv[1]
    #print(f'{file_name=}')
    #exit(3)

    # # Open the file 
    # # and yield read_line_number and line till "\n" in loop
    try:
        json_line = None
        read_line_number = 0
        # manually opening file because otherwise file not available in finally
        file = open(file_name, 'r')

        # can not use for loop on file
        # because file.tell() and fie.seek() not working then
        tell_before_read = 0
        last_valid_tell = 0
        while True:
            tell_before_read = file.tell()
            print(f'Next readline {tell_before_read=}')
            json_line = file.readline()
            print(f'{json_line=} {file.tell()=}')

            # stop is end of file
            if not json_line:
                print('End of file')
                break
            # if line exist, counter updated
            read_line_number += 1

            # skip empty lines
            if json_line == '\n':
                #print(f'Skipping empty line {json_line=}')
                continue

            try:
                log_entry = json.loads(json_line)
            except json.decoder.JSONDecodeError as e:
                print(f'Not JSON {json_line=} details: {e=}')
                continue

            # here we have valid tell

            # if from_asctime >= log_entry['asctime']:
            #     #logging.debug('Log line already processed')
            #     continue


    except FileNotFoundError:
        print(f"Error: File '{file_name=}' not found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        print(f"{read_line_number}: {json_line}")

    finally:
        len_current_line = len(json_line.encode('utf-8'))
        current_byte_offset = file.tell()
        last_log_line_offset = current_byte_offset - len_current_line
        print(f'{file.tell()=} {len_current_line=} {last_log_line_offset=}')
        file.close()


if __name__ == "__main__":
    #print('start')
    main()
    #print('end')
