---
title: global_reach_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - global_reach_connections
  - vmware
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>global_reach_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.vmware.global_reach_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `properties` | `object` | The properties of a global reach connection |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `globalReachConnectionName, privateCloudName, resourceGroupName, subscriptionId` |
| `list` | `SELECT` | `privateCloudName, resourceGroupName, subscriptionId` |
| `create_or_update` | `INSERT` | `globalReachConnectionName, privateCloudName, resourceGroupName, subscriptionId` |
| `delete` | `DELETE` | `globalReachConnectionName, privateCloudName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `privateCloudName, resourceGroupName, subscriptionId` |
