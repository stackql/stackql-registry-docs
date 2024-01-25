---
title: integration_service_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_service_environments
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
<tr><td><b>Name</b></td><td><code>integration_service_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.integration_service_environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `identity` | `object` | Managed service identity properties. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The integration service environment properties. |
| `sku` | `object` | The integration service environment sku. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | Gets the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId` | Gets an integration service environment. |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroup, subscriptionId` | Gets a list of integration service environments by resource group. |
| `list_by_subscription` | `SELECT` | `api-version, subscriptionId` | Gets a list of integration service environments by subscription. |
| `create_or_update` | `INSERT` | `api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId` | Creates or updates an integration service environment. |
| `delete` | `DELETE` | `api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId` | Deletes an integration service environment. |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroup, subscriptionId` | Gets a list of integration service environments by resource group. |
| `_list_by_subscription` | `EXEC` | `api-version, subscriptionId` | Gets a list of integration service environments by subscription. |
| `restart` | `EXEC` | `api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId` | Restarts an integration service environment. |
| `update` | `EXEC` | `api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId` | Updates an integration service environment. |
