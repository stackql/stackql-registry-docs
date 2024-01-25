---
title: ports_liveness
hide_title: false
hide_table_of_contents: false
keywords:
  - ports_liveness
  - service_map
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
<tr><td><b>Name</b></td><td><code>ports_liveness</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_map.ports_liveness</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `endTime` | `string` | Liveness interval end time. |
| `live` | `boolean` | `true` if the resource is live during [startTime, endTime], `false` otherwise |
| `startTime` | `string` | Liveness interval start time. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `machineName, portName, resourceGroupName, subscriptionId, workspaceName` |
