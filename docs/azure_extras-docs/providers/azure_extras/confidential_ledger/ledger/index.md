---
title: ledger
hide_title: false
hide_table_of_contents: false
keywords:
  - ledger
  - confidential_ledger
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.confidential_ledger.ledger</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource Id for the resource. |
| `name` | `string` | Name of the Resource. |
| `tags` | `object` | Additional tags for Confidential Ledger |
| `type` | `string` | The type of the resource. |
| `location` | `string` | The Azure location where the Confidential Ledger is running. |
| `properties` | `object` | Additional Confidential Ledger properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Ledger_Get` | `SELECT` | `ledgerName, resourceGroupName, subscriptionId` | Retrieves the properties of a Confidential Ledger. |
| `Ledger_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieves the properties of all Confidential Ledgers. |
| `Ledger_ListBySubscription` | `SELECT` | `subscriptionId` | Retrieves the properties of all Confidential Ledgers. |
| `Ledger_Create` | `INSERT` | `ledgerName, resourceGroupName, subscriptionId` | Creates a  Confidential Ledger with the specified ledger parameters. |
| `Ledger_Delete` | `DELETE` | `ledgerName, resourceGroupName, subscriptionId` | Deletes an existing Confidential Ledger. |
| `Ledger_Update` | `EXEC` | `ledgerName, resourceGroupName, subscriptionId` | Updates properties of Confidential Ledger |
