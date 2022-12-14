---
title: integration_account_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_maps
  - logic_apps
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
<tr><td><b>Name</b></td><td><code>integration_account_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.integration_account_maps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `type` | `string` | Gets the resource type. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The integration account map. |
| `tags` | `object` | The resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IntegrationAccountMaps_Get` | `SELECT` | `api-version, integrationAccountName, mapName, resourceGroupName, subscriptionId` | Gets an integration account map. |
| `IntegrationAccountMaps_List` | `SELECT` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Gets a list of integration account maps. |
| `IntegrationAccountMaps_CreateOrUpdate` | `INSERT` | `api-version, integrationAccountName, mapName, resourceGroupName, subscriptionId, data__properties` | Creates or updates an integration account map. If the map is larger than 4 MB, you need to store the map in an Azure blob and use the blob's Shared Access Signature (SAS) URL as the 'contentLink' property value. |
| `IntegrationAccountMaps_Delete` | `DELETE` | `api-version, integrationAccountName, mapName, resourceGroupName, subscriptionId` | Deletes an integration account map. |
| `IntegrationAccountMaps_ListContentCallbackUrl` | `EXEC` | `api-version, integrationAccountName, mapName, resourceGroupName, subscriptionId` | Get the content callback url. |
