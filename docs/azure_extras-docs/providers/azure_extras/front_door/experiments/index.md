---
title: experiments
hide_title: false
hide_table_of_contents: false
keywords:
  - experiments
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
<tr><td><b>Name</b></td><td><code>experiments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.front_door.experiments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Defines the properties of an experiment |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Experiments_Get` | `SELECT` | `experimentName, profileName, resourceGroupName, subscriptionId` |  |
| `Experiments_ListByProfile` | `SELECT` | `profileName, resourceGroupName, subscriptionId` |  |
| `Experiments_CreateOrUpdate` | `INSERT` | `experimentName, profileName, resourceGroupName, subscriptionId` |  |
| `Experiments_Delete` | `DELETE` | `experimentName, profileName, resourceGroupName, subscriptionId` |  |
| `Experiments_Update` | `EXEC` | `experimentName, profileName, resourceGroupName, subscriptionId` | Updates an Experiment |
