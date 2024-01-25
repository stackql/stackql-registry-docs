---
title: experiments_all_statuses
hide_title: false
hide_table_of_contents: false
keywords:
  - experiments_all_statuses
  - chaos
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
<tr><td><b>Name</b></td><td><code>experiments_all_statuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.chaos.experiments_all_statuses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | String of the fully qualified resource ID. |
| `name` | `string` | String of the resource name. |
| `properties` | `object` | Model that represents the Experiment status properties model. |
| `type` | `string` | String of the resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `api-version, experimentName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `api-version, experimentName, resourceGroupName, subscriptionId` |
