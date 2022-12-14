---
title: batch_deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - batch_deployments
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
<tr><td><b>Name</b></td><td><code>batch_deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_services.batch_deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `kind` | `string` | Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Batch inference settings per deployment. |
| `sku` | `object` | The resource model definition representing SKU |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `BatchDeployments_Get` | `SELECT` | `deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName` |
| `BatchDeployments_List` | `SELECT` | `endpointName, resourceGroupName, subscriptionId, workspaceName` |
| `BatchDeployments_CreateOrUpdate` | `INSERT` | `deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName, data__location, data__properties` |
| `BatchDeployments_Delete` | `DELETE` | `deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName` |
| `BatchDeployments_Update` | `EXEC` | `deploymentName, endpointName, resourceGroupName, subscriptionId, workspaceName` |
