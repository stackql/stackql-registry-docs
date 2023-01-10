---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - smartdevicemanagement
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.smartdevicemanagement.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Required. The resource name of the device. For example: "enterprises/XYZ/devices/123". |
| `parentRelations` | `array` | Assignee details of the device. |
| `traits` | `object` | Output only. Device traits. |
| `type` | `string` | Output only. Type of the device for general display purposes. For example: "THERMOSTAT". The device type should not be used to deduce or infer functionality of the actual device it is assigned to. Instead, use the returned traits for the device. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `enterprises_devices_get` | `SELECT` | `devicesId, enterprisesId` | Gets a device managed by the enterprise. |
| `enterprises_devices_list` | `SELECT` | `enterprisesId` | Lists devices managed by the enterprise. |
| `enterprises_devices_executeCommand` | `EXEC` | `devicesId, enterprisesId` | Executes a command to device managed by the enterprise. |
