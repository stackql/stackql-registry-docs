---
title: postgres_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_instances
  - azure_arc_data
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
<tr><td><b>Name</b></td><td><code>postgres_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.azure_arc_data.postgres_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | The complex type of the extended location. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Postgres Instance properties. |
| `sku` | `object` | The resource model definition representing SKU for Azure Database for PostgresSQL - Azure Arc |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, postgresInstanceName, resourceGroupName, subscriptionId` | Retrieves a postgres Instance resource |
| `list` | `SELECT` | `api-version, subscriptionId` |  |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Get a postgres Instances list by Resource group name. |
| `create` | `INSERT` | `api-version, postgresInstanceName, resourceGroupName, subscriptionId, data__properties` | Creates or replaces a postgres Instance resource |
| `delete` | `DELETE` | `api-version, postgresInstanceName, resourceGroupName, subscriptionId` | Deletes a postgres Instance resource |
| `_list` | `EXEC` | `api-version, subscriptionId` |  |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Get a postgres Instances list by Resource group name. |
| `update` | `EXEC` | `api-version, postgresInstanceName, resourceGroupName, subscriptionId` | Updates a postgres Instance resource |
