---
title: linked_services
hide_title: false
hide_table_of_contents: false
keywords:
  - linked_services
  - operational_insights
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
<tr><td><b>Name</b></td><td><code>linked_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operational_insights.linked_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Linked service properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LinkedServices_Get` | `SELECT` | `linkedServiceName, resourceGroupName, subscriptionId, workspaceName` | Gets a linked service instance. |
| `LinkedServices_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets the linked services instances in a workspace. |
| `LinkedServices_CreateOrUpdate` | `INSERT` | `linkedServiceName, resourceGroupName, subscriptionId, workspaceName, data__properties` | Create or update a linked service. |
| `LinkedServices_Delete` | `DELETE` | `linkedServiceName, resourceGroupName, subscriptionId, workspaceName` | Deletes a linked service instance. |
