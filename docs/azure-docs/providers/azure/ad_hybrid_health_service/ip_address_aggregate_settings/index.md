---
title: ip_address_aggregate_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_address_aggregate_settings
  - ad_hybrid_health_service
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
<tr><td><b>Name</b></td><td><code>ip_address_aggregate_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.ip_address_aggregate_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique ID for the entree |
| `badPasswordAndExtranetLockoutCombinedDailyThreshold` | `integer` | This threshold setting defines the per day trigger for a new event to be generated in the report. |
| `badPasswordAndExtranetLockoutCombinedHourlyThreshold` | `integer` | This threshold setting defines the per hour trigger for a new event to be generated in the report. |
| `emailNotificationEnabled` | `boolean` | A value indicating whether email notification has been enabled. |
| `extranetLockoutDailyThreshold` | `integer` | This threshold setting defines the per hour trigger for a new event to be generated in the report. |
| `extranetLockoutHourlyThreshold` | `integer` | This threshold setting defines the per hour trigger for a new event to be generated in the report. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `serviceName` | Gets the IP address aggregate settings. |
| `update` | `EXEC` | `serviceName` | Updates the IP address aggregate settings alert thresholds. |
