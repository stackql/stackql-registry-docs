---
title: application_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - application_definitions
  - solutions
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
<tr><td><b>Name</b></td><td><code>application_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.solutions.application_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `managedBy` | `string` | ID of the resource that manages this resource. |
| `properties` | `object` | The managed application definition properties. |
| `sku` | `object` | SKU for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApplicationDefinitions_Get` | `SELECT` | `applicationDefinitionName, resourceGroupName, subscriptionId` | Gets the managed application definition. |
| `ApplicationDefinitions_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the managed application definitions in a resource group. |
| `ApplicationDefinitions_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all the application definitions within a subscription. |
| `ApplicationDefinitions_CreateOrUpdate` | `INSERT` | `applicationDefinitionName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a managed application definition. |
| `ApplicationDefinitions_Delete` | `DELETE` | `applicationDefinitionName, resourceGroupName, subscriptionId` | Deletes the managed application definition. |
| `ApplicationDefinitions_Update` | `EXEC` | `applicationDefinitionName, resourceGroupName, subscriptionId` | Updates the managed application definition. |
