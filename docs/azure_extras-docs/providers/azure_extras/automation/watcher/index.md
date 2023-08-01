---
title: watcher
hide_title: false
hide_table_of_contents: false
keywords:
  - watcher
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
<tr><td><b>Name</b></td><td><code>watcher</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.automation.watcher</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Definition of the watcher properties |
| `tags` | `object` | Resource tags. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `etag` | `string` | Gets or sets the etag of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Watcher_Get` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId, watcherName` | Retrieve the watcher identified by watcher name. |
| `Watcher_ListByAutomationAccount` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of watchers. |
| `Watcher_CreateOrUpdate` | `INSERT` | `automationAccountName, resourceGroupName, subscriptionId, watcherName` | Create the watcher identified by watcher name. |
| `Watcher_Delete` | `DELETE` | `automationAccountName, resourceGroupName, subscriptionId, watcherName` | Delete the watcher by name. |
| `Watcher_Start` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId, watcherName` | Resume the watcher identified by watcher name. |
| `Watcher_Stop` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId, watcherName` | Resume the watcher identified by watcher name. |
| `Watcher_Update` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId, watcherName` | Update the watcher identified by watcher name. |
