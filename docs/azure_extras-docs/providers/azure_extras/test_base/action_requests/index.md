---
title: action_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - action_requests
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
<tr><td><b>Name</b></td><td><code>action_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.action_requests</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `actionRequestName, resourceGroupName, subscriptionId, testBaseAccountName` | Get the action request under the specified test base account. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, testBaseAccountName` | List all action requests under the specified test base account. |
| `delete` | `DELETE` | `actionRequestName, resourceGroupName, subscriptionId, testBaseAccountName` | Delete (revoke) an action request. Only requests in review can be deleted. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, testBaseAccountName` | List all action requests under the specified test base account. |
| `put` | `EXEC` | `actionRequestName, resourceGroupName, subscriptionId, testBaseAccountName` | Create (submit) an action request. |
