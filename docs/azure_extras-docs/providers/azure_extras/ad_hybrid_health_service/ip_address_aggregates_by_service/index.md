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
| `attemptCountThresholdOnTrigger` | `integer` | The attempted count threshold on trigger. |
| `extranetLockoutErrorCount` | `integer` | The extranet lockout error count |
| `geographicLocation` | `string` | The geographic location. |
| `timeSpan` | `string` | The duration of the event |
| `uniqueUsernamesAttemptedCount` | `integer` | The unique usernames attempted |
| `badPasswordErrorCount` | `integer` | The bad password error count |
| `timestamp` | `string` | When the event occurred |
| `networkLocation` | `string` | The network location |
| `tenantId` | `string` | The tenant ID |
| `attemptThresholdTypeOnTrigger` | `string` | The attempted threshold type on trigger. |
| `lastAuditTimestamp` | `string` | The last audit timestamp |
| `ipAddress` | `string` | The IP address from where the attempted login originated from. |
| `isWhitelistedIpAddress` | `boolean` | A value indicating whether the IP address has been whitelisted. |
| `firstAuditTimestamp` | `string` | The first audit timestamp |
| `attemptCountThresholdIsExceeded` | `boolean` | A value indicating whether the attempt count threshold been exceeded |
| `serviceId` | `string` | The service ID |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_IPAddressAggregatesByService` | `SELECT` | `serviceName` |
