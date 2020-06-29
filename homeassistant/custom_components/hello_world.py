from homeassistant import __main__ as hass_entry
import sys

if __name__ == "__main__":
    sys.argv[0] = '--runner';
    sys.exit(hass_entry.main())