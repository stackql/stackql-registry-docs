---
title: express_route_port_authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_port_authorizations
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
<tr><td><b>Name</b></td><td><code>express_route_port_authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_port_authorizations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of ExpressRoutePort Authorization. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="authorizationName, expressRoutePortName, resourceGroupName, subscriptionId" /> | Gets the specified authorization from the specified express route port. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="expressRoutePortName, resourceGroupName, subscriptionId" /> | Gets all authorizations in an express route port. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="authorizationName, expressRoutePortName, resourceGroupName, subscriptionId" /> | Creates or updates an authorization in the specified express route port. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="authorizationName, expressRoutePortName, resourceGroupName, subscriptionId" /> | Deletes the specified authorization from the specified express route port. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="expressRoutePortName, resourceGroupName, subscriptionId" /> | Gets all authorizations in an express route port. |
