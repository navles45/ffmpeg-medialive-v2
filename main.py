from livestream.input import create_medialive_input

input_name = "BD-Webinar"
stream_key = "bangladesh-A"

def main():
	input_properties = create_medialive_input(input_name, stream_key)
	

if __name__ == '__main__':
    main()
