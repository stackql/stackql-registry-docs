---
title: storage_task_assignment
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_task_assignment
  - storageactions
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
<tr><td><b>Name</b></td><td><code>storage_task_assignment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storageactions.storage_task_assignment</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, storageTaskName, subscriptionId` |
| `_list` | `EXEC` | `resourceGroupName, storageTaskName, subscriptionId` |
