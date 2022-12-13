---
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
  - cdn
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
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.routes</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Routes_Get` | `SELECT` | `endpointName, profileName, resourceGroupName, routeName, subscriptionId` | Gets an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint. |
| `Routes_ListByEndpoint` | `SELECT` | `endpointName, profileName, resourceGroupName, subscriptionId` | Lists all of the existing origins within a profile. |
| `Routes_Create` | `INSERT` | `endpointName, profileName, resourceGroupName, routeName, subscriptionId` | Creates a new route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint. |
| `Routes_Delete` | `DELETE` | `endpointName, profileName, resourceGroupName, routeName, subscriptionId` | Deletes an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint. |
| `Routes_Update` | `EXEC` | `endpointName, profileName, resourceGroupName, routeName, subscriptionId` | Updates an existing route with the specified route name under the specified subscription, resource group, profile, and AzureFrontDoor endpoint. |
