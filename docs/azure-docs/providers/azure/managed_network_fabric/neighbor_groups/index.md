---
title: neighbor_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - neighbor_groups
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>neighbor_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.neighbor_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Neighbor Group Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="neighborGroupName, resourceGroupName, subscriptionId" /> | Gets the Neighbor Group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Displays NeighborGroups list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Displays NeighborGroups list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="neighborGroupName, resourceGroupName, subscriptionId, data__properties" /> | Implements the Neighbor Group PUT method. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="neighborGroupName, resourceGroupName, subscriptionId" /> | Implements Neighbor Group DELETE method. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="neighborGroupName, resourceGroupName, subscriptionId" /> | Updates the Neighbor Group. |
