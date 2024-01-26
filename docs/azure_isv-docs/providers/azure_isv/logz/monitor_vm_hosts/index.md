---
title: monitor_vm_hosts
hide_title: false
hide_table_of_contents: false
keywords:
  - monitor_vm_hosts
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
<tr><td><b>Name</b></td><td><code>monitor_vm_hosts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.logz.monitor_vm_hosts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | Link to the next set of results, if any. |
| `value` | `array` | Response of a list vm host update operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
