---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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

Creates, updates, deletes, gets or lists a <code>services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.services" /></td></tr>
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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="serviceName" /> | Gets the details of a service for a tenant having Azure AD Premium license and is onboarded to Azure Active Directory Connect Health. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Gets the details of services, for a tenant, that are onboarded to Azure Active Directory Connect Health. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="serviceName" /> | Deletes a service which is onboarded to Azure Active Directory Connect Health. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="serviceName" /> | Updates the service properties of an onboarded service. |
| <CopyableCode code="add" /> | `EXEC` | <CopyableCode code="" /> | Onboards a service for a given tenant in Azure Active Directory Connect Health. |
| <CopyableCode code="add_alert_feedback" /> | `EXEC` | <CopyableCode code="serviceName" /> | Adds an alert feedback submitted by customer. |
| <CopyableCode code="update_monitoring_configuration" /> | `EXEC` | <CopyableCode code="serviceName" /> | Updates the service level monitoring configuration. |

## `SELECT` examples

Gets the details of services, for a tenant, that are onboarded to Azure Active Directory Connect Health.


```sql
SELECT
id,
activeAlerts,
additionalInformation,
createdDate,
customNotificationEmails,
disabled,
displayName,
health,
lastDisabled,
lastUpdated,
monitoringConfigurationsComputed,
monitoringConfigurationsCustomized,
notificationEmailEnabled,
notificationEmailEnabledForGlobalAdmins,
notificationEmails,
notificationEmailsEnabledForGlobalAdmins,
originalDisabledState,
resolvedAlerts,
serviceId,
serviceName,
signature,
simpleProperties,
tenantId,
type
FROM azure.ad_hybrid_health_service.services
;
```
## `UPDATE` example

Updates a <code>services</code> resource.

```sql
/*+ update */
UPDATE azure.ad_hybrid_health_service.services
SET 
id = '{{ id }}',
activeAlerts = '{{ activeAlerts }}',
additionalInformation = '{{ additionalInformation }}',
createdDate = '{{ createdDate }}',
customNotificationEmails = '{{ customNotificationEmails }}',
disabled = true|false,
displayName = '{{ displayName }}',
health = '{{ health }}',
lastDisabled = '{{ lastDisabled }}',
lastUpdated = '{{ lastUpdated }}',
monitoringConfigurationsComputed = '{{ monitoringConfigurationsComputed }}',
monitoringConfigurationsCustomized = '{{ monitoringConfigurationsCustomized }}',
notificationEmailEnabled = true|false,
notificationEmailEnabledForGlobalAdmins = true|false,
notificationEmailsEnabledForGlobalAdmins = true|false,
notificationEmails = '{{ notificationEmails }}',
originalDisabledState = true|false,
resolvedAlerts = '{{ resolvedAlerts }}',
serviceId = '{{ serviceId }}',
serviceName = '{{ serviceName }}',
signature = '{{ signature }}',
simpleProperties = '{{ simpleProperties }}',
tenantId = '{{ tenantId }}',
type = '{{ type }}'
WHERE 
serviceName = '{{ serviceName }}';
```

## `DELETE` example

Deletes the specified <code>services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.ad_hybrid_health_service.services
WHERE serviceName = '{{ serviceName }}';
```
