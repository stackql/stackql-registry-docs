---
title: vmware_collectors
hide_title: false
hide_table_of_contents: false
keywords:
  - vmware_collectors
  - migrate
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
<tr><td><b>Name</b></td><td><code>vmware_collectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.migrate.vmware_collectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `properties` | `object` |
| `type` | `string` |
| `eTag` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VMwareCollectors_Get` | `SELECT` | `api-version, projectName, resourceGroupName, subscriptionId, vmWareCollectorName` | Get a VMware collector. |
| `VMwareCollectors_ListByProject` | `SELECT` | `api-version, projectName, resourceGroupName, subscriptionId` | Get a list of VMware collector. |
| `VMwareCollectors_Create` | `INSERT` | `api-version, projectName, resourceGroupName, subscriptionId, vmWareCollectorName` | Create or Update VMware collector |
| `VMwareCollectors_Delete` | `DELETE` | `api-version, projectName, resourceGroupName, subscriptionId, vmWareCollectorName` | Delete a VMware collector from the project. |
