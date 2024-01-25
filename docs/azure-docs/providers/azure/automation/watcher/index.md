---
title: watcher
hide_title: false
hide_table_of_contents: false
keywords:
  - watcher
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
<tr><td><b>Name</b></td><td><code>watcher</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.automation.watcher</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `etag` | `string` | Gets or sets the etag of the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Definition of the watcher properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId, watcherName` | Retrieve the watcher identified by watcher name. |
| `list_by_automation_account` | `SELECT` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of watchers. |
| `create_or_update` | `INSERT` | `automationAccountName, resourceGroupName, subscriptionId, watcherName` | Create the watcher identified by watcher name. |
| `delete` | `DELETE` | `automationAccountName, resourceGroupName, subscriptionId, watcherName` | Delete the watcher by name. |
| `_list_by_automation_account` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId` | Retrieve a list of watchers. |
| `start` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId, watcherName` | Resume the watcher identified by watcher name. |
| `stop` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId, watcherName` | Resume the watcher identified by watcher name. |
| `update` | `EXEC` | `automationAccountName, resourceGroupName, subscriptionId, watcherName` | Update the watcher identified by watcher name. |
