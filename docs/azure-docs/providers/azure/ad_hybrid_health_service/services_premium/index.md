---
title: services_premium
hide_title: false
hide_table_of_contents: false
keywords:
  - services_premium
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services_premium</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.services_premium</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The id of the service. |
| `activeAlerts` | `integer` | The count of alerts that are currently active for the service. |
| `additionalInformation` | `string` | The additional information related to the service. |
| `createdDate` | `string` | The date and time, in UTC, when the service was onboarded to Azure Active Directory Connect Health. |
| `customNotificationEmails` | `array` | The list of additional emails that are configured to receive notifications about the service. |
| `disabled` | `boolean` | Indicates if the service is disabled or not. |
| `displayName` | `string` | The display name of the service. |
| `health` | `string` | The health of the service. |
| `lastDisabled` | `string` | The date and time, in UTC, when the service was last disabled. |
| `lastUpdated` | `string` | The date or time , in UTC, when the service properties were last updated. |
| `monitoringConfigurationsComputed` | `object` | The monitoring configuration of the service which determines what activities are monitored by Azure Active Directory Connect Health. |
| `monitoringConfigurationsCustomized` | `object` | The customized monitoring configuration of the service which determines what activities are monitored by Azure Active Directory Connect Health. |
| `notificationEmailEnabled` | `boolean` | Indicates if email notification is enabled or not. |
| `notificationEmailEnabledForGlobalAdmins` | `boolean` | Indicates if email notification is enabled for global administrators of the tenant. |
| `notificationEmails` | `array` | The list of emails to whom service notifications will be sent. |
| `notificationEmailsEnabledForGlobalAdmins` | `boolean` | Indicates if email notification is enabled for global administrators of the tenant. |
| `originalDisabledState` | `boolean` | Gets the original disable state. |
| `resolvedAlerts` | `integer` | The total count of alerts that has been resolved for the service. |
| `serviceId` | `string` | The id of the service. |
| `serviceName` | `string` | The name of the service. |
| `signature` | `string` | The signature of the service. |
| `simpleProperties` | `object` | List of service specific configuration properties. |
| `tenantId` | `string` | The id of the tenant to which the service is registered to. |
| `type` | `string` | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
| `_list` | `EXEC` |  |
