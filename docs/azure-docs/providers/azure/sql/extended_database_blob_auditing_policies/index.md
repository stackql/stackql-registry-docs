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
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExtendedDatabaseBlobAuditingPolicies_Get` | `SELECT` | `blobAuditingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId` | Gets an extended database's blob auditing policy. |
| `ExtendedDatabaseBlobAuditingPolicies_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Lists extended auditing settings of a database. |
| `ExtendedDatabaseBlobAuditingPolicies_CreateOrUpdate` | `INSERT` | `blobAuditingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId` | Creates or updates an extended database's blob auditing policy. |
