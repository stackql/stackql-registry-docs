---
title: online_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - online_deployments
  - machine_learning_services
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>online_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_services.online_deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `OnlineDeployments_Get` | `SELECT` | `deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName` |
| `OnlineDeployments_List` | `SELECT` | `endpointName, resourceGroupName, subscriptionId, workspaceName` |
| `OnlineDeployments_CreateOrUpdate` | `INSERT` | `deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName, data__location, data__properties` |
| `OnlineDeployments_Delete` | `DELETE` | `deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName` |
| `OnlineDeployments_GetLogs` | `EXEC` | `deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName` |
| `OnlineDeployments_ListSkus` | `EXEC` | `deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName` |
| `OnlineDeployments_Update` | `EXEC` | `deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName` |
