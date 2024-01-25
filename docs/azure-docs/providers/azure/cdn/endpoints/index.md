---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - endpoints
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
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.endpoints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location. |
| `properties` | `object` | The JSON object that contains the properties required to create an endpoint. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `endpointName, profileName, resourceGroupName, subscriptionId` | Gets an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| `list_by_profile` | `SELECT` | `profileName, resourceGroupName, subscriptionId` | Lists existing CDN endpoints. |
| `create` | `INSERT` | `endpointName, profileName, resourceGroupName, subscriptionId` | Creates a new CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| `delete` | `DELETE` | `endpointName, profileName, resourceGroupName, subscriptionId` | Deletes an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. |
| `_list_by_profile` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Lists existing CDN endpoints. |
| `load_content` | `EXEC` | `endpointName, profileName, resourceGroupName, subscriptionId, data__contentPaths` | Pre-loads a content to CDN. Available for Verizon Profiles. |
| `purge_content` | `EXEC` | `endpointName, profileName, resourceGroupName, subscriptionId, data__contentPaths` | Removes a content from CDN. |
| `start` | `EXEC` | `endpointName, profileName, resourceGroupName, subscriptionId` | Starts an existing CDN endpoint that is on a stopped state. |
| `stop` | `EXEC` | `endpointName, profileName, resourceGroupName, subscriptionId` | Stops an existing running CDN endpoint. |
| `update` | `EXEC` | `endpointName, profileName, resourceGroupName, subscriptionId` | Updates an existing CDN endpoint with the specified endpoint name under the specified subscription, resource group and profile. Only tags can be updated after creating an endpoint. To update origins, use the Update Origin operation. To update origin groups, use the Update Origin group operation. To update custom domains, use the Update Custom Domain operation. |
| `validate_custom_domain` | `EXEC` | `endpointName, profileName, resourceGroupName, subscriptionId, data__hostName` | Validates the custom domain mapping to ensure it maps to the correct CDN endpoint in DNS. |
