---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.ad_hybrid_health_service.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The id of the service. |
| `activeAlerts` | `integer` | The count of alerts that are currently active for the service. |
| `customNotificationEmails` | `array` | The list of additional emails that are configured to receive notifications about the service. |
| `serviceId` | `string` | The id of the service. |
| `notificationEmailsEnabledForGlobalAdmins` | `boolean` | Indicates if email notification is enabled for global administrators of the tenant. |
| `signature` | `string` | The signature of the service. |
| `notificationEmailEnabled` | `boolean` | Indicates if email notification is enabled or not. |
| `lastUpdated` | `string` | The date or time , in UTC, when the service properties were last updated. |
| `resolvedAlerts` | `integer` | The total count of alerts that has been resolved for the service. |
| `health` | `string` | The health of the service. |
| `tenantId` | `string` | The id of the tenant to which the service is registered to. |
| `createdDate` | `string` | The date and time, in UTC, when the service was onboarded to Azure Active Directory Connect Health. |
| `serviceName` | `string` | The name of the service. |
| `originalDisabledState` | `boolean` | Gets the original disable state. |
| `notificationEmails` | `array` | The list of emails to whom service notifications will be sent. |
| `type` | `string` | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. |
| `displayName` | `string` | The display name of the service. |
| `disabled` | `boolean` | Indicates if the service is disabled or not. |
| `additionalInformation` | `string` | The additional information related to the service. |
| `notificationEmailEnabledForGlobalAdmins` | `boolean` | Indicates if email notification is enabled for global administrators of the tenant. |
| `simpleProperties` | `object` | List of service specific configuration properties. |
| `monitoringConfigurationsCustomized` | `object` | The customized monitoring configuration of the service which determines what activities are monitored by Azure Active Directory Connect Health. |
| `monitoringConfigurationsComputed` | `object` | The monitoring configuration of the service which determines what activities are monitored by Azure Active Directory Connect Health. |
| `lastDisabled` | `string` | The date and time, in UTC, when the service was last disabled. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `serviceName` | Gets the details of a service for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health. |
| `list` | `SELECT` |  | Gets the details of services, for a tenant, that are onboarded to Azure Active Directory Connect Health. |
| `add` | `INSERT` |  | Onboards a service for a given tenant in Azure Active Directory Connect Health. |
| `delete` | `DELETE` | `serviceName` | Deletes a service which is onboarded to Azure Active Directory Connect Health. |
| `addAlertFeedback` | `EXEC` | `serviceName` | Adds an alert feedback submitted by customer. |
| `getFeatureAvailibility` | `EXEC` | `featureName, serviceName` | Checks if the service has all the pre-requisites met to use a feature. |
| `getMetricMetadata` | `EXEC` | `metricName, serviceName` | Gets the service related metrics information. |
| `getMetricMetadataForGroup` | `EXEC` | `groupName, metricName, serviceName` | Gets the service related metrics for a given metric and group combination. |
| `getTenantWhitelisting` | `EXEC` | `featureName, serviceName` | Checks if the tenant, to which a service is registered, is whitelisted to use a feature. |
| `listAlertFeedback` | `EXEC` | `serviceName, shortName` | Gets a list of all alert feedback for a given tenant and alert type. |
| `listAlerts` | `EXEC` | `serviceName` | Gets the alerts for a given service. |
| `listAllRiskyIpDownloadReport` | `EXEC` | `serviceName` | Gets all Risky IP report URIs for the last 7 days. |
| `listCurrentRiskyIpDownloadReport` | `EXEC` | `serviceName` | Initiate the generation of a new Risky IP report. Returns the URI for the new one. |
| `listExportErrors` | `EXEC` | `serviceName` | Gets the count of latest AAD export errors. |
| `listExportErrorsV2` | `EXEC` | `errorBucket, serviceName` |  Gets the categorized export errors. |
| `listExportStatus` | `EXEC` | `serviceName` | Gets the export status. |
| `listMetricMetadata` | `EXEC` | `serviceName` | Gets the service related metrics information. |
| `listMetricsAverage` | `EXEC` | `groupName, metricName, serviceName` | Gets the average of the metric values for a given metric and group combination. |
| `listMetricsSum` | `EXEC` | `groupName, metricName, serviceName` | Gets the sum of the metric values for a given metric and group combination. |
| `listMonitoringConfigurations` | `EXEC` | `serviceName` | Gets the service level monitoring configurations. |
| `listPremium` | `EXEC` |  | Gets the details of services for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health. |
| `listUserBadPasswordReport` | `EXEC` | `serviceName` | Gets the bad password login attempt report for an user |
| `update` | `EXEC` | `serviceName` | Updates the service properties of an onboarded service. |
| `updateMonitoringConfiguration` | `EXEC` | `serviceName` | Updates the service level monitoring configuration. |
