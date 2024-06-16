---
title: express_route_circuit_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuit_connections
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
<tr><td><b>Name</b></td><td><code>express_route_circuit_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_circuit_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Properties of the express route circuit connection. |
| <CopyableCode code="type" /> | `string` | Type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="circuitName, connectionName, peeringName, resourceGroupName, subscriptionId" /> | Gets the specified Express Route Circuit Connection from the specified express route circuit. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="circuitName, peeringName, resourceGroupName, subscriptionId" /> | Gets all global reach connections associated with a private peering in an express route circuit. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="circuitName, connectionName, peeringName, resourceGroupName, subscriptionId" /> | Creates or updates a Express Route Circuit Connection in the specified express route circuits. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="circuitName, connectionName, peeringName, resourceGroupName, subscriptionId" /> | Deletes the specified Express Route Circuit Connection from the specified express route circuit. |
