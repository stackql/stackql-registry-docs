---
title: inventory_items
hide_title: false
hide_table_of_contents: false
keywords:
  - inventory_items
  - system_center_vm_manager
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
<tr><td><b>Name</b></td><td><code>inventory_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.system_center_vm_manager.inventory_items" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="properties" /> | `object` | Defines the resource properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="inventoryItemResourceName, resourceGroupName, subscriptionId, vmmServerName" /> | Shows an inventory item. |
| <CopyableCode code="list_by_vmm_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmmServerName" /> | Returns the list of inventoryItems in the given VmmServer. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="inventoryItemResourceName, resourceGroupName, subscriptionId, vmmServerName" /> | Create Or Update InventoryItem. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="inventoryItemResourceName, resourceGroupName, subscriptionId, vmmServerName" /> | Deletes an inventoryItem. |
