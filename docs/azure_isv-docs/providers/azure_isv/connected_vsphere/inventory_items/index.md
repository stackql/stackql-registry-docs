---
title: inventory_items
hide_title: false
hide_table_of_contents: false
keywords:
  - inventory_items
  - connected_vsphere
  - azure_isv    
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.connected_vsphere.inventory_items" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value. |
| <CopyableCode code="properties" /> | `object` | Describes the properties of an Inventory Item. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, inventoryItemName, resourceGroupName, subscriptionId, vcenterName" /> | Implements InventoryItem GET method. |
| <CopyableCode code="list_by_v_center" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, vcenterName" /> | Returns the list of inventoryItems of the given vCenter. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, inventoryItemName, resourceGroupName, subscriptionId, vcenterName, data__properties" /> | Create Or Update InventoryItem. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, inventoryItemName, resourceGroupName, subscriptionId, vcenterName" /> | Implements inventoryItem DELETE method. |
| <CopyableCode code="_list_by_v_center" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId, vcenterName" /> | Returns the list of inventoryItems of the given vCenter. |
