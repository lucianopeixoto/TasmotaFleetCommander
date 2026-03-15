# TasmotaFleetCommander

TasmotaFleetCommander is a lightweight Python utility designed to manage multiple Tasmota IoT devices across a local network.

The tool automatically discovers Tasmota devices, inspects their configuration, and allows administrators to issue commands across an entire fleet using the Tasmota Web API.

It is particularly useful for homelabs, IoT deployments, and smart homes where dozens of devices must be managed consistently.

---

![Sample Screenshot](https://github.com/lucianopeixoto/TasmotaFleetCommander/screenshot.png?raw=true)

---

## Features

- Automatic network scanning
- Tasmota device detection
- Parallel device communication
- MQTT configuration management
- Batch command execution
- Fast fleet-wide updates
- Simple Python implementation

---

## Example Use Case

When migrating an MQTT server, manually updating each device can be time consuming.

TasmotaFleetCommander can automatically discover all devices and update the MQTT host for the entire fleet in seconds.

Example operation:

Scan network for devices:
