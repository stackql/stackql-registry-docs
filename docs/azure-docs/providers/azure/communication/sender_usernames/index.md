---
title: sender_usernames
hide_title: false
hide_table_of_contents: false
keywords:
  - sender_usernames
  - communication
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
<tr><td><b>Name</b></td><td><code>sender_usernames</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.communication.sender_usernames</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `domainName, emailServiceName, resourceGroupName, senderUsername, subscriptionId` | Get a valid sender username for a domains resource. |
| `list_by_domains` | `SELECT` | `domainName, emailServiceName, resourceGroupName, subscriptionId` | List all valid sender usernames for a domains resource. |
| `create_or_update` | `INSERT` | `domainName, emailServiceName, resourceGroupName, senderUsername, subscriptionId` | Add a new SenderUsername resource under the parent Domains resource or update an existing SenderUsername resource. |
| `delete` | `DELETE` | `domainName, emailServiceName, resourceGroupName, senderUsername, subscriptionId` | Operation to delete a SenderUsernames resource. |
| `_list_by_domains` | `EXEC` | `domainName, emailServiceName, resourceGroupName, subscriptionId` | List all valid sender usernames for a domains resource. |
