---
title: traffic_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - traffic_filters
  - elastic
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
<tr><td><b>Name</b></td><td><code>traffic_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.elastic.traffic_filters</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
| `delete` | `DELETE` | `monitorName, resourceGroupName, subscriptionId` |
| `associate` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `detach_and_delete` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
| `update` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` |
