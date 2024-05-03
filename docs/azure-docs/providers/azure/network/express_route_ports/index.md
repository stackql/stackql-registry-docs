---
title: express_route_ports
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_ports
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
<tr><td><b>Name</b></td><td><code>express_route_ports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_ports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties specific to ExpressRoutePort resources. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="expressRoutePortName, resourceGroupName, subscriptionId" /> | Retrieves the requested ExpressRoutePort resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the ExpressRoutePort resources in the specified subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the ExpressRoutePort resources in the specified resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="expressRoutePortName, resourceGroupName, subscriptionId" /> | Creates or updates the specified ExpressRoutePort resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="expressRoutePortName, resourceGroupName, subscriptionId" /> | Deletes the specified ExpressRoutePort resource. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | List all the ExpressRoutePort resources in the specified subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the ExpressRoutePort resources in the specified resource group. |
| <CopyableCode code="generate_loa" /> | `EXEC` | <CopyableCode code="expressRoutePortName, resourceGroupName, subscriptionId, data__customerName" /> | Generate a letter of authorization for the requested ExpressRoutePort resource. |
