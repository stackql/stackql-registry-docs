---
title: express_route_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_connections
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
<tr><td><b>Name</b></td><td><code>express_route_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the ExpressRouteConnection subresource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, expressRouteGatewayName, resourceGroupName, subscriptionId" /> | Gets the specified ExpressRouteConnection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="expressRouteGatewayName, resourceGroupName, subscriptionId" /> | Lists ExpressRouteConnections. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectionName, expressRouteGatewayName, resourceGroupName, subscriptionId, data__name" /> | Creates a connection between an ExpressRoute gateway and an ExpressRoute circuit. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionName, expressRouteGatewayName, resourceGroupName, subscriptionId" /> | Deletes a connection to a ExpressRoute circuit. |
