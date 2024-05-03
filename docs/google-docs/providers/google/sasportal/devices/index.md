---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - sasportal
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sasportal.devices" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource path name. |
| <CopyableCode code="activeConfig" /> | `object` | Information about the device configuration. |
| <CopyableCode code="currentChannels" /> | `array` | Output only. Current channels with scores. |
| <CopyableCode code="deviceMetadata" /> | `object` | Device data overridable by both SAS Portal and registration requests. |
| <CopyableCode code="displayName" /> | `string` | Device display name. |
| <CopyableCode code="fccId" /> | `string` | The FCC identifier of the device. |
| <CopyableCode code="grantRangeAllowlists" /> | `array` | Only ranges that are within the allowlists are available for new grants. |
| <CopyableCode code="grants" /> | `array` | Output only. Grants held by the device. |
| <CopyableCode code="preloadedConfig" /> | `object` | Information about the device configuration. |
| <CopyableCode code="serialNumber" /> | `string` | A serial number assigned to the device by the device manufacturer. |
| <CopyableCode code="state" /> | `string` | Output only. Device state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="customers_deployments_devices_list" /> | `SELECT` | <CopyableCode code="customersId, deploymentsId" /> | Lists devices under a node or customer. |
| <CopyableCode code="customers_devices_get" /> | `SELECT` | <CopyableCode code="customersId, devicesId" /> | Gets details about a device. |
| <CopyableCode code="customers_devices_list" /> | `SELECT` | <CopyableCode code="customersId" /> | Lists devices under a node or customer. |
| <CopyableCode code="customers_nodes_devices_list" /> | `SELECT` | <CopyableCode code="customersId, nodesId" /> | Lists devices under a node or customer. |
| <CopyableCode code="deployments_devices_get" /> | `SELECT` | <CopyableCode code="deploymentsId, devicesId" /> | Gets details about a device. |
| <CopyableCode code="nodes_deployments_devices_list" /> | `SELECT` | <CopyableCode code="deploymentsId, nodesId" /> | Lists devices under a node or customer. |
| <CopyableCode code="nodes_devices_get" /> | `SELECT` | <CopyableCode code="devicesId, nodesId" /> | Gets details about a device. |
| <CopyableCode code="nodes_devices_list" /> | `SELECT` | <CopyableCode code="nodesId" /> | Lists devices under a node or customer. |
| <CopyableCode code="nodes_nodes_devices_list" /> | `SELECT` | <CopyableCode code="nodesId, nodesId1" /> | Lists devices under a node or customer. |
| <CopyableCode code="customers_deployments_devices_create" /> | `INSERT` | <CopyableCode code="customersId, deploymentsId" /> | Creates a device under a node or customer. |
| <CopyableCode code="customers_devices_create" /> | `INSERT` | <CopyableCode code="customersId" /> | Creates a device under a node or customer. |
| <CopyableCode code="customers_nodes_devices_create" /> | `INSERT` | <CopyableCode code="customersId, nodesId" /> | Creates a device under a node or customer. |
| <CopyableCode code="nodes_deployments_devices_create" /> | `INSERT` | <CopyableCode code="deploymentsId, nodesId" /> | Creates a device under a node or customer. |
| <CopyableCode code="nodes_devices_create" /> | `INSERT` | <CopyableCode code="nodesId" /> | Creates a device under a node or customer. |
| <CopyableCode code="nodes_nodes_devices_create" /> | `INSERT` | <CopyableCode code="nodesId, nodesId1" /> | Creates a device under a node or customer. |
| <CopyableCode code="customers_devices_delete" /> | `DELETE` | <CopyableCode code="customersId, devicesId" /> | Deletes a device. |
| <CopyableCode code="deployments_devices_delete" /> | `DELETE` | <CopyableCode code="deploymentsId, devicesId" /> | Deletes a device. |
| <CopyableCode code="nodes_devices_delete" /> | `DELETE` | <CopyableCode code="devicesId, nodesId" /> | Deletes a device. |
| <CopyableCode code="_customers_deployments_devices_list" /> | `EXEC` | <CopyableCode code="customersId, deploymentsId" /> | Lists devices under a node or customer. |
| <CopyableCode code="_customers_devices_list" /> | `EXEC` | <CopyableCode code="customersId" /> | Lists devices under a node or customer. |
| <CopyableCode code="_customers_nodes_devices_list" /> | `EXEC` | <CopyableCode code="customersId, nodesId" /> | Lists devices under a node or customer. |
| <CopyableCode code="_nodes_deployments_devices_list" /> | `EXEC` | <CopyableCode code="deploymentsId, nodesId" /> | Lists devices under a node or customer. |
| <CopyableCode code="_nodes_devices_list" /> | `EXEC` | <CopyableCode code="nodesId" /> | Lists devices under a node or customer. |
| <CopyableCode code="_nodes_nodes_devices_list" /> | `EXEC` | <CopyableCode code="nodesId, nodesId1" /> | Lists devices under a node or customer. |
| <CopyableCode code="customers_devices_move" /> | `EXEC` | <CopyableCode code="customersId, devicesId" /> | Moves a device under another node or customer. |
| <CopyableCode code="customers_devices_patch" /> | `EXEC` | <CopyableCode code="customersId, devicesId" /> | Updates a device. |
| <CopyableCode code="customers_devices_sign_device" /> | `EXEC` | <CopyableCode code="customersId, devicesId" /> | Signs a device. |
| <CopyableCode code="deployments_devices_move" /> | `EXEC` | <CopyableCode code="deploymentsId, devicesId" /> | Moves a device under another node or customer. |
| <CopyableCode code="deployments_devices_patch" /> | `EXEC` | <CopyableCode code="deploymentsId, devicesId" /> | Updates a device. |
| <CopyableCode code="deployments_devices_sign_device" /> | `EXEC` | <CopyableCode code="deploymentsId, devicesId" /> | Signs a device. |
| <CopyableCode code="nodes_devices_move" /> | `EXEC` | <CopyableCode code="devicesId, nodesId" /> | Moves a device under another node or customer. |
| <CopyableCode code="nodes_devices_patch" /> | `EXEC` | <CopyableCode code="devicesId, nodesId" /> | Updates a device. |
| <CopyableCode code="nodes_devices_sign_device" /> | `EXEC` | <CopyableCode code="devicesId, nodesId" /> | Signs a device. |
