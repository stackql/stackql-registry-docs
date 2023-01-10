---
title: service_members
hide_title: false
hide_table_of_contents: false
keywords:
  - service_members
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
<tr><td><b>Name</b></td><td><code>service_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.ad_hybrid_health_service.service_members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `dimensions` | `object` | The server specific configuration related dimensions. |
| `role` | `string` | The service role that is being monitored in the server. |
| `lastServerReportedMonitoringLevelChange` | `string` | The date and time, in UTC, when the server's data monitoring configuration was last changed. |
| `installedQfes` | `object` | The list of installed QFEs for the server. |
| `serviceMemberId` | `string` | The id of the server. |
| `serviceId` | `string` | The service id to whom this server belongs. |
| `tenantId` | `string` | The tenant id to whom this server belongs. |
| `disabledReason` | `integer` | The reason for disabling the server. |
| `monitoringConfigurationsCustomized` | `object` | The customized monitoring configuration of the server which determines what activities are monitored by Azure Active Directory Connect Health. |
| `recommendedQfes` | `object` | The list of recommended hotfixes for the server. |
| `additionalInformation` | `string` | The additional information, if any, for the server. |
| `resolvedAlerts` | `integer` | The total count of alerts that are resolved for this server. |
| `osVersion` | `string` | The version of the operating system installed in the machine. |
| `lastDisabled` | `string` | The date and time , in UTC, when the server was last disabled. |
| `createdDate` | `string` | The date time , in UTC, when the server was onboarded to Azure Active Directory Connect Health. |
| `status` | `string` | The health status of the server. |
| `lastUpdated` | `string` | The date and time, in UTC, when the server properties were last updated. |
| `properties` | `object` | Server specific properties. |
| `activeAlerts` | `integer` | The total number of alerts that are currently active for the server. |
| `osName` | `string` | The name of the operating system installed in the machine. |
| `machineId` | `string` | The id of the machine. |
| `lastReboot` | `string` | The date and time, in UTC, when the server was last rebooted. |
| `serverReportedMonitoringLevel` | `string` | The monitoring level reported by the server. |
| `monitoringConfigurationsComputed` | `object` | The monitoring configuration of the server which determines what activities are monitored by Azure Active Directory Connect Health. |
| `disabled` | `boolean` | Indicates if the server is disabled or not.  |
| `machineName` | `string` | The name of the server. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `serviceMembers_get` | `SELECT` | `serviceMemberId, serviceName` | Gets the details of a server, for a given service, that are onboarded to Azure Active Directory Connect Health Service. |
| `serviceMembers_list` | `SELECT` | `serviceName` | Gets the details of the servers, for a given service, that are onboarded to Azure Active Directory Connect Health Service. |
| `serviceMembers_add` | `INSERT` | `serviceName` | Onboards  a server, for a given service, to Azure Active Directory Connect Health Service. |
| `serviceMembers_delete` | `DELETE` | `serviceMemberId, serviceName` | Deletes a server that has been onboarded to Azure Active Directory Connect Health Service. |
| `serviceMembers_deleteData` | `EXEC` | `serviceMemberId, serviceName` | Deletes the data uploaded by the server to Azure Active Directory Connect Health Service. |
| `serviceMembers_getConnectorMetadata` | `EXEC` | `metricName, serviceMemberId, serviceName` | Gets the list of connectors and run profile names. |
| `serviceMembers_getMetrics` | `EXEC` | `groupName, metricName, serviceMemberId, serviceName` | Gets the server related metrics for a given metric and group combination. |
| `serviceMembers_getServiceConfiguration` | `EXEC` | `serviceMemberId, serviceName` | Gets the service configuration. |
| `serviceMembers_listAlerts` | `EXEC` | `serviceMemberId, serviceName` | Gets the details of an alert for a given service and server combination. |
| `serviceMembers_listConnectors` | `EXEC` | `serviceMemberId, serviceName` | Gets the connector details for a service. |
| `serviceMembers_listCredentials` | `EXEC` | `serviceMemberId, serviceName` | Gets the credentials of the server which is needed by the agent to connect to Azure Active Directory Connect Health Service. |
| `serviceMembers_listDataFreshness` | `EXEC` | `serviceMemberId, serviceName` | Gets the last time when the server uploaded data to Azure Active Directory Connect Health Service. |
| `serviceMembers_listExportStatus` | `EXEC` | `serviceMemberId, serviceName` | Gets the export status. |
| `serviceMembers_listGlobalConfiguration` | `EXEC` | `serviceMemberId, serviceName` | Gets the global configuration. |
