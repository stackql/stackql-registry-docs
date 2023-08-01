---
title: ip_address_aggregates_by_service
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_address_aggregates_by_service
  - ad_hybrid_health_service
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.ad_hybrid_health_service.ip_address_aggregates_by_service</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique ID for the entree |
| `tenantId` | `string` | The tenant ID |
| `extranetLockoutErrorCount` | `integer` | The extranet lockout error count |
| `networkLocation` | `string` | The network location |
| `timeSpan` | `string` | The duration of the event |
| `attemptThresholdTypeOnTrigger` | `string` | The attempted threshold type on trigger. |
| `attemptCountThresholdIsExceeded` | `boolean` | A value indicating whether the attempt count threshold been exceeded |
| `geographicLocation` | `string` | The geographic location. |
| `firstAuditTimestamp` | `string` | The first audit timestamp |
| `isWhitelistedIpAddress` | `boolean` | A value indicating whether the IP address has been whitelisted. |
| `attemptCountThresholdOnTrigger` | `integer` | The attempted count threshold on trigger. |
| `badPasswordErrorCount` | `integer` | The bad password error count |
| `serviceId` | `string` | The service ID |
| `timestamp` | `string` | When the event occurred |
| `ipAddress` | `string` | The IP address from where the attempted login originated from. |
| `uniqueUsernamesAttemptedCount` | `integer` | The unique usernames attempted |
| `lastAuditTimestamp` | `string` | The last audit timestamp |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_IPAddressAggregatesByService` | `SELECT` | `serviceName` |
