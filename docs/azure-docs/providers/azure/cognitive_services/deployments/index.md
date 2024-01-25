---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - cognitive_services
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
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cognitive_services.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Resource Etag. |
| `properties` | `object` | Properties of Cognitive Services account deployment. |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, deploymentName, resourceGroupName, subscriptionId` | Gets the specified deployments associated with the Cognitive Services account. |
| `list` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the deployments associated with the Cognitive Services account. |
| `create_or_update` | `INSERT` | `accountName, deploymentName, resourceGroupName, subscriptionId` | Update the state of specified deployments associated with the Cognitive Services account. |
| `delete` | `DELETE` | `accountName, deploymentName, resourceGroupName, subscriptionId` | Deletes the specified deployment associated with the Cognitive Services account. |
| `_list` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Gets the deployments associated with the Cognitive Services account. |
| `update` | `EXEC` | `accountName, deploymentName, resourceGroupName, subscriptionId` | Update specified deployments associated with the Cognitive Services account. |
