---
title: vh_ds
hide_title: false
hide_table_of_contents: false
keywords:
  - vh_ds
  - test_base
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
<tr><td><b>Name</b></td><td><code>vh_ds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.vh_ds</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, testBaseAccountName, vhdName` | Gets a Test Base VHD. |
| `list_by_test_base_account` | `SELECT` | `resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the VHDs under a test base account. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, testBaseAccountName, vhdName` | Deletes a Test Base VHD. |
| `_list_by_test_base_account` | `EXEC` | `resourceGroupName, subscriptionId, testBaseAccountName` | Lists all the VHDs under a test base account. |
