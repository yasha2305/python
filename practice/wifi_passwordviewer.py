import subprocess

# Get all saved Wi-Fi profiles
def get_wifi_profiles():
    command = "netsh wlan show profiles"

    result = subprocess.check_output(
        command,
        shell=True
    ).decode(errors="ignore")

    profiles = []

    for line in result.split("\n"):
        if "All User Profile" in line:
            profile = line.split(":")[1].strip()
            profiles.append(profile)

    return profiles

# Get password for one Wi-Fi profile
def get_wifi_password(profile):
    try:
        command = f'netsh wlan show profile "{profile}" key=clear'

        result = subprocess.check_output(
            command,
            shell=True
        ).decode(errors="ignore")

        for line in result.split("\n"):
            if "Key Content" in line:
                return line.split(":")[1].strip()

        return "No Password"

    except:
        return "Access Denied"

# Main program
def main():
    print("\nSaved Wi-Fi Networks:\n")

    profiles = get_wifi_profiles()

    if not profiles:
        print("No Wi-Fi profiles found.")
        return

    for profile in profiles:
        password = get_wifi_password(profile)

        print(f"Wi-Fi Name : {profile}")
        print(f"Password   : {password}")
        print("-" * 40)

if __name__ == "__main__":
    main()