"""Sensor platform for CoCT Loadshedding Interface."""
from .const import (
    DEFAULT_NAME,
    DOMAIN,
    ICON,
    SENSOR,
)
from .entity import CoCTEntity, LoadSheddingActiveEntity, NextLoadSheddingEntity, NextLoadSheddingSecondsEntity
import datetime


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        [
            CoCTStageSensor(coordinator, entry),
            LoadSheddingActiveSensor(coordinator, entry),
            NextLoadSheddingSensor(coordinator, entry),
            NextLoadSheddingSecondsSensor(coordinator, entry),  # Add this line
        ]
    )


class CoCTStageSensor(CoCTEntity):
    """CoCT Stage Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_stage"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get("stage")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON


class LoadSheddingActiveSensor(LoadSheddingActiveEntity):
    """Load Shedding Active Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_load_shedding_active"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get("load_shedding_active")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON


class NextLoadSheddingSensor(NextLoadSheddingEntity):
    """Load Shedding Active Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_next_load_shedding_slot"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get("next_load_shedding_slot")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON


class NextLoadSheddingSecondsSensor(NextLoadSheddingSecondsEntity):
    """Next Load Shedding Seconds Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_next_load_shedding_seconds"

    @property
    def state(self):
        """Return the state of the sensor."""
        next_slot = self.coordinator.data.get("next_load_shedding_slot")
        if next_slot:
            return (next_slot - datetime.datetime.now()).total_seconds()
        return None

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON
