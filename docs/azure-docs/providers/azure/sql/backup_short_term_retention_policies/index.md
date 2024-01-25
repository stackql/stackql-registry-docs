---
title: backup_short_term_retention_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_short_term_retention_policies
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
<tr><td><b>Name</b></td><td><code>backup_short_term_retention_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.backup_short_term_retention_policies</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, policyName, resourceGroupName, serverName, subscriptionId` | Gets a database's short term retention policy. |
| `list_by_database` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a database's short term retention policy. |
| `create_or_update` | `INSERT` | `databaseName, policyName, resourceGroupName, serverName, subscriptionId` | Updates a database's short term retention policy. |
| `_list_by_database` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a database's short term retention policy. |
| `update` | `EXEC` | `databaseName, policyName, resourceGroupName, serverName, subscriptionId` | Updates a database's short term retention policy. |
