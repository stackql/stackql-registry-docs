---
title: log_analytics
hide_title: false
hide_table_of_contents: false
keywords:
  - log_analytics
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
<tr><td><b>Name</b></td><td><code>log_analytics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.log_analytics</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LogAnalytics_GetLogAnalyticsLocations` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Get all available location names for AFD log analytics report. |
| `LogAnalytics_GetLogAnalyticsMetrics` | `EXEC` | `customDomains, dateTimeBegin, dateTimeEnd, granularity, metrics, profileName, protocols, resourceGroupName, subscriptionId` | Get log report for AFD profile |
| `LogAnalytics_GetLogAnalyticsRankings` | `EXEC` | `dateTimeBegin, dateTimeEnd, maxRanking, metrics, profileName, rankings, resourceGroupName, subscriptionId` | Get log analytics ranking report for AFD profile |
| `LogAnalytics_GetLogAnalyticsResources` | `EXEC` | `profileName, resourceGroupName, subscriptionId` | Get all endpoints and custom domains available for AFD log report |
| `LogAnalytics_GetWafLogAnalyticsMetrics` | `EXEC` | `dateTimeBegin, dateTimeEnd, granularity, metrics, profileName, resourceGroupName, subscriptionId` | Get Waf related log analytics report for AFD profile. |
| `LogAnalytics_GetWafLogAnalyticsRankings` | `EXEC` | `dateTimeBegin, dateTimeEnd, maxRanking, metrics, profileName, rankings, resourceGroupName, subscriptionId` | Get WAF log analytics charts for AFD profile |
