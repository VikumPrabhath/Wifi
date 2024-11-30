import subprocess

def get_wifi_passwords():
    """This function retrieves Wi-Fi passwords from the system."""

    # Get a list of Wi-Fi profiles
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    profiles = [i.split(":")[1][1:-1] for i in results if "All User Profile" in i]

    # Print a header
    print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
    print("-" * 50)

    # Iterate over each profile
    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

        try:
            print("{:<30}| {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30}| {:<}".format(i, "NOT FOUND"))
        except subprocess.CalledProcessError:
            print("{:<30}| {:<}".format(i, "ERROR: Could not retrieve password"))

if __name__ == "__main__":
    get_wifi_passwords()