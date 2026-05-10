import os
from dotenv import load_dotenv
from config_manager import load_config, save_config
from batch_generator import run_batch_generation
from generator import TEMPLATE_CONFIGS

load_dotenv()

def prompt_for_data(current_data):
    fields = [
        ("organization_name", "Organization Name", "ABC University"),
        ("organization_tagline", "Tagline", "Excellence in Education"),
        ("certificate_title", "Certificate Title", "Certificate of Excellence"),
        ("subtitle", "Subtitle", "This certificate is proudly presented to"),
        ("body_line", "Body Line", "for outstanding performance in"),
        ("event_name", "Event Name", "Tech Workshop 2026"),
        ("organized_by", "Organized By", "organized by ABC University"),
        ("date_label", "Date Label", "Date"),
        ("date_value", "Date Value", "May 2026"),
        ("venue_label", "Venue Label", "Venue"),
        ("venue_value", "Venue Value", "Hyderabad"),
        ("cert_id_label", "Certificate ID Label", "Certificate No."),
        ("dignitary_1_name", "Dignitary 1 Name", "Dr. Rao"),
        ("dignitary_1_title", "Dignitary 1 Title", "Director"),
        ("dignitary_2_name", "Dignitary 2 Name", "Prof. Sharma"),
        ("dignitary_2_title", "Dignitary 2 Title", "Dean"),
        ("dignitary_3_name", "Dignitary 3 Name", "Ms. Iyer"),
        ("dignitary_3_title", "Dignitary 3 Title", "Coordinator"),
        ("footer_text", "Footer Text", "abc@university.com")
    ]
    
    print("\n--- Certificate Data Wizard ---")
    print("Press Enter to keep the default/saved value.\n")
    
    new_data = {}
    for key, label, default in fields:
        saved_val = current_data.get(key, default)
        user_input = input(f"{label} [{saved_val}]: ").strip()
        new_data[key] = user_input if user_input else saved_val
        
    return new_data

def select_template():
    print("\n--- Select a Template ---")
    for tid, config in TEMPLATE_CONFIGS.items():
        print(f"[{tid}] {config['description']}")
        
    while True:
        choice = input("Enter template number: ").strip()
        if choice in TEMPLATE_CONFIGS:
            return choice
        print("Invalid choice, please try again.")

def main():
    while True:
        print("\n===== CERTIFICATE GENERATOR =====")
        print("1. Generate Certificates")
        print("2. Send Emails")
        print("3. Generate + Send")
        print("4. Update Configuration")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice in ["1", "2", "3"]:
            config = load_config()
            if not config:
                print("\nConfiguration not found. Let's set it up.")
                config = prompt_for_data({})
                save_config(config)
            
            print("\nUsing current configuration.")
            
            template_id = select_template()
            
            generate_certs = choice in ["1", "3"]
            send_emails = choice in ["2", "3"]
            
            print("\nStarting batch process...\n")
            run_batch_generation(
                cert_data=config, 
                template_id=template_id, 
                generate_certs=generate_certs, 
                send_emails=send_emails
            )
            print("\nBatch process completed.")
            
        elif choice == "4":
            config = load_config()
            new_config = prompt_for_data(config)
            save_config(new_config)
            print("\nConfiguration saved.")
            
        elif choice == "5":
            print("\nExiting program...\n")
            break
            
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()