---
title: webhook
hide_title: false
hide_table_of_contents: false
keywords:
  - webhook
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
<tr><td><b>Name</b></td><td><code>webhook</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.webhook</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId, webhookName` | Retrieve the webhook identified by webhook name. |
| `list_by_automation_account` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of webhooks. |
| `create_or_update` | `INSERT` | `automationAccountName, resourceGroupName, subscriptionId, webhookName, data__name, data__properties` | Create the webhook identified by webhook name. |
| `delete` | `DELETE` | `automationAccountName, resourceGroupName, subscriptionId, webhookName` | Delete the webhook by name. |
| `_list_by_automation_account` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of webhooks. |
| `generate_uri` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Generates a Uri for use in creating a webhook. |
| `update` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId, webhookName` | Update the webhook identified by webhook name. |
