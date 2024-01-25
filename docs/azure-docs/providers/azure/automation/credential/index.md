---
title: credential
hide_title: false
hide_table_of_contents: false
keywords:
  - credential
  - automation
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
<tr><td><b>Name</b></td><td><code>credential</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.credential</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationAccountName, credentialName, resourceGroupName, subscriptionId` | Retrieve the credential identified by credential name. |
| `list_by_automation_account` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of credentials. |
| `create_or_update` | `INSERT` | `automationAccountName, credentialName, resourceGroupName, subscriptionId, data__name, data__properties` | Create a credential. |
| `delete` | `DELETE` | `automationAccountName, credentialName, resourceGroupName, subscriptionId` | Delete the credential. |
| `_list_by_automation_account` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of credentials. |
| `update` | `EXEC` | `automationAccountName, credentialName, resourceGroupName, subscriptionId` | Update a credential. |
