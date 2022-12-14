---
title: database_blob_auditing_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - database_blob_auditing_policies
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
<tr><td><b>Name</b></td><td><code>database_blob_auditing_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.database_blob_auditing_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a database blob auditing policy. |
| `kind` | `string` | Resource kind. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DatabaseBlobAuditingPolicies_Get` | `SELECT` | `blobAuditingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId` | Gets a database's blob auditing policy. |
| `DatabaseBlobAuditingPolicies_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Lists auditing settings of a database. |
| `DatabaseBlobAuditingPolicies_CreateOrUpdate` | `INSERT` | `blobAuditingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId` | Creates or updates a database's blob auditing policy. |
