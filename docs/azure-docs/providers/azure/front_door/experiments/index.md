---
title: experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - experiments
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
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.front_door.experiments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Defines the properties of an experiment |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `experimentName, profileName, resourceGroupName, subscriptionId` |  |
| `list_by_profile` | `SELECT` | `profileName, resourceGroupName, subscriptionId` |  |
| `create_or_update` | `INSERT` | `experimentName, profileName, resourceGroupName, subscriptionId` |  |
| `delete` | `DELETE` | `experimentName, profileName, resourceGroupName, subscriptionId` |  |
| `_list_by_profile` | `EXEC` | `profileName, resourceGroupName, subscriptionId` |  |
| `update` | `EXEC` | `experimentName, profileName, resourceGroupName, subscriptionId` | Updates an Experiment |
