<h1 align="center">mysistem</h1>

Systemd is an init system and system manager that is widely used in modern Linux distributions to bootstrap the user space and manage system processes. A systemd service is a unit configuration file that defines how a particular service should be started, stopped, and managed.

# Install

Run the following script to copy all necessary services into systemd:

```
. install.sh
```

# Uninstall

Run the following script to remove all necessary services from systemd:

```
. uninstall.sh
```

# Testing

To test the service without installing it into systemd, run:

```
. testing.sh
```

# Services

### mysistem_check_container.service

This service checks the status of Docker containers and reports any errors to a Telegram group chat.

| environment | description |
| :-- | :-- |
| CHECK_CONTAINER_TELEGRAM | Telegram bot token |
| CHECK_CONTAINER_CHATID | Collection of Telegram group chat IDs, separated by `;` |
| CHECK_CONTAINER_LIST | Collection of containers to monitor, separated by `;` |
