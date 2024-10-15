---
title: ip_address_aggregates_by_services
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_address_aggregates_by_services
  - ad_hybrid_health_service
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>ip_address_aggregates_by_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_address_aggregates_by_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.ip_address_aggregates_by_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique ID for the entree |
| <CopyableCode code="attemptCountThresholdIsExceeded" /> | `boolean` | A value indicating whether the attempt count threshold been exceeded |
| <CopyableCode code="attemptCountThresholdOnTrigger" /> | `integer` | The attempted count threshold on trigger. |
| <CopyableCode code="attemptThresholdTypeOnTrigger" /> | `string` | The attempted threshold type on trigger. |
| <CopyableCode code="badPasswordErrorCount" /> | `integer` | The bad password error count |
| <CopyableCode code="extranetLockoutErrorCount" /> | `integer` | The extranet lockout error count |
| <CopyableCode code="firstAuditTimestamp" /> | `string` | The first audit timestamp |
| <CopyableCode code="geographicLocation" /> | `string` | The geographic location. |
| <CopyableCode code="ipAddress" /> | `string` | The IP address from where the attempted login originated from. |
| <CopyableCode code="isWhitelistedIpAddress" /> | `boolean` | A value indicating whether the IP address has been listed as allowed. |
| <CopyableCode code="lastAuditTimestamp" /> | `string` | The last audit timestamp |
| <CopyableCode code="networkLocation" /> | `string` | The network location |
| <CopyableCode code="serviceId" /> | `string` | The service ID |
| <CopyableCode code="tenantId" /> | `string` | The tenant ID |
| <CopyableCode code="timeSpan" /> | `string` | The duration of the event |
| <CopyableCode code="timestamp" /> | `string` | When the event occurred |
| <CopyableCode code="uniqueUsernamesAttemptedCount" /> | `integer` | The unique usernames attempted |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> | Gets the IP address aggregates for a given service. |

## `SELECT` examples

Gets the IP address aggregates for a given service.


```sql
SELECT
id,
attemptCountThresholdIsExceeded,
attemptCountThresholdOnTrigger,
attemptThresholdTypeOnTrigger,
badPasswordErrorCount,
extranetLockoutErrorCount,
firstAuditTimestamp,
geographicLocation,
ipAddress,
isWhitelistedIpAddress,
lastAuditTimestamp,
networkLocation,
serviceId,
tenantId,
timeSpan,
timestamp,
uniqueUsernamesAttemptedCount
FROM azure.ad_hybrid_health_service.ip_address_aggregates_by_services
WHERE serviceName = '{{ serviceName }}';
```