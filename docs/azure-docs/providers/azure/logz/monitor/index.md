---
title: monitor
hide_title: false
hide_table_of_contents: false
keywords:
  - monitor
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
<tr><td><b>Name</b></td><td><code>monitor</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logz.monitor</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Monitor_ListVMHosts` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitor_ListVmHostUpdate` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `Monitor_VMHostPayload` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
