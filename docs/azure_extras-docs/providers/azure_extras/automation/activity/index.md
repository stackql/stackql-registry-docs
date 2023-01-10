---
title: activity
hide_title: false
hide_table_of_contents: false
keywords:
  - activity
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
<tr><td><b>Name</b></td><td><code>activity</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.activity</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the id of the resource. |
| `name` | `string` | Gets the name of the activity. |
| `properties` | `object` | Properties of the activity. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Activity_Get` | `SELECT` | `activityName, automationAccountName, moduleName, resourceGroupName, subscriptionId` | Retrieve the activity in the module identified by module name and activity name. |
| `Activity_ListByModule` | `SELECT` | `automationAccountName, moduleName, resourceGroupName, subscriptionId` | Retrieve a list of activities in the module identified by module name. |
