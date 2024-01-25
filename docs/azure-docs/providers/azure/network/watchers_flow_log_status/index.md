---
title: watchers_flow_log_status
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers_flow_log_status
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
<tr><td><b>Name</b></td><td><code>watchers_flow_log_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.watchers_flow_log_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `flowAnalyticsConfiguration` | `object` | Parameters that define the configuration of traffic analytics. |
| `properties` | `object` | Parameters that define the configuration of flow log. |
| `targetResourceId` | `string` | The ID of the resource to configure for flow log and traffic analytics (optional) . |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `networkWatcherName, resourceGroupName, subscriptionId, data__targetResourceId` |
