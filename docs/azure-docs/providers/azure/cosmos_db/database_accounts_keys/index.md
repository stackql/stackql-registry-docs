---
title: database_accounts_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - database_accounts_keys
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>database_accounts_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.database_accounts_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `primaryMasterKey` | `string` | Base 64 encoded value of the primary read-write key. |
| `primaryReadonlyMasterKey` | `string` | Base 64 encoded value of the primary read-only key. |
| `secondaryMasterKey` | `string` | Base 64 encoded value of the secondary read-write key. |
| `secondaryReadonlyMasterKey` | `string` | Base 64 encoded value of the secondary read-only key. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `accountName, resourceGroupName, subscriptionId` |
