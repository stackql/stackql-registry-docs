---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - cloudiot
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudiot.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The user-defined device identifier. The device ID must be unique within a device registry. |
| `name` | `string` | The resource path name. For example, `projects/p1/locations/us-central1/registries/registry0/devices/dev0` or `projects/p1/locations/us-central1/registries/registry0/devices/{num_id}`. When `name` is populated as a response from the service, it always ends in the device numeric ID. |
| `lastErrorStatus` | `object` | The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). |
| `lastStateTime` | `string` | [Output only] The last time a state event was received. Timestamps are periodically collected and written to storage; they may be stale by a few minutes. |
| `logLevel` | `string` | **Beta Feature** The logging verbosity for device activity. If unspecified, DeviceRegistry.log_level will be used. |
| `metadata` | `object` | The metadata key-value pairs assigned to the device. This metadata is not interpreted or indexed by Cloud IoT Core. It can be used to add contextual information for the device. Keys must conform to the regular expression a-zA-Z+ and be less than 128 bytes in length. Values are free-form strings. Each value must be less than or equal to 32 KB in size. The total size of all keys and values must be less than 256 KB, and the maximum number of key-value pairs is 500. |
| `lastEventTime` | `string` | [Output only] The last time a telemetry event was received. Timestamps are periodically collected and written to storage; they may be stale by a few minutes. |
| `blocked` | `boolean` | If a device is blocked, connections or requests from this device will fail. Can be used to temporarily prevent the device from connecting if, for example, the sensor is generating bad data and needs maintenance. |
| `lastConfigAckTime` | `string` | [Output only] The last time a cloud-to-device config version acknowledgment was received from the device. This field is only for configurations sent through MQTT. |
| `lastHeartbeatTime` | `string` | [Output only] The last time an MQTT `PINGREQ` was received. This field applies only to devices connecting through MQTT. MQTT clients usually only send `PINGREQ` messages if the connection is idle, and no other messages have been sent. Timestamps are periodically collected and written to storage; they may be stale by a few minutes. |
| `lastConfigSendTime` | `string` | [Output only] The last time a cloud-to-device config version was sent to the device. |
| `config` | `object` | The device configuration. Eventually delivered to devices. |
| `numId` | `string` | [Output only] A server-defined unique numeric ID for the device. This is a more compact way to identify devices, and it is globally unique. |
| `credentials` | `array` | The credentials used to authenticate this device. To allow credential rotation without interruption, multiple device credentials can be bound to this device. No more than 3 credentials can be bound to a single device at a time. When new credentials are added to a device, they are verified against the registry credentials. For details, see the description of the `DeviceRegistry.credentials` field. |
| `state` | `object` | The device state, as reported by the device. |
| `lastErrorTime` | `string` | [Output only] The time the most recent error occurred, such as a failure to publish to Cloud Pub/Sub. This field is the timestamp of 'last_error_status'. |
| `gatewayConfig` | `object` | Gateway-related configuration and state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_registries_devices_get` | `SELECT` | `devicesId, locationsId, projectsId, registriesId` | Gets details about a device. |
| `projects_locations_registries_devices_list` | `SELECT` | `locationsId, projectsId, registriesId` | List devices in a device registry. |
| `projects_locations_registries_groups_devices_list` | `SELECT` | `groupsId, locationsId, projectsId, registriesId` | List devices in a device registry. |
| `projects_locations_registries_devices_create` | `INSERT` | `locationsId, projectsId, registriesId` | Creates a device in a device registry. |
| `projects_locations_registries_devices_delete` | `DELETE` | `devicesId, locationsId, projectsId, registriesId` | Deletes a device. |
| `projects_locations_registries_devices_modifyCloudToDeviceConfig` | `EXEC` | `devicesId, locationsId, projectsId, registriesId` | Modifies the configuration for the device, which is eventually sent from the Cloud IoT Core servers. Returns the modified configuration version and its metadata. |
| `projects_locations_registries_devices_patch` | `EXEC` | `devicesId, locationsId, projectsId, registriesId` | Updates a device. |
| `projects_locations_registries_devices_sendCommandToDevice` | `EXEC` | `devicesId, locationsId, projectsId, registriesId` | Sends a command to the specified device. In order for a device to be able to receive commands, it must: 1) be connected to Cloud IoT Core using the MQTT protocol, and 2) be subscribed to the group of MQTT topics specified by /devices/{device-id}/commands/#. This subscription will receive commands at the top-level topic /devices/{device-id}/commands as well as commands for subfolders, like /devices/{device-id}/commands/subfolder. Note that subscribing to specific subfolders is not supported. If the command could not be delivered to the device, this method will return an error; in particular, if the device is not subscribed, this method will return FAILED_PRECONDITION. Otherwise, this method will return OK. If the subscription is QoS 1, at least once delivery will be guaranteed; for QoS 0, no acknowledgment will be expected from the device. |
