---
title: adds_services_service_members
hide_title: false
hide_table_of_contents: false
keywords:
  - adds_services_service_members
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
<tr><td><b>Name</b></td><td><code>adds_services_service_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.ad_hybrid_health_service.adds_services_service_members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `monitoringConfigurationsCustomized` | `object` | The customized monitoring configuration of the server which determines what activities are monitored by Azure Active Directory Connect Health. |
| `status` | `string` | The health status of the server. |
| `createdDate` | `string` | The date time , in UTC, when the server was onboarded to Azure Active Directory Connect Health. |
| `properties` | `object` | Server specific properties. |
| `machineName` | `string` | The name of the server. |
| `machineId` | `string` | The id of the machine. |
| `tenantId` | `string` | The tenant id to whom this server belongs. |
| `osVersion` | `string` | The version of the operating system installed in the machine. |
| `osName` | `string` | The name of the operating system installed in the machine. |
| `serviceMemberId` | `string` | The id of the server. |
| `role` | `string` | The service role that is being monitored in the server. |
| `serviceId` | `string` | The service id to whom this server belongs. |
| `recommendedQfes` | `object` | The list of recommended hotfixes for the server. |
| `installedQfes` | `object` | The list of installed QFEs for the server. |
| `resolvedAlerts` | `integer` | The total count of alerts that are resolved for this server. |
| `additionalInformation` | `string` | The additional information, if any, for the server. |
| `dimensions` | `object` | The server specific configuration related dimensions. |
| `serverReportedMonitoringLevel` | `string` | The monitoring level reported by the server. |
| `disabledReason` | `integer` | The reason for disabling the server. |
| `activeAlerts` | `integer` | The total number of alerts that are currently active for the server. |
| `lastServerReportedMonitoringLevelChange` | `string` | The date and time, in UTC, when the server's data monitoring configuration was last changed. |
| `disabled` | `boolean` | Indicates if the server is disabled or not.  |
| `lastUpdated` | `string` | The date and time, in UTC, when the server properties were last updated. |
| `monitoringConfigurationsComputed` | `object` | The monitoring configuration of the server which determines what activities are monitored by Azure Active Directory Connect Health. |
| `lastDisabled` | `string` | The date and time , in UTC, when the server was last disabled. |
| `lastReboot` | `string` | The date and time, in UTC, when the server was last rebooted. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `addsServicesServiceMembers_list` | `SELECT` | `serviceName` | Gets the details of the servers, for a given Active Directory Domain Controller service, that are onboarded to Azure Active Directory Connect Health Service. |
| `addsServicesServiceMembers_add` | `INSERT` | `serviceName` | Onboards  a server, for a given Active Directory Domain Controller service, to Azure Active Directory Connect Health Service. |
