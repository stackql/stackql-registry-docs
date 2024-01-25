---
title: accounts_customer_initiated_migration
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_customer_initiated_migration
  - storage
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
<tr><td><b>Name</b></td><td><code>accounts_customer_initiated_migration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.accounts_customer_initiated_migration</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Migration Resource Id |
| `name` | `string` | current value is 'default' for customer initiated migration |
| `properties` | `object` | The properties of a storage account’s ongoing or enqueued migration. |
| `type` | `string` | SrpAccountMigrationType in ARM contract which is 'accountMigrations' |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `accountName, migrationName, resourceGroupName, subscriptionId` |
