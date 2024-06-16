---
title: load_balancer_backend_address_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - load_balancer_backend_address_pools
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
<tr><td><b>Name</b></td><td><code>load_balancer_backend_address_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.load_balancer_backend_address_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within the set of backend address pools used by the load balancer. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the backend address pool. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backendAddressPoolName, loadBalancerName, resourceGroupName, subscriptionId" /> | Gets load balancer backend address pool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="loadBalancerName, resourceGroupName, subscriptionId" /> | Gets all the load balancer backed address pools. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="backendAddressPoolName, loadBalancerName, resourceGroupName, subscriptionId" /> | Creates or updates a load balancer backend address pool. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backendAddressPoolName, loadBalancerName, resourceGroupName, subscriptionId" /> | Deletes the specified load balancer backend address pool. |
