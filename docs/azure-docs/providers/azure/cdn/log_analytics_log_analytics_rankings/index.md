---
title: log_analytics_log_analytics_rankings
hide_title: false
hide_table_of_contents: false
keywords:
  - log_analytics_log_analytics_rankings
  - cdn
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
<tr><td><b>Name</b></td><td><code>log_analytics_log_analytics_rankings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.log_analytics_log_analytics_rankings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `dateTimeBegin` | `string` |
| `dateTimeEnd` | `string` |
| `tables` | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `dateTimeBegin, dateTimeEnd, maxRanking, metrics, profileName, rankings, resourceGroupName, subscriptionId` |
