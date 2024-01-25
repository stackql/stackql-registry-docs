---
title: ledger
hide_title: false
hide_table_of_contents: false
keywords:
  - ledger
  - confidential_ledger
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
<tr><td><b>Name</b></td><td><code>ledger</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.confidential_ledger.ledger</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Additional Confidential Ledger properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `ledgerName, resourceGroupName, subscriptionId` | Retrieves the properties of a Confidential Ledger. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieves the properties of all Confidential Ledgers. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Retrieves the properties of all Confidential Ledgers. |
| `create` | `INSERT` | `ledgerName, resourceGroupName, subscriptionId` | Creates a  Confidential Ledger with the specified ledger parameters. |
| `delete` | `DELETE` | `ledgerName, resourceGroupName, subscriptionId` | Deletes an existing Confidential Ledger. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Retrieves the properties of all Confidential Ledgers. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Retrieves the properties of all Confidential Ledgers. |
| `backup` | `EXEC` | `ledgerName, resourceGroupName, subscriptionId, data__uri` | Backs up a Confidential Ledger Resource. |
| `restore` | `EXEC` | `ledgerName, resourceGroupName, subscriptionId, data__fileShareName, data__restoreRegion, data__uri` | Restores a Confidential Ledger Resource. |
| `update` | `EXEC` | `ledgerName, resourceGroupName, subscriptionId` | Updates properties of Confidential Ledger |
