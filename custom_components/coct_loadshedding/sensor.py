"""Sensor platform for CoCT Loadshedding Interface."""
from .const import (
    DEFAULT_NAME,
    DOMAIN,
    ICON,
    SENSOR,
)
from .entity import CoCTEntity, LoadSheddingActiveEntity, NextLoadSheddingEntity, SecondsTillNextSheddingEntity
from datetime import datetime, timedelta

async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices(
        [
            CoCTStageSensor(coordinator, entry),
            LoadSheddingActiveSensor(coordinator, entry),
            NextLoadSheddingSensor(coordinator, entry),
            SecondsTillNextSheddingSensor(coordinator, entry),
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

class SecondsTillNextSheddingSensor(SecondsTillNextSheddingEntity):
    """Load Shedding Active Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_seconds_till_next_shedding"

    @property
    def state(self):
        """Return the state of the sensor."""
        date_format = "%Y-%m-%d %H:%M:%S"
        next_slot = self.coordinator.data.get("next_load_shedding_slot")
        if next_slot:
            next_slot_time = datetime.strptime(next_slot, date_format)
            seconds_till_next = (next_slot_time - datetime.now()).total_seconds()
            return max(0, int(seconds_till_next))
        return None

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON