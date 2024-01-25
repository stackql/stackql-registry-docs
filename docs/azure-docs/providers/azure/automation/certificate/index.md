---
title: certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate
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
<tr><td><b>Name</b></td><td><code>certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.certificate</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationAccountName, certificateName, resourceGroupName, subscriptionId` | Retrieve the certificate identified by certificate name. |
| `list_by_automation_account` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of certificates. |
| `create_or_update` | `INSERT` | `automationAccountName, certificateName, resourceGroupName, subscriptionId, data__name, data__properties` | Create a certificate. |
| `delete` | `DELETE` | `automationAccountName, certificateName, resourceGroupName, subscriptionId` | Delete the certificate. |
| `_list_by_automation_account` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of certificates. |
| `update` | `EXEC` | `automationAccountName, certificateName, resourceGroupName, subscriptionId` | Update a certificate. |
