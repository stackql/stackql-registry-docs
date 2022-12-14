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
| `IntegrationServiceEnvironments_Get` | `SELECT` | `api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId` | Gets an integration service environment. |
| `IntegrationServiceEnvironments_ListByResourceGroup` | `SELECT` | `api-version, resourceGroup, subscriptionId` | Gets a list of integration service environments by resource group. |
| `IntegrationServiceEnvironments_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Gets a list of integration service environments by subscription. |
| `IntegrationServiceEnvironments_CreateOrUpdate` | `INSERT` | `api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId` | Creates or updates an integration service environment. |
| `IntegrationServiceEnvironments_Delete` | `DELETE` | `api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId` | Deletes an integration service environment. |
| `IntegrationServiceEnvironments_Restart` | `EXEC` | `api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId` | Restarts an integration service environment. |
| `IntegrationServiceEnvironments_Update` | `EXEC` | `api-version, integrationServiceEnvironmentName, resourceGroup, subscriptionId` | Updates an integration service environment. |
