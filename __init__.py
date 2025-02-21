from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

DOMAIN = "met_alerts"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    return True

async def async_setup_entry(hass: HomeAssistant, entry) -> bool:
    name = entry.data[CONF_NAME]
    latitude = entry.data[CONF_LATITUDE]
    longitude = entry.data[CONF_LONGITUDE]

    coordinator = MetAlertsCoordinator(hass, latitude, longitude)
    await coordinator.async_refresh()

    entities = [
        MetAlertsSensor(f"{name}", coordinator, 0),
        MetAlertsSensor(f"{name}_2", coordinator, 1),
        MetAlertsSensor(f"{name}_3", coordinator, 2),
        MetAlertsSensor(f"{name}_4", coordinator, 3),
    ]
    async_add_entities(entities, True)

    return True
