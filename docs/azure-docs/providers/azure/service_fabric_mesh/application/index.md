---
title: application
hide_title: false
hide_table_of_contents: false
keywords:
  - application
  - service_fabric_mesh
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
<tr><td><b>Name</b></td><td><code>application</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_mesh.application</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | This type describes properties of an application resource. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Application_Get` | `SELECT` | `api-version, applicationResourceName, resourceGroupName, subscriptionId` | Gets the information about the application resource with the given name. The information include the description and other properties of the application. |
| `Application_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Gets the information about all application resources in a given resource group. The information include the description and other properties of the Application. |
| `Application_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Gets the information about all application resources in a given resource group. The information include the description and other properties of the application. |
| `Application_Create` | `INSERT` | `api-version, applicationResourceName, resourceGroupName, subscriptionId, data__properties` | Creates an application resource with the specified name, description and properties. If an application resource with the same name exists, then it is updated with the specified description and properties. |
| `Application_Delete` | `DELETE` | `api-version, applicationResourceName, resourceGroupName, subscriptionId` | Deletes the application resource identified by the name. |
