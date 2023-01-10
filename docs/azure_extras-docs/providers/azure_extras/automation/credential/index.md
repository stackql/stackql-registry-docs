---
title: credential
hide_title: false
hide_table_of_contents: false
keywords:
  - credential
  - automation
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
<tr><td><b>Name</b></td><td><code>credential</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.credential</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Credential_Get` | `SELECT` | `automationAccountName, credentialName, resourceGroupName, subscriptionId` | Retrieve the credential identified by credential name. |
| `Credential_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of credentials. |
| `Credential_CreateOrUpdate` | `INSERT` | `automationAccountName, credentialName, resourceGroupName, subscriptionId, data__name, data__properties` | Create a credential. |
| `Credential_Delete` | `DELETE` | `automationAccountName, credentialName, resourceGroupName, subscriptionId` | Delete the credential. |
| `Credential_Update` | `EXEC` | `automationAccountName, credentialName, resourceGroupName, subscriptionId` | Update a credential. |
