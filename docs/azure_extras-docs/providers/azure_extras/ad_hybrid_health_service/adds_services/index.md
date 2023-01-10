---
title: adds_services
hide_title: false
hide_table_of_contents: false
keywords:
  - adds_services
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
<tr><td><b>Name</b></td><td><code>adds_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.ad_hybrid_health_service.adds_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The id of the service. |
| `lastDisabled` | `string` | The date and time, in UTC, when the service was last disabled. |
| `type` | `string` | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. |
| `createdDate` | `string` | The date and time, in UTC, when the service was onboarded to Azure Active Directory Connect Health. |
| `notificationEmailEnabled` | `boolean` | Indicates if email notification is enabled or not. |
| `notificationEmails` | `array` | The list of emails to whom service notifications will be sent. |
| `monitoringConfigurationsComputed` | `object` | The monitoring configuration of the service which determines what activities are monitored by Azure Active Directory Connect Health. |
| `notificationEmailsEnabledForGlobalAdmins` | `boolean` | Indicates if email notification is enabled for global administrators of the tenant. |
| `simpleProperties` | `object` | List of service specific configuration properties. |
| `lastUpdated` | `string` | The date or time , in UTC, when the service properties were last updated. |
| `disabled` | `boolean` | Indicates if the service is disabled or not. |
| `resolvedAlerts` | `integer` | The total count of alerts that has been resolved for the service. |
| `customNotificationEmails` | `array` | The list of additional emails that are configured to receive notifications about the service. |
| `originalDisabledState` | `boolean` | Gets the original disable state. |
| `serviceName` | `string` | The name of the service. |
| `serviceId` | `string` | The id of the service. |
| `health` | `string` | The health of the service. |
| `monitoringConfigurationsCustomized` | `object` | The customized monitoring configuration of the service which determines what activities are monitored by Azure Active Directory Connect Health. |
| `signature` | `string` | The signature of the service. |
| `activeAlerts` | `integer` | The count of alerts that are currently active for the service. |
| `displayName` | `string` | The display name of the service. |
| `tenantId` | `string` | The id of the tenant to which the service is registered to. |
| `additionalInformation` | `string` | The additional information related to the service. |
| `notificationEmailEnabledForGlobalAdmins` | `boolean` | Indicates if email notification is enabled for global administrators of the tenant. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `addsServices_get` | `SELECT` | `serviceName` | Gets the details of an Active Directory Domain Service for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health. |
| `addsServices_list` | `SELECT` |  | Gets the details of Active Directory Domain Service, for a tenant, that are onboarded to Azure Active Directory Connect Health. |
| `addsServices_add` | `INSERT` |  | Onboards a service for a given tenant in Azure Active Directory Connect Health. |
| `addsServices_delete` | `DELETE` | `serviceName` | Deletes an Active Directory Domain Service which is onboarded to Azure Active Directory Connect Health. |
| `addsServices_getForestSummary` | `EXEC` | `serviceName` | Gets the forest summary for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health. |
| `addsServices_getMetricMetadata` | `EXEC` | `metricName, serviceName` | Gets the service related metric information. |
| `addsServices_getMetricMetadataForGroup` | `EXEC` | `groupName, metricName, serviceName` | Gets the service related metrics for a given metric and group combination. |
| `addsServices_listMetricMetadata` | `EXEC` | `serviceName` | Gets the service related metrics information. |
| `addsServices_listMetricsAverage` | `EXEC` | `groupName, metricName, serviceName` | Gets the average of the metric values for a given metric and group combination. |
| `addsServices_listMetricsSum` | `EXEC` | `groupName, metricName, serviceName` | Gets the sum of the metric values for a given metric and group combination. |
| `addsServices_listPremiumServices` | `EXEC` |  | Gets the details of Active Directory Domain Services for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health. |
| `addsServices_listReplicationDetails` | `EXEC` | `serviceName` | Gets complete domain controller list along with replication details for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health. |
| `addsServices_listReplicationSummary` | `EXEC` | `isGroupbySite, nextPartitionKey, nextRowKey, query, serviceName` | Gets complete domain controller list along with replication details for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health. |
| `addsServices_listServerAlerts` | `EXEC` | `serviceMemberId, serviceName` | Gets the details of an alert for a given Active Directory Domain Controller service and server combination. |
| `addsServices_update` | `EXEC` | `serviceName` | Updates an Active Directory Domain Service properties of an onboarded service. |
