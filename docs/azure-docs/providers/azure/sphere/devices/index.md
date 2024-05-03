---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - sphere
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sphere.devices" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, deviceGroupName, deviceName, productName, resourceGroupName, subscriptionId" /> | Get a Device. Use '.unassigned' or '.default' for the device group and product names when a device does not belong to a device group and product. |
| <CopyableCode code="list_by_device_group" /> | `SELECT` | <CopyableCode code="catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | List Device resources by DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="catalogName, deviceGroupName, deviceName, productName, resourceGroupName, subscriptionId" /> | Create a Device. Use '.unassigned' or '.default' for the device group and product names to claim a device to the catalog only. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogName, deviceGroupName, deviceName, productName, resourceGroupName, subscriptionId" /> | Delete a Device |
| <CopyableCode code="_list_by_device_group" /> | `EXEC` | <CopyableCode code="catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | List Device resources by DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| <CopyableCode code="generate_capability_image" /> | `EXEC` | <CopyableCode code="catalogName, deviceGroupName, deviceName, productName, resourceGroupName, subscriptionId, data__capabilities" /> | Generates the capability image for the device. Use '.unassigned' or '.default' for the device group and product names to generate the image for a device that does not belong to a specific device group and product. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="catalogName, deviceGroupName, deviceName, productName, resourceGroupName, subscriptionId" /> | Update a Device. Use '.unassigned' or '.default' for the device group and product names to move a device to the catalog level. |
