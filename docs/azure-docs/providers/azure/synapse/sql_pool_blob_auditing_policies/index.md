---
title: sql_pool_blob_auditing_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_blob_auditing_policies
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
<tr><td><b>Name</b></td><td><code>sql_pool_blob_auditing_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_blob_auditing_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Resource kind. |
| `properties` | `object` | Properties of a Sql pool blob auditing policy. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlPoolBlobAuditingPolicies_Get` | `SELECT` | `blobAuditingPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get a SQL pool's blob auditing policy. |
| `SqlPoolBlobAuditingPolicies_ListBySqlPool` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Lists auditing settings of a Sql pool. |
| `SqlPoolBlobAuditingPolicies_CreateOrUpdate` | `INSERT` | `blobAuditingPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Creates or updates a SQL pool's blob auditing policy. |
