---
title: attached_database_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - attached_database_configurations
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
<tr><td><b>Name</b></td><td><code>attached_database_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_explorer.attached_database_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location. |
| `properties` | `object` | Class representing the an attached database configuration properties of kind specific. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `attachedDatabaseConfigurationName, clusterName, resourceGroupName, subscriptionId` | Returns an attached database configuration. |
| `list_by_cluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Returns the list of attached database configurations of the given Kusto cluster. |
| `create_or_update` | `INSERT` | `attachedDatabaseConfigurationName, clusterName, resourceGroupName, subscriptionId` | Creates or updates an attached database configuration. |
| `delete` | `DELETE` | `attachedDatabaseConfigurationName, clusterName, resourceGroupName, subscriptionId` | Deletes the attached database configuration with the given name. |
| `_list_by_cluster` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Returns the list of attached database configurations of the given Kusto cluster. |
| `check_name_availability` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, data__name, data__type` | Checks that the attached database configuration resource name is valid and is not already in use. |
