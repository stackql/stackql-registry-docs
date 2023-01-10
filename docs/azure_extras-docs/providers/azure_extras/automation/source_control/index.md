---
title: source_control
hide_title: false
hide_table_of_contents: false
keywords:
  - source_control
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
<tr><td><b>Name</b></td><td><code>source_control</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.source_control</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SourceControl_Get` | `SELECT` | `automationAccountName, resourceGroupName, sourceControlName, subscriptionId` | Retrieve the source control identified by source control name. |
| `SourceControl_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of source controls. |
| `SourceControl_CreateOrUpdate` | `INSERT` | `automationAccountName, resourceGroupName, sourceControlName, subscriptionId, data__properties` | Create a source control. |
| `SourceControl_Delete` | `DELETE` | `automationAccountName, resourceGroupName, sourceControlName, subscriptionId` | Delete the source control. |
| `SourceControl_Update` | `EXEC` | `automationAccountName, resourceGroupName, sourceControlName, subscriptionId` | Update a source control. |
