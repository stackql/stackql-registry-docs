---
title: network_racks
hide_title: false
hide_table_of_contents: false
keywords:
  - network_racks
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
<tr><td><b>Name</b></td><td><code>network_racks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_racks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network Rack Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkRackName, resourceGroupName, subscriptionId" /> | Get Network Rack resource details. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all Network Rack resources in the given resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all Network Rack resources in the given subscription |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkRackName, resourceGroupName, subscriptionId, data__location, data__properties" /> | Create Network Rack resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkRackName, resourceGroupName, subscriptionId" /> | Delete Network Rack resource. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all Network Rack resources in the given resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List all Network Rack resources in the given subscription |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="networkRackName, resourceGroupName, subscriptionId" /> | Update certain properties of the Network Rack resource. |
