---
title: afd_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - afd_endpoints
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
<tr><td><b>Name</b></td><td><code>afd_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.afd_endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The JSON object that contains the properties required to create an endpoint. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AFDEndpoints_Get` | `SELECT` | `endpointName, profileName, resourceGroupName, subscriptionId` | Gets an existing AzureFrontDoor endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| `AFDEndpoints_ListByProfile` | `SELECT` | `profileName, resourceGroupName, subscriptionId` | Lists existing AzureFrontDoor endpoints. |
| `AFDEndpoints_Create` | `INSERT` | `endpointName, profileName, resourceGroupName, subscriptionId` | Creates a new AzureFrontDoor endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| `AFDEndpoints_Delete` | `DELETE` | `endpointName, profileName, resourceGroupName, subscriptionId` | Deletes an existing AzureFrontDoor endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| `AFDEndpoints_ListResourceUsage` | `EXEC` | `endpointName, profileName, resourceGroupName, subscriptionId` | Checks the quota and actual usage of endpoints under the given CDN profile. |
| `AFDEndpoints_PurgeContent` | `EXEC` | `endpointName, profileName, resourceGroupName, subscriptionId, data__contentPaths` | Removes a content from AzureFrontDoor. |
| `AFDEndpoints_Update` | `EXEC` | `endpointName, profileName, resourceGroupName, subscriptionId` | Updates an existing AzureFrontDoor endpoint with the specified endpoint name under the specified subscription, resource group and profile. Only tags can be updated after creating an endpoint. To update origins, use the Update Origin operation. To update origin groups, use the Update Origin group operation. To update domains, use the Update Custom Domain operation. |
| `AFDEndpoints_ValidateCustomDomain` | `EXEC` | `endpointName, profileName, resourceGroupName, subscriptionId, data__hostName` | Validates the custom domain mapping to ensure it maps to the correct CDN endpoint in DNS. |
