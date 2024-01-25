---
title: kusto_pool_attached_database_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pool_attached_database_configurations
  - synapse
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
<tr><td><b>Name</b></td><td><code>kusto_pool_attached_database_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.kusto_pool_attached_database_configurations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location. |
| `properties` | `object` | Class representing the an attached database configuration properties of kind specific. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `attachedDatabaseConfigurationName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Returns an attached database configuration. |
| `list_by_kusto_pool` | `SELECT` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Returns the list of attached database configurations of the given Kusto Pool. |
| `create_or_update` | `INSERT` | `attachedDatabaseConfigurationName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Creates or updates an attached database configuration. |
| `delete` | `DELETE` | `attachedDatabaseConfigurationName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Deletes the attached database configuration with the given name. |
| `_list_by_kusto_pool` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Returns the list of attached database configurations of the given Kusto Pool. |
