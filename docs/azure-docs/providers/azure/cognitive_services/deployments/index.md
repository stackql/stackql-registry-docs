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
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Deployments_Get` | `SELECT` | `accountName, deploymentName, resourceGroupName, subscriptionId` | Gets the specified deployments associated with the Cognitive Services account. |
| `Deployments_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the deployments associated with the Cognitive Services account. |
| `Deployments_CreateOrUpdate` | `INSERT` | `accountName, deploymentName, resourceGroupName, subscriptionId` | Update the state of specified deployments associated with the Cognitive Services account. |
| `Deployments_Delete` | `DELETE` | `accountName, deploymentName, resourceGroupName, subscriptionId` | Deletes the specified deployment associated with the Cognitive Services account. |
