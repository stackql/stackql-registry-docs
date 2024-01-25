---
title: libraries
hide_title: false
hide_table_of_contents: false
keywords:
  - libraries
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
<tr><td><b>Name</b></td><td><code>libraries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.libraries</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` |
