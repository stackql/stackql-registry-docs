---
title: ip_address_aggregates_by_service
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_address_aggregates_by_service
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
<tr><td><b>Name</b></td><td><code>ip_address_aggregates_by_service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.ip_address_aggregates_by_service</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique ID for the entree |
| `attemptCountThresholdIsExceeded` | `boolean` | A value indicating whether the attempt count threshold been exceeded |
| `attemptCountThresholdOnTrigger` | `integer` | The attempted count threshold on trigger. |
| `attemptThresholdTypeOnTrigger` | `string` | The attempted threshold type on trigger. |
| `badPasswordErrorCount` | `integer` | The bad password error count |
| `extranetLockoutErrorCount` | `integer` | The extranet lockout error count |
| `firstAuditTimestamp` | `string` | The first audit timestamp |
| `geographicLocation` | `string` | The geographic location. |
| `ipAddress` | `string` | The IP address from where the attempted login originated from. |
| `isWhitelistedIpAddress` | `boolean` | A value indicating whether the IP address has been listed as allowed. |
| `lastAuditTimestamp` | `string` | The last audit timestamp |
| `networkLocation` | `string` | The network location |
| `serviceId` | `string` | The service ID |
| `tenantId` | `string` | The tenant ID |
| `timeSpan` | `string` | The duration of the event |
| `timestamp` | `string` | When the event occurred |
| `uniqueUsernamesAttemptedCount` | `integer` | The unique usernames attempted |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `serviceName` |
| `_list` | `EXEC` | `serviceName` |
