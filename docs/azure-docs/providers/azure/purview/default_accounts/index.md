---
title: default_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - default_accounts
  - purview
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
<tr><td><b>Name</b></td><td><code>default_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.purview.default_accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `scopeType` | `string` | The scope where the default account is set. |
| `subscriptionId` | `string` | The subscription ID of the account that is set as the default. |
| `accountName` | `string` | The name of the account that is set as the default. |
| `resourceGroupName` | `string` | The resource group name of the account that is set as the default. |
| `scope` | `string` | The scope object ID. For example, sub ID or tenant ID. |
| `scopeTenantId` | `string` | The scope tenant in which the default account is set. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DefaultAccounts_Get` | `SELECT` | `api-version, scopeTenantId, scopeType` | Get the default account for the scope. |
| `DefaultAccounts_Remove` | `EXEC` | `api-version, scopeTenantId, scopeType` | Removes the default account from the scope. |
| `DefaultAccounts_Set` | `EXEC` | `api-version` | Sets the default account for the scope. |
