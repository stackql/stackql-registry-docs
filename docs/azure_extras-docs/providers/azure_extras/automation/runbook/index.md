---
title: runbook
hide_title: false
hide_table_of_contents: false
keywords:
  - runbook
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
<tr><td><b>Name</b></td><td><code>runbook</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.runbook</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `etag` | `string` | Gets or sets the etag of the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Definition of the runbook property type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Runbook_Get` | `SELECT` | `automationAccountName, resourceGroupName, runbookName, subscriptionId` | Retrieve the runbook identified by runbook name. |
| `Runbook_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of runbooks. |
| `Runbook_CreateOrUpdate` | `INSERT` | `automationAccountName, resourceGroupName, runbookName, subscriptionId, data__properties` | Create the runbook identified by runbook name. |
| `Runbook_Delete` | `DELETE` | `automationAccountName, resourceGroupName, runbookName, subscriptionId` | Delete the runbook by name. |
| `Runbook_GetContent` | `EXEC` | `automationAccountName, resourceGroupName, runbookName, subscriptionId` | Retrieve the content of runbook identified by runbook name. |
| `Runbook_Publish` | `EXEC` | `automationAccountName, resourceGroupName, runbookName, subscriptionId` | Publish runbook draft. |
| `Runbook_Update` | `EXEC` | `automationAccountName, resourceGroupName, runbookName, subscriptionId` | Update the runbook identified by runbook name. |
