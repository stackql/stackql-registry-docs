---
title: chat_sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - chat_sessions
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
<tr><td><b>Name</b></td><td><code>chat_sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.test_base.chat_sessions</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `chatSessionName, resourceGroupName, subscriptionId, testBaseAccountName` | Get a chat session |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, testBaseAccountName` | List all chat sessions |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, testBaseAccountName` | List all chat sessions |
