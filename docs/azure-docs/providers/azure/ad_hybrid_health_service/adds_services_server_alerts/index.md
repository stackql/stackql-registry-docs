---
title: adds_services_server_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - adds_services_server_alerts
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

Creates, updates, deletes, gets or lists a <code>adds_services_server_alerts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>adds_services_server_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.adds_services_server_alerts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | The alert description. |
| <CopyableCode code="activeAlertProperties" /> | `array` | The active alert properties. |
| <CopyableCode code="additionalInformation" /> | `array` | Additional information related to the alert. |
| <CopyableCode code="alertId" /> | `string` | The alert Id. |
| <CopyableCode code="createdDate" /> | `string` | The date and time,in UTC,when the alert was created. |
| <CopyableCode code="displayName" /> | `string` | The display name for the alert. |
| <CopyableCode code="lastUpdated" /> | `string` | The date and time, in UTC, when the alert was last updated. |
| <CopyableCode code="level" /> | `string` | The alert level which indicates the severity of the alert. |
| <CopyableCode code="monitorRoleType" /> | `string` | The monitoring role type for which the alert was raised. |
| <CopyableCode code="relatedLinks" /> | `array` | The help links to get more information related to the alert. |
| <CopyableCode code="remediation" /> | `string` | The alert remediation. |
| <CopyableCode code="resolvedAlertProperties" /> | `array` | The resolved alert properties. |
| <CopyableCode code="resolvedDate" /> | `string` | The date and time, in UTC, when the alert was resolved. |
| <CopyableCode code="scope" /> | `string` | The scope of the alert. Indicates if it is a service or a server related alert. |
| <CopyableCode code="serviceId" /> | `string` | The service Id. |
| <CopyableCode code="serviceMemberId" /> | `string` | The server Id. |
| <CopyableCode code="shortName" /> | `string` | The alert short name. |
| <CopyableCode code="state" /> | `string` | The alert state which can be either active or resolved with multiple resolution types. |
| <CopyableCode code="tenantId" /> | `string` | The tenant Id. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceMemberId, serviceName" /> | Gets the details of an alert for a given Active Directory Domain Controller service and server combination. |

## `SELECT` examples

Gets the details of an alert for a given Active Directory Domain Controller service and server combination.


```sql
SELECT
description,
activeAlertProperties,
additionalInformation,
alertId,
createdDate,
displayName,
lastUpdated,
level,
monitorRoleType,
relatedLinks,
remediation,
resolvedAlertProperties,
resolvedDate,
scope,
serviceId,
serviceMemberId,
shortName,
state,
tenantId
FROM azure.ad_hybrid_health_service.adds_services_server_alerts
WHERE serviceMemberId = '{{ serviceMemberId }}'
AND serviceName = '{{ serviceName }}';
```