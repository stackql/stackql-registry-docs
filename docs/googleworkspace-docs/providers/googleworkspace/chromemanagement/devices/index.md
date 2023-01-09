---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - chromemanagement
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.chromemanagement.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Resource name of the device. |
| `storageStatusReport` | `array` | Output only. Storage reports collected periodically. |
| `batteryInfo` | `array` | Output only. Information on battery specs for the device. |
| `serialNumber` | `string` | Output only. Device serial number. This value is the same as the Admin Console's Serial Number in the ChromeOS Devices tab. |
| `bootPerformanceReport` | `array` | Output only. Boot performance reports of the device. |
| `deviceId` | `string` | Output only. The unique Directory API ID of the device. This value is the same as the Admin Console's Directory API ID in the ChromeOS Devices tab |
| `memoryStatusReport` | `array` | Output only. Memory status reports collected periodically sorted decreasing by report_time. |
| `thunderboltInfo` | `array` | Output only. Information on Thunderbolt bus. |
| `graphicsStatusReport` | `array` | Output only. Graphics reports collected periodically. |
| `orgUnitId` | `string` | Output only. Organization unit ID of the device. |
| `cpuStatusReport` | `array` | Output only. CPU status reports collected periodically sorted in a decreasing order of report_time. |
| `cpuInfo` | `array` | Output only. Information regarding CPU specs for the device. |
| `networkDiagnosticsReport` | `array` | Output only. Network diagnostics collected periodically. |
| `networkStatusReport` | `array` | Output only. Network specs collected periodically. |
| `networkInfo` | `object` | Network device information. * This field provides device information, which is static and will not change over time. * Data for this field is controlled via policy: [ReportNetworkDeviceConfiguration](https://chromeenterprise.google/policies/#ReportNetworkDeviceConfiguration) * Data Collection Frequency: At device startup * Default Data Reporting Frequency: At device startup - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: Yes * Reported for affiliated users only: N/A |
| `storageInfo` | `object` | Status data for storage. * This field is telemetry information and this will change over time as the device is utilized. * Data for this field is controlled via policy: [ReportDeviceStorageStatus](https://chromeenterprise.google/policies/#ReportDeviceStorageStatus) * Data Collection Frequency: Only at Upload * Default Data Reporting Frequency: 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: No * Reported for affiliated users only: N/A |
| `memoryInfo` | `object` | Memory information of a device. * This field has both telemetry and device information: - `totalRamBytes` - Device information - `availableRamBytes` - Telemetry information - `totalMemoryEncryption` - Device information * Data for this field is controlled via policy: [ReportDeviceMemoryInfo](https://chromeenterprise.google/policies/#ReportDeviceMemoryInfo) * Data Collection Frequency: - `totalRamBytes` - Only at upload - `availableRamBytes` - Every 10 minutes - `totalMemoryEncryption` - at device startup * Default Data Reporting Frequency: - `totalRamBytes` - 3 hours - `availableRamBytes` - 3 hours - `totalMemoryEncryption` - at device startup - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: only for `totalMemoryEncryption` * Reported for affiliated users only: N/A |
| `osUpdateStatus` | `array` | Output only. Contains relevant information regarding ChromeOS update status. |
| `batteryStatusReport` | `array` | Output only. Battery reports collected periodically. |
| `customer` | `string` | Output only. Google Workspace Customer whose enterprise enrolled the device. |
| `graphicsInfo` | `object` | Information of the graphics subsystem. * This field provides device information, which is static and will not change over time. * Data for this field is controlled via policy: [ReportDeviceGraphicsStatus](https://chromeenterprise.google/policies/#ReportDeviceGraphicsStatus) * Data Collection Frequency: Only at Upload * Default Data Reporting Frequency: 3 hours - Policy Controlled: Yes * Cache: If the device is offline, the collected data is stored locally, and will be reported when the device is next online: No * Reported for affiliated users only: N/A |
| `audioStatusReport` | `array` | Output only. Audio reports collected periodically sorted in a decreasing order of report_time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `customers_telemetry_devices_get` | `SELECT` | `customersId, devicesId` | Get telemetry device. |
| `customers_telemetry_devices_list` | `SELECT` | `customersId` | List all telemetry devices. |
