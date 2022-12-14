---
title: management_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - management_associations
  - operations_management
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
<tr><td><b>Name</b></td><td><code>management_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operations_management.management_associations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `location` | `string` | Resource location |
| `properties` | `object` | ManagementAssociation properties supported by the OperationsManagement resource provider. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagementAssociations_Get` | `SELECT` | `managementAssociationName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId` | Retrieves the user ManagementAssociation. |
| `ManagementAssociations_ListBySubscription` | `SELECT` | `subscriptionId` | Retrieves the ManagementAssociations list. |
| `ManagementAssociations_CreateOrUpdate` | `INSERT` | `managementAssociationName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId` | Creates or updates the ManagementAssociation. |
| `ManagementAssociations_Delete` | `DELETE` | `managementAssociationName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId` | Deletes the ManagementAssociation in the subscription. |
