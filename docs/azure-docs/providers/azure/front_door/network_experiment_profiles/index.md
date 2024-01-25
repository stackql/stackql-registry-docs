---
title: network_experiment_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - network_experiment_profiles
  - front_door
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
<tr><td><b>Name</b></td><td><code>network_experiment_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.front_door.network_experiment_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | Gets a unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Defines the properties of an experiment |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `profileName, resourceGroupName, subscriptionId` |  |
| `list` | `SELECT` | `subscriptionId` |  |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` |  |
| `create_or_update` | `INSERT` | `profileName, resourceGroupName, subscriptionId` |  |
| `delete` | `DELETE` | `profileName, resourceGroupName, subscriptionId` |  |
| `_list` | `EXEC` | `subscriptionId` |  |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` |  |
| `update` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Updates an NetworkExperimentProfiles |
