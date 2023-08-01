---
title: network_experiment_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - network_experiment_profiles
  - front_door
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
<tr><td><b>Name</b></td><td><code>network_experiment_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.front_door.network_experiment_profiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | Gets a unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Defines the properties of an experiment |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NetworkExperimentProfiles_Get` | `SELECT` | `profileName, resourceGroupName, subscriptionId` |  |
| `NetworkExperimentProfiles_List` | `SELECT` | `subscriptionId` |  |
| `NetworkExperimentProfiles_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` |  |
| `NetworkExperimentProfiles_CreateOrUpdate` | `INSERT` | `profileName, resourceGroupName, subscriptionId` |  |
| `NetworkExperimentProfiles_Delete` | `DELETE` | `profileName, resourceGroupName, subscriptionId` |  |
| `NetworkExperimentProfiles_Update` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Updates an NetworkExperimentProfiles |
