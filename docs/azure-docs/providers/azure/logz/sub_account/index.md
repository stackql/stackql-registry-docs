---
title: sub_account
hide_title: false
hide_table_of_contents: false
keywords:
  - sub_account
  - logz
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
<tr><td><b>Name</b></td><td><code>sub_account</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logz.sub_account</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ARM id of the monitor resource. |
| `name` | `string` | Name of the monitor resource. |
| `properties` | `object` | Properties specific to the monitor resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` |  |
| `type` | `string` | The type of the monitor resource. |
| `identity` | `object` |  |
| `location` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SubAccount_Get` | `SELECT` | `monitorName, resourceGroupName, subAccountName, subscriptionId` |
| `SubAccount_List` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
| `SubAccount_Create` | `INSERT` | `monitorName, resourceGroupName, subAccountName, subscriptionId, data__location` |
| `SubAccount_Delete` | `DELETE` | `monitorName, resourceGroupName, subAccountName, subscriptionId` |
| `SubAccount_ListMonitoredResources` | `EXEC` | `monitorName, resourceGroupName, subAccountName, subscriptionId` |
| `SubAccount_ListVMHosts` | `EXEC` | `monitorName, resourceGroupName, subAccountName, subscriptionId` |
| `SubAccount_ListVmHostUpdate` | `EXEC` | `monitorName, resourceGroupName, subAccountName, subscriptionId` |
| `SubAccount_Update` | `EXEC` | `monitorName, resourceGroupName, subAccountName, subscriptionId` |
| `SubAccount_VMHostPayload` | `EXEC` | `monitorName, resourceGroupName, subAccountName, subscriptionId` |
