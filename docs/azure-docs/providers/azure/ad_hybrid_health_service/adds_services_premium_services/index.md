---
title: adds_services_premium_services
hide_title: false
hide_table_of_contents: false
keywords:
  - adds_services_premium_services
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
<tr><td><b>Name</b></td><td><code>adds_services_premium_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.adds_services_premium_services" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The id of the service. |
| <CopyableCode code="activeAlerts" /> | `integer` | The count of alerts that are currently active for the service. |
| <CopyableCode code="additionalInformation" /> | `string` | The additional information related to the service. |
| <CopyableCode code="createdDate" /> | `string` | The date and time, in UTC, when the service was onboarded to Azure Active Directory Connect Health. |
| <CopyableCode code="customNotificationEmails" /> | `array` | The list of additional emails that are configured to receive notifications about the service. |
| <CopyableCode code="disabled" /> | `boolean` | Indicates if the service is disabled or not. |
| <CopyableCode code="displayName" /> | `string` | The display name of the service. |
| <CopyableCode code="health" /> | `string` | The health of the service. |
| <CopyableCode code="lastDisabled" /> | `string` | The date and time, in UTC, when the service was last disabled. |
| <CopyableCode code="lastUpdated" /> | `string` | The date or time , in UTC, when the service properties were last updated. |
| <CopyableCode code="monitoringConfigurationsComputed" /> | `object` | The monitoring configuration of the service which determines what activities are monitored by Azure Active Directory Connect Health. |
| <CopyableCode code="monitoringConfigurationsCustomized" /> | `object` | The customized monitoring configuration of the service which determines what activities are monitored by Azure Active Directory Connect Health. |
| <CopyableCode code="notificationEmailEnabled" /> | `boolean` | Indicates if email notification is enabled or not. |
| <CopyableCode code="notificationEmailEnabledForGlobalAdmins" /> | `boolean` | Indicates if email notification is enabled for global administrators of the tenant. |
| <CopyableCode code="notificationEmails" /> | `array` | The list of emails to whom service notifications will be sent. |
| <CopyableCode code="notificationEmailsEnabledForGlobalAdmins" /> | `boolean` | Indicates if email notification is enabled for global administrators of the tenant. |
| <CopyableCode code="originalDisabledState" /> | `boolean` | Gets the original disable state. |
| <CopyableCode code="resolvedAlerts" /> | `integer` | The total count of alerts that has been resolved for the service. |
| <CopyableCode code="serviceId" /> | `string` | The id of the service. |
| <CopyableCode code="serviceName" /> | `string` | The name of the service. |
| <CopyableCode code="signature" /> | `string` | The signature of the service. |
| <CopyableCode code="simpleProperties" /> | `object` | List of service specific configuration properties. |
| <CopyableCode code="tenantId" /> | `string` | The id of the tenant to which the service is registered to. |
| <CopyableCode code="type" /> | `string` | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` |  |
