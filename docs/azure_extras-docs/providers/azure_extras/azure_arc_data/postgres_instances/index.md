---
title: postgres_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - postgres_instances
  - azure_arc_data
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
<tr><td><b>Name</b></td><td><code>postgres_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.azure_arc_data.postgres_instances</code></td></tr>
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
| `PostgresInstances_Get` | `SELECT` | `api-version, postgresInstanceName, resourceGroupName, subscriptionId` | Retrieves a postgres Instance resource |
| `PostgresInstances_List` | `SELECT` | `api-version, subscriptionId` |  |
| `PostgresInstances_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Get a postgres Instances list by Resource group name. |
| `PostgresInstances_Create` | `INSERT` | `api-version, postgresInstanceName, resourceGroupName, subscriptionId, data__properties` | Creates or replaces a postgres Instance resource |
| `PostgresInstances_Delete` | `DELETE` | `api-version, postgresInstanceName, resourceGroupName, subscriptionId` | Deletes a postgres Instance resource |
| `PostgresInstances_Update` | `EXEC` | `api-version, postgresInstanceName, resourceGroupName, subscriptionId` | Updates a postgres Instance resource |
