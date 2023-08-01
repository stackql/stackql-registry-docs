---
title: ad_domain_service_members
hide_title: false
hide_table_of_contents: false
keywords:
  - ad_domain_service_members
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
<tr><td><b>Name</b></td><td><code>ad_domain_service_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.ad_hybrid_health_service.ad_domain_service_members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `dcTypes` | `array` | The list of domain controller types. |
| `serviceMemberId` | `string` | The id of the server. |
| `createdDate` | `string` | The date time , in UTC, when the server was onboarded to Azure Active Directory Connect Health. |
| `disabled` | `boolean` | Indicates if the server is disabled or not.  |
| `recommendedQfes` | `array` | The list of recommended hotfixes for the server. |
| `tenantId` | `string` | The tenant id to whom this server belongs. |
| `dimensions` | `array` | The server specific configuration related dimensions. |
| `status` | `string` | The health status of the server. |
| `serviceId` | `string` | The service id to whom this server belongs. |
| `gcReachable` | `boolean` | Indicates if the global catalog for this domain is reachable or not. |
| `osVersion` | `string` | The version of the operating system installed in the machine. |
| `properties` | `array` | Server specific properties. |
| `resolvedAlerts` | `integer` | The total count of alerts that are resolved for this server. |
| `machineId` | `string` | The id of the machine. |
| `serverReportedMonitoringLevel` | `string` | The monitoring level reported by the server. |
| `osName` | `string` | The name of the operating system installed in the machine. |
| `sysvolState` | `boolean` | Indicates if the SYSVOL state is healthy or not. |
| `monitoringConfigurationsCustomized` | `array` | The customized monitoring configuration of the server which determines what activities are monitored by Azure Active Directory Connect Health. |
| `domainName` | `string` | The domain name. |
| `lastServerReportedMonitoringLevelChange` | `string` | The date and time, in UTC, when the server's data monitoring configuration was last changed. |
| `additionalInformation` | `string` | The additional information, if any, for the server. |
| `activeAlerts` | `integer` | The total number of alerts that are currently active for the server. |
| `installedQfes` | `array` | The list of installed QFEs for the server. |
| `monitoringConfigurationsComputed` | `array` | The monitoring configuration of the server which determines what activities are monitored by Azure Active Directory Connect Health. |
| `lastDisabled` | `string` | The date and time , in UTC, when the server was last disabled. |
| `machineName` | `string` | The name of the server. |
| `siteName` | `string` | The site name. |
| `disabledReason` | `integer` | The reason for disabling the server. |
| `lastUpdated` | `string` | The date and time, in UTC, when the server properties were last updated. |
| `addsRoles` | `array` | The list of ADDS roles. |
| `pdcReachable` | `boolean` | Indicates if the primary domain controller is reachable or not. |
| `isAdvertising` | `boolean` | Indicates if the Dc is advertising or not. |
| `role` | `string` | The service role that is being monitored in the server. |
| `lastReboot` | `string` | The date and time, in UTC, when the server was last rebooted. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `adDomainServiceMembers_list` | `SELECT` | `isGroupbySite, nextPartitionKey, nextRowKey, serviceName` |
