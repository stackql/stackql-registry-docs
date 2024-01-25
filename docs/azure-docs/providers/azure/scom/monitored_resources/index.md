---
title: monitored_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - monitored_resources
  - scom
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
<tr><td><b>Name</b></td><td><code>monitored_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.scom.monitored_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | The properties of a monitored resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `instanceName, monitoredResourceName, resourceGroupName, subscriptionId` | Retrieve the details of the monitored resource. |
| `list_by_managed_instance` | `SELECT` | `instanceName, resourceGroupName, subscriptionId` | A comprehensive list of all monitored resources within a SCOM managed instance. |
| `create_or_update` | `INSERT` | `instanceName, monitoredResourceName, resourceGroupName, subscriptionId` | Create or update a monitored resource. |
| `delete` | `DELETE` | `instanceName, monitoredResourceName, resourceGroupName, subscriptionId` | Delete a monitored resource. |
| `_list_by_managed_instance` | `EXEC` | `instanceName, resourceGroupName, subscriptionId` | A comprehensive list of all monitored resources within a SCOM managed instance. |
