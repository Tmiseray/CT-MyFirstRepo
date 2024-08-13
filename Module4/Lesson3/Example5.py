class Smartphone:
    def download_app(self, app_name):
        print(f"Downloading {app_name} in a generic way")

class AndroidPhone(Smartphone):
    def download_app(self, app_name):
        print(f"Downloading {app_name} from Google Play Store")

class IPhone(Smartphone):
    def download_app(self, app_name):
        print(f"Downloading {app_name} from Apple App Store")

def download_app_on_phone(phone, app_name):
    phone.download_app(app_name)

generic_phone = Smartphone()
android_phone = AndroidPhone()
iphone = IPhone()

# Using the same function to download an app on different types of phones
download_app_on_phone(generic_phone, "WhatsApp")    # Output: Downloading WhatsApp in a generic way
download_app_on_phone(android_phone, "WhatsApp")    # Output: Downloading WhatsApp from Google Play Store
download_app_on_phone(iphone, "WhatsApp")   # Output: Downloading WhatsApp from Apple App Store