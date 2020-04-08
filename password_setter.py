import os
def change_the_password(password = 'Hello123'):
    os.system('nmcli connection modify Ml_is_DeepShit \
    802-11-wireless-security.key-mgmt wpa-psk \
    802-11-wireless-security.psk ' + password)
