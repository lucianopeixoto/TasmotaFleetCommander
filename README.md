# TasmotaFleetCommander

TasmotaFleetCommander is a lightweight Python utility designed to manage multiple Tasmota IoT devices across a local network.

The tool automatically discovers Tasmota devices, inspects their configuration, and allows administrators to issue commands across an entire fleet using the Tasmota Web API.

It is particularly useful for homelabs, IoT deployments, and smart homes where dozens of devices must be managed consistently.

---

![Sample Screenshot](https://github.com/lucianopeixoto/TasmotaFleetCommander/blob/main/screenshot.png?raw=true)

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

In a real-world scenario, this tool was developed during a network redesign where the ISP router was converted to a gateway-only device and a new OpenWrt router took over DHCP and Wi-Fi. The network was migrated to `192.168.100.0/24`.

Previously, Tasmota devices were configured to use a static IP (e.g., `192.168.1.50`) for the MQTT broker due to unreliable DNS. With the new setup, reliable hostname resolution made it possible to switch to a hostname-based configuration (e.g., `mqtt.local`).

TasmotaFleetCommander can automatically discover all devices and update the MQTT host for the entire fleet in seconds, eliminating manual effort and ensuring consistency.

Example operation:

- Scan the network for Tasmota devices  
- Identify active devices and their configurations  
- Apply updated MQTT settings across all devices
