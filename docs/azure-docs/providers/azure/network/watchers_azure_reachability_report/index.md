---
title: watchers_azure_reachability_report
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers_azure_reachability_report
  - network
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
<tr><td><b>Name</b></td><td><code>watchers_azure_reachability_report</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.watchers_azure_reachability_report</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `aggregationLevel` | `string` | The aggregation level of Azure reachability report. Can be Country, State or City. |
| `providerLocation` | `object` | Parameters that define a geographic location. |
| `reachabilityReport` | `array` | List of Azure reachability report items. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `networkWatcherName, resourceGroupName, subscriptionId, data__endTime, data__providerLocation, data__startTime` |
