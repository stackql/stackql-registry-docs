---
title: sub_account
hide_title: false
hide_table_of_contents: false
keywords:
  - sub_account
  - logz
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
<tr><td><b>Name</b></td><td><code>sub_account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.logz.sub_account</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ARM id of the monitor resource. |
| `name` | `string` | Name of the monitor resource. |
| `identity` | `object` |  |
| `location` | `string` |  |
| `properties` | `object` | Properties specific to the monitor resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` |  |
| `type` | `string` | The type of the monitor resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `monitorName, resourceGroupName, subAccountName, subscriptionId` |
| `list` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
| `create` | `INSERT` | `monitorName, resourceGroupName, subAccountName, subscriptionId, data__location` |
| `delete` | `DELETE` | `monitorName, resourceGroupName, subAccountName, subscriptionId` |
| `_list` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `update` | `EXEC` | `monitorName, resourceGroupName, subAccountName, subscriptionId` |
| `vm_host_payload` | `EXEC` | `monitorName, resourceGroupName, subAccountName, subscriptionId` |
