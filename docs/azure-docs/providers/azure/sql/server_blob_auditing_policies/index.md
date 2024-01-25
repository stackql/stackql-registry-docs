---
title: server_blob_auditing_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - server_blob_auditing_policies
  - sql
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
<tr><td><b>Name</b></td><td><code>server_blob_auditing_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_blob_auditing_policies</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `blobAuditingPolicyName, resourceGroupName, serverName, subscriptionId` | Gets a server's blob auditing policy. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Lists auditing settings of a server. |
| `create_or_update` | `INSERT` | `blobAuditingPolicyName, resourceGroupName, serverName, subscriptionId` | Creates or updates a server's blob auditing policy. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Lists auditing settings of a server. |
