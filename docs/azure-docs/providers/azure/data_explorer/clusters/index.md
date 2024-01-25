---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
  - data_explorer
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_explorer.clusters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Class representing the Kusto cluster properties. |
| `sku` | `object` | Azure SKU definition. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `zones` | `array` | An array represents the availability zones of the cluster. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets a Kusto cluster. |
| `list` | `SELECT` | `subscriptionId` | Lists all Kusto clusters within a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Kusto clusters within a resource group. |
| `create_or_update` | `INSERT` | `clusterName, resourceGroupName, subscriptionId, data__sku` | Create or update a Kusto cluster. |
| `delete` | `DELETE` | `clusterName, resourceGroupName, subscriptionId` | Deletes a Kusto cluster. |
| `_list` | `EXEC` | `subscriptionId` | Lists all Kusto clusters within a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all Kusto clusters within a resource group. |
| `add_language_extensions` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Add a list of language extensions that can run within KQL queries. |
| `check_name_availability` | `EXEC` | `location, subscriptionId, data__name, data__type` | Checks that the cluster name is valid and is not already in use. |
| `detach_follower_databases` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, data__attachedDatabaseConfigurationName, data__clusterResourceId` | Detaches all followers of a database owned by this cluster. |
| `diagnose_virtual_network` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Diagnoses network connectivity status for external resources on which the service is dependent on. |
| `migrate` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, data__clusterResourceId` | Migrate data from a Kusto cluster to another cluster. |
| `remove_language_extensions` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Remove a list of language extensions that can run within KQL queries. |
| `start` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Starts a Kusto cluster. |
| `stop` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Stops a Kusto cluster. |
| `update` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Update a Kusto cluster. |
