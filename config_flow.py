import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.const import CONF_NAME, CONF_LATITUDE, CONF_LONGITUDE

from .const import DOMAIN, DEFAULT_NAME

@callback
def configured_instances(hass):
    return set(entry.title for entry in hass.config_entries.async_entries(DOMAIN))

class MetAlertsConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            if user_input[CONF_NAME] not in configured_instances(self.hass):
                return self.async_create_entry(title=user_input[CONF_NAME], data=user_input)
            else:
                errors["base"] = "name_exists"

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_NAME, default=DEFAULT_NAME): str,
                vol.Required(CONF_LATITUDE): float,
                vol.Required(CONF_LONGITUDE): float,
            }),
            errors=errors,
        )