---
title: service_members
hide_title: false
hide_table_of_contents: false
keywords:
  - service_members
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

Creates, updates, deletes, gets or lists a <code>service_members</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.service_members" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activeAlerts" /> | `integer` | The total number of alerts that are currently active for the server. |
| <CopyableCode code="additionalInformation" /> | `string` | The additional information, if any, for the server. |
| <CopyableCode code="createdDate" /> | `string` | The date time , in UTC, when the server was onboarded to Azure Active Directory Connect Health. |
| <CopyableCode code="dimensions" /> | `object` | The server specific configuration related dimensions. |
| <CopyableCode code="disabled" /> | `boolean` | Indicates if the server is disabled or not. |
| <CopyableCode code="disabledReason" /> | `integer` | The reason for disabling the server. |
| <CopyableCode code="installedQfes" /> | `object` | The list of installed QFEs for the server. |
| <CopyableCode code="lastDisabled" /> | `string` | The date and time , in UTC, when the server was last disabled. |
| <CopyableCode code="lastReboot" /> | `string` | The date and time, in UTC, when the server was last rebooted. |
| <CopyableCode code="lastServerReportedMonitoringLevelChange" /> | `string` | The date and time, in UTC, when the server's data monitoring configuration was last changed. |
| <CopyableCode code="lastUpdated" /> | `string` | The date and time, in UTC, when the server properties were last updated. |
| <CopyableCode code="machineId" /> | `string` | The id of the machine. |
| <CopyableCode code="machineName" /> | `string` | The name of the server. |
| <CopyableCode code="monitoringConfigurationsComputed" /> | `object` | The monitoring configuration of the server which determines what activities are monitored by Azure Active Directory Connect Health. |
| <CopyableCode code="monitoringConfigurationsCustomized" /> | `object` | The customized monitoring configuration of the server which determines what activities are monitored by Azure Active Directory Connect Health. |
| <CopyableCode code="osName" /> | `string` | The name of the operating system installed in the machine. |
| <CopyableCode code="osVersion" /> | `string` | The version of the operating system installed in the machine. |
| <CopyableCode code="properties" /> | `object` | Server specific properties. |
| <CopyableCode code="recommendedQfes" /> | `object` | The list of recommended hotfixes for the server. |
| <CopyableCode code="resolvedAlerts" /> | `integer` | The total count of alerts that are resolved for this server. |
| <CopyableCode code="role" /> | `string` | The service role that is being monitored in the server. |
| <CopyableCode code="serverReportedMonitoringLevel" /> | `string` | The monitoring level reported by the server. |
| <CopyableCode code="serviceId" /> | `string` | The service id to whom this server belongs. |
| <CopyableCode code="serviceMemberId" /> | `string` | The id of the server. |
| <CopyableCode code="status" /> | `string` | The health status of the server. |
| <CopyableCode code="tenantId" /> | `string` | The tenant id to whom this server belongs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="serviceMemberId, serviceName" /> | Gets the details of a server, for a given service, that are onboarded to Azure Active Directory Connect Health Service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> | Gets the details of the servers, for a given service, that are onboarded to Azure Active Directory Connect Health Service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="serviceMemberId, serviceName" /> | Deletes a server that has been onboarded to Azure Active Directory Connect Health Service. |
| <CopyableCode code="add" /> | `EXEC` | <CopyableCode code="serviceName" /> | Onboards  a server, for a given service, to Azure Active Directory Connect Health Service. |
| <CopyableCode code="delete_data" /> | `EXEC` | <CopyableCode code="serviceMemberId, serviceName" /> | Deletes the data uploaded by the server to Azure Active Directory Connect Health Service. |

## `SELECT` examples

Gets the details of the servers, for a given service, that are onboarded to Azure Active Directory Connect Health Service.


```sql
SELECT
activeAlerts,
additionalInformation,
createdDate,
dimensions,
disabled,
disabledReason,
installedQfes,
lastDisabled,
lastReboot,
lastServerReportedMonitoringLevelChange,
lastUpdated,
machineId,
machineName,
monitoringConfigurationsComputed,
monitoringConfigurationsCustomized,
osName,
osVersion,
properties,
recommendedQfes,
resolvedAlerts,
role,
serverReportedMonitoringLevel,
serviceId,
serviceMemberId,
status,
tenantId
FROM azure.ad_hybrid_health_service.service_members
WHERE serviceName = '{{ serviceName }}';
```
## `DELETE` example

Deletes the specified <code>service_members</code> resource.

```sql
/*+ delete */
DELETE FROM azure.ad_hybrid_health_service.service_members
WHERE serviceMemberId = '{{ serviceMemberId }}'
AND serviceName = '{{ serviceName }}';
```
