---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - nginx
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.nginx.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` |  |
| `type` | `string` |  |
| `sku` | `object` |  |
| `properties` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `identity` | `object` |  |
| `location` | `string` |  |
| `tags` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Deployments_Get` | `SELECT` | `deploymentName, resourceGroupName, subscriptionId` |
| `Deployments_List` | `SELECT` | `subscriptionId` |
| `Deployments_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |
| `Deployments_Create` | `INSERT` | `deploymentName, resourceGroupName, subscriptionId` |
| `Deployments_Delete` | `DELETE` | `deploymentName, resourceGroupName, subscriptionId` |
| `Deployments_Update` | `EXEC` | `deploymentName, resourceGroupName, subscriptionId` |
