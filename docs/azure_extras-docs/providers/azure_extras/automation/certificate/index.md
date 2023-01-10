---
title: certificate
hide_title: false
hide_table_of_contents: false
keywords:
  - certificate
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
<tr><td><b>Name</b></td><td><code>certificate</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.certificate</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Certificate_Get` | `SELECT` | `automationAccountName, certificateName, resourceGroupName, subscriptionId` | Retrieve the certificate identified by certificate name. |
| `Certificate_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of certificates. |
| `Certificate_CreateOrUpdate` | `INSERT` | `automationAccountName, certificateName, resourceGroupName, subscriptionId, data__name, data__properties` | Create a certificate. |
| `Certificate_Delete` | `DELETE` | `automationAccountName, certificateName, resourceGroupName, subscriptionId` | Delete the certificate. |
| `Certificate_Update` | `EXEC` | `automationAccountName, certificateName, resourceGroupName, subscriptionId` | Update a certificate. |
