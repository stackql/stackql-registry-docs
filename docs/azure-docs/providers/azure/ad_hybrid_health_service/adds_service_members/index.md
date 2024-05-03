---
title: adds_service_members
hide_title: false
hide_table_of_contents: false
keywords:
  - adds_service_members
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>adds_service_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.adds_service_members" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activeAlerts" /> | `integer` | The total number of alerts that are currently active for the server. |
| <CopyableCode code="additionalInformation" /> | `string` | The additional information, if any, for the server. |
| <CopyableCode code="createdDate" /> | `string` | The date time , in UTC, when the server was onboarded to Azure Active Directory Connect Health. |
| <CopyableCode code="dimensions" /> | `object` | The server specific configuration related dimensions. |
| <CopyableCode code="disabled" /> | `boolean` | Indicates if the server is disabled or not.  |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="serviceMemberId, serviceName" /> | Gets the details of a server, for a given Active Directory Domain Controller service, that are onboarded to Azure Active Directory Connect Health Service. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="serviceName" /> | Gets the details of the Active Directory Domain servers, for a given Active Directory Domain Service, that are onboarded to Azure Active Directory Connect Health. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="serviceMemberId, serviceName" /> | Deletes a Active Directory Domain Controller server that has been onboarded to Azure Active Directory Connect Health Service. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="serviceName" /> | Gets the details of the Active Directory Domain servers, for a given Active Directory Domain Service, that are onboarded to Azure Active Directory Connect Health. |
