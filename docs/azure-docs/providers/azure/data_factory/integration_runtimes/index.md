---
title: integration_runtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtimes
  - data_factory
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
<tr><td><b>Name</b></td><td><code>integration_runtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.integration_runtimes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `etag` | `string` | Etag identifies change in the resource. |
| `properties` | `object` | Azure Data Factory nested object which serves as a compute resource for activities. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Gets an integration runtime. |
| `list_by_factory` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists integration runtimes. |
| `create_or_update` | `INSERT` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId, data__properties` | Creates or updates an integration runtime. |
| `delete` | `DELETE` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Deletes an integration runtime. |
| `_list_by_factory` | `EXEC` | `api-version, factoryName, resourceGroupName, subscriptionId` | Lists integration runtimes. |
| `regenerate_auth_key` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Regenerates the authentication key for an integration runtime. |
| `remove_links` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId, data__factoryName` | Remove all linked integration runtimes under specific data factory in a self-hosted integration runtime. |
| `start` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Starts a ManagedReserved type integration runtime. |
| `stop` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Stops a ManagedReserved type integration runtime. |
| `sync_credentials` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Force the integration runtime to synchronize credentials across integration runtime nodes, and this will override the credentials across all worker nodes with those available on the dispatcher node. If you already have the latest credential backup file, you should manually import it (preferred) on any self-hosted integration runtime node than using this API directly. |
| `update` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Updates an integration runtime. |
| `upgrade` | `EXEC` | `api-version, factoryName, integrationRuntimeName, resourceGroupName, subscriptionId` | Upgrade self-hosted integration runtime to latest version if availability. |
