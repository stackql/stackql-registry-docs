---
title: managed_backup_short_term_retention_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_backup_short_term_retention_policies
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
<tr><td><b>Name</b></td><td><code>managed_backup_short_term_retention_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_backup_short_term_retention_policies</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedBackupShortTermRetentionPolicies_Get` | `SELECT` | `databaseName, managedInstanceName, policyName, resourceGroupName, subscriptionId` | Gets a managed database's short term retention policy. |
| `ManagedBackupShortTermRetentionPolicies_ListByDatabase` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | Gets a managed database's short term retention policy list. |
| `ManagedBackupShortTermRetentionPolicies_CreateOrUpdate` | `INSERT` | `databaseName, managedInstanceName, policyName, resourceGroupName, subscriptionId` | Updates a managed database's short term retention policy. |
| `ManagedBackupShortTermRetentionPolicies_Update` | `EXEC` | `databaseName, managedInstanceName, policyName, resourceGroupName, subscriptionId` | Updates a managed database's short term retention policy. |
