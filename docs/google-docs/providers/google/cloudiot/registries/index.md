---
title: registries
hide_title: false
hide_table_of_contents: false
keywords:
  - registries
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
<tr><td><b>Name</b></td><td><code>registries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudiot.registries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of this device registry. For example, `myRegistry`. |
| `name` | `string` | The resource path name. For example, `projects/example-project/locations/us-central1/registries/my-registry`. |
| `stateNotificationConfig` | `object` | The configuration for notification of new states received from the device. |
| `credentials` | `array` | The credentials used to verify the device credentials. No more than 10 credentials can be bound to a single registry at a time. The verification process occurs at the time of device creation or update. If this field is empty, no verification is performed. Otherwise, the credentials of a newly created device or added credentials of an updated device should be signed with one of these registry credentials. Note, however, that existing devices will never be affected by modifications to this list of credentials: after a device has been successfully created in a registry, it should be able to connect even if its registry credentials are revoked, deleted, or modified. |
| `eventNotificationConfigs` | `array` | The configuration for notification of telemetry events received from the device. All telemetry events that were successfully published by the device and acknowledged by Cloud IoT Core are guaranteed to be delivered to Cloud Pub/Sub. If multiple configurations match a message, only the first matching configuration is used. If you try to publish a device telemetry event using MQTT without specifying a Cloud Pub/Sub topic for the device's registry, the connection closes automatically. If you try to do so using an HTTP connection, an error is returned. Up to 10 configurations may be provided. |
| `httpConfig` | `object` | The configuration of the HTTP bridge for a device registry. |
| `logLevel` | `string` | **Beta Feature** The default logging verbosity for activity from devices in this registry. The verbosity level can be overridden by Device.log_level. |
| `mqttConfig` | `object` | The configuration of MQTT for a device registry. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_registries_get` | `SELECT` | `locationsId, projectsId, registriesId` | Gets a device registry configuration. |
| `projects_locations_registries_list` | `SELECT` | `locationsId, projectsId` | Lists device registries. |
| `projects_locations_registries_create` | `INSERT` | `locationsId, projectsId` | Creates a device registry that contains devices. |
| `projects_locations_registries_delete` | `DELETE` | `locationsId, projectsId, registriesId` | Deletes a device registry configuration. |
| `projects_locations_registries_bindDeviceToGateway` | `EXEC` | `locationsId, projectsId, registriesId` | Associates the device with the gateway. |
| `projects_locations_registries_patch` | `EXEC` | `locationsId, projectsId, registriesId` | Updates a device registry configuration. |
| `projects_locations_registries_unbindDeviceFromGateway` | `EXEC` | `locationsId, projectsId, registriesId` | Deletes the association between the device and the gateway. |
