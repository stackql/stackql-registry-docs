---
title: extended_database_blob_auditing_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - extended_database_blob_auditing_policies
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
<tr><td><b>Name</b></td><td><code>extended_database_blob_auditing_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.extended_database_blob_auditing_policies</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `blobAuditingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId` | Gets an extended database's blob auditing policy. |
| `list_by_database` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Lists extended auditing settings of a database. |
| `create_or_update` | `INSERT` | `blobAuditingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId` | Creates or updates an extended database's blob auditing policy. |
| `_list_by_database` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Lists extended auditing settings of a database. |
