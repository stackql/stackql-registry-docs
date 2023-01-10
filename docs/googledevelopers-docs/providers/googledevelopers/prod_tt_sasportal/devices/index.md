---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - prod_tt_sasportal
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
<tr><td><b>Id</b></td><td><code>googledevelopers.prod_tt_sasportal.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource path name. |
| `deviceMetadata` | `object` | Device data overridable by both SAS Portal and registration requests. |
| `fccId` | `string` | The FCC identifier of the device. |
| `preloadedConfig` | `object` | Information about the device configuration. |
| `serialNumber` | `string` | A serial number assigned to the device by the device manufacturer. |
| `state` | `string` | Output only. Device state. |
| `currentChannels` | `array` | Output only. Current channels with scores. |
| `activeConfig` | `object` | Information about the device configuration. |
| `grants` | `array` | Output only. Grants held by the device. |
| `grantRangeAllowlists` | `array` | Only ranges that are within the allowlists are available for new grants. |
| `displayName` | `string` | Device display name. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `customers_deployments_devices_list` | `SELECT` | `customersId, deploymentsId` | Lists devices under a node or customer. |
| `customers_devices_get` | `SELECT` | `customersId, devicesId` | Gets details about a device. |
| `customers_devices_list` | `SELECT` | `customersId` | Lists devices under a node or customer. |
| `customers_nodes_devices_list` | `SELECT` | `customersId, nodesId` | Lists devices under a node or customer. |
| `deployments_devices_get` | `SELECT` | `deploymentsId, devicesId` | Gets details about a device. |
| `nodes_deployments_devices_list` | `SELECT` | `deploymentsId, nodesId` | Lists devices under a node or customer. |
| `nodes_devices_get` | `SELECT` | `devicesId, nodesId` | Gets details about a device. |
| `nodes_devices_list` | `SELECT` | `nodesId` | Lists devices under a node or customer. |
| `nodes_nodes_devices_list` | `SELECT` | `nodesId, nodesId1` | Lists devices under a node or customer. |
| `customers_deployments_devices_create` | `INSERT` | `customersId, deploymentsId` | Creates a device under a node or customer. |
| `customers_devices_create` | `INSERT` | `customersId` | Creates a device under a node or customer. |
| `customers_nodes_devices_create` | `INSERT` | `customersId, nodesId` | Creates a device under a node or customer. |
| `nodes_deployments_devices_create` | `INSERT` | `deploymentsId, nodesId` | Creates a device under a node or customer. |
| `nodes_devices_create` | `INSERT` | `nodesId` | Creates a device under a node or customer. |
| `nodes_nodes_devices_create` | `INSERT` | `nodesId, nodesId1` | Creates a device under a node or customer. |
| `customers_devices_delete` | `DELETE` | `customersId, devicesId` | Deletes a device. |
| `deployments_devices_delete` | `DELETE` | `deploymentsId, devicesId` | Deletes a device. |
| `nodes_devices_delete` | `DELETE` | `devicesId, nodesId` | Deletes a device. |
| `customers_devices_move` | `EXEC` | `customersId, devicesId` | Moves a device under another node or customer. |
| `customers_devices_patch` | `EXEC` | `customersId, devicesId` | Updates a device. |
| `customers_devices_signDevice` | `EXEC` | `customersId, devicesId` | Signs a device. |
| `customers_devices_updateSigned` | `EXEC` | `customersId, devicesId` | Updates a signed device. |
| `deployments_devices_move` | `EXEC` | `deploymentsId, devicesId` | Moves a device under another node or customer. |
| `deployments_devices_patch` | `EXEC` | `deploymentsId, devicesId` | Updates a device. |
| `deployments_devices_signDevice` | `EXEC` | `deploymentsId, devicesId` | Signs a device. |
| `deployments_devices_updateSigned` | `EXEC` | `deploymentsId, devicesId` | Updates a signed device. |
| `nodes_devices_move` | `EXEC` | `devicesId, nodesId` | Moves a device under another node or customer. |
| `nodes_devices_patch` | `EXEC` | `devicesId, nodesId` | Updates a device. |
| `nodes_devices_signDevice` | `EXEC` | `devicesId, nodesId` | Signs a device. |
| `nodes_devices_updateSigned` | `EXEC` | `devicesId, nodesId` | Updates a signed device. |
