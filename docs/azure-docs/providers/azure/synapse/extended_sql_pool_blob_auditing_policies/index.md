---
title: extended_sql_pool_blob_auditing_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - extended_sql_pool_blob_auditing_policies
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
<tr><td><b>Name</b></td><td><code>extended_sql_pool_blob_auditing_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.extended_sql_pool_blob_auditing_policies</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `blobAuditingPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Gets an extended Sql pool's blob auditing policy. |
| `list_by_sql_pool` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Lists extended auditing settings of a Sql pool. |
| `create_or_update` | `INSERT` | `blobAuditingPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Creates or updates an extended Sql pool's blob auditing policy. |
| `_list_by_sql_pool` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Lists extended auditing settings of a Sql pool. |
