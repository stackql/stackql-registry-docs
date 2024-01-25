---
title: mongo_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - mongo_clusters
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>mongo_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.mongo_clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of a mongo cluster. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `mongoClusterName, resourceGroupName, subscriptionId` | Gets information about a mongo cluster. |
| `list` | `SELECT` | `subscriptionId` | List all the mongo clusters in a given subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all the mongo clusters in a given resource group. |
| `create_or_update` | `INSERT` | `mongoClusterName, resourceGroupName, subscriptionId` | Create or update a mongo cluster. Update overwrites all properties for the resource. To only modify some of the properties, use PATCH. |
| `delete` | `DELETE` | `mongoClusterName, resourceGroupName, subscriptionId` | Deletes a mongo cluster. |
| `_list` | `EXEC` | `subscriptionId` | List all the mongo clusters in a given subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all the mongo clusters in a given resource group. |
| `check_name_availability` | `EXEC` | `location, subscriptionId` | Check the availability of name for resource |
| `update` | `EXEC` | `mongoClusterName, resourceGroupName, subscriptionId` | Updates an existing mongo cluster. The request body can contain one to many of the properties present in the normal mongo cluster definition. |
