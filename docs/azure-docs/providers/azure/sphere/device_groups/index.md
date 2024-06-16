---
title: device_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - device_groups
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
<tr><td><b>Name</b></td><td><code>device_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sphere.device_groups" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | Get a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| <CopyableCode code="list_by_product" /> | `SELECT` | <CopyableCode code="catalogName, productName, resourceGroupName, subscriptionId" /> | List DeviceGroup resources by Product. '.default' and '.unassigned' are system defined values and cannot be used for product name. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | Create a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | Delete a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| <CopyableCode code="claim_devices" /> | `EXEC` | <CopyableCode code="catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId, data__deviceIdentifiers" /> | Bulk claims the devices. Use '.unassigned' or '.default' for the device group and product names when bulk claiming devices to a catalog only. |
| <CopyableCode code="count_devices" /> | `EXEC` | <CopyableCode code="catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | Counts devices in device group. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId" /> | Update a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
