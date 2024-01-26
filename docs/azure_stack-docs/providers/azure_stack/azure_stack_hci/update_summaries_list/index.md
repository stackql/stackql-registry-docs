---
title: update_summaries_list
hide_title: false
hide_table_of_contents: false
keywords:
  - update_summaries_list
  - azure_stack_hci
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>update_summaries_list</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.azure_stack_hci.update_summaries_list</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of Update summaries |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` |
