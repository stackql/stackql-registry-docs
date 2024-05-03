---
title: load_balancers
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancers
  - network
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
<tr><td><b>Name</b></td><td><code>load_balancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.load_balancers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation complex type. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of the load balancer. |
| <CopyableCode code="sku" /> | `object` | SKU of a load balancer. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="loadBalancerName, resourceGroupName, subscriptionId" /> | Gets the specified load balancer. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the load balancers in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="loadBalancerName, resourceGroupName, subscriptionId" /> | Creates or updates a load balancer. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="loadBalancerName, resourceGroupName, subscriptionId" /> | Deletes the specified load balancer. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the load balancers in a resource group. |
| <CopyableCode code="migrate_to_ip_based" /> | `EXEC` | <CopyableCode code="groupName, loadBalancerName, subscriptionId" /> | Migrate load balancer to IP Based |
| <CopyableCode code="swap_public_ip_addresses" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Swaps VIPs between two load balancers. |
