---
title: component_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - component_containers
  - machine_learning_services
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
<tr><td><b>Name</b></td><td><code>component_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.machine_learning_services.component_containers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | Component container definition.<br />&lt;see href="https://docs.microsoft.com/en-us/azure/machine-learning/reference-yaml-component-command" /&gt; |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `ComponentContainers_Get` | `SELECT` | `name, resourceGroupName, subscriptionId, workspaceName` |
| `ComponentContainers_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
| `ComponentContainers_CreateOrUpdate` | `INSERT` | `name, resourceGroupName, subscriptionId, workspaceName, data__properties` |
| `ComponentContainers_Delete` | `DELETE` | `name, resourceGroupName, subscriptionId, workspaceName` |
