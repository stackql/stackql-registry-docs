---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
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

Creates, updates, deletes, gets or lists a <code>configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ad_hybrid_health_service.configurations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="aadLicense" /> | `string` | The Azure Active Directory license of the tenant. |
| <CopyableCode code="aadPremium" /> | `boolean` | Indicate if the tenant has Azure Active Directory Premium license or not. |
| <CopyableCode code="agentAutoUpdate" /> | `boolean` | Indicates if the tenant is configured to automatically receive updates for Azure Active Directory Connect Health client side features. |
| <CopyableCode code="alertSuppressionTimeInMins" /> | `integer` | The time in minutes after which an alert will be auto-suppressed. |
| <CopyableCode code="consentedToMicrosoftDevOps" /> | `boolean` | Indicates if the tenant data can be seen by Microsoft through Azure portal. |
| <CopyableCode code="countryLetterCode" /> | `string` | The country letter code of the tenant. |
| <CopyableCode code="createdDate" /> | `string` | The date, in UTC, when the tenant was onboarded to Azure Active Directory Connect Health. |
| <CopyableCode code="devOpsTtl" /> | `string` | The date and time, in UTC, till when the tenant data can be seen by Microsoft through Azure portal. |
| <CopyableCode code="disabled" /> | `boolean` | Indicates if the tenant is disabled in Azure Active Directory Connect Health. |
| <CopyableCode code="disabledReason" /> | `integer` | The reason due to which the tenant was disabled in Azure Active Directory Connect Health. |
| <CopyableCode code="globalAdminsEmail" /> | `array` | The list of global administrators for the tenant. |
| <CopyableCode code="initialDomain" /> | `string` | The initial domain of the tenant. |
| <CopyableCode code="lastDisabled" /> | `string` | The date and time, in UTC, when the tenant was last disabled in Azure Active Directory Connect Health. |
| <CopyableCode code="lastVerified" /> | `string` | The date and time, in UTC, when the tenant onboarding status in Azure Active Directory Connect Health was last verified. |
| <CopyableCode code="onboarded" /> | `boolean` | Indicates if the tenant is already onboarded to Azure Active Directory Connect Health. |
| <CopyableCode code="onboardingAllowed" /> | `boolean` | Indicates if the tenant is allowed to  onboard to Azure Active Directory Connect Health. |
| <CopyableCode code="pksCertificate" /> | `object` | The certificate associated with the tenant to onboard data to Azure Active Directory Connect Health. |
| <CopyableCode code="privatePreviewTenant" /> | `boolean` | Indicates if the tenant has signed up for private preview of Azure Active Directory Connect Health features. |
| <CopyableCode code="tenantId" /> | `string` | The Id of the tenant. |
| <CopyableCode code="tenantInQuarantine" /> | `boolean` | Indicates if data collection for this tenant is disabled or not. |
| <CopyableCode code="tenantName" /> | `string` | The name of the tenant. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="" /> | Gets the details of a tenant onboarded to Azure Active Directory Connect Health. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="" /> | Updates tenant properties for tenants onboarded to Azure Active Directory Connect Health. |
| <CopyableCode code="add" /> | `EXEC` | <CopyableCode code="" /> | Onboards a tenant in Azure Active Directory Connect Health. |

## `SELECT` examples

Gets the details of a tenant onboarded to Azure Active Directory Connect Health.


```sql
SELECT
aadLicense,
aadPremium,
agentAutoUpdate,
alertSuppressionTimeInMins,
consentedToMicrosoftDevOps,
countryLetterCode,
createdDate,
devOpsTtl,
disabled,
disabledReason,
globalAdminsEmail,
initialDomain,
lastDisabled,
lastVerified,
onboarded,
onboardingAllowed,
pksCertificate,
privatePreviewTenant,
tenantId,
tenantInQuarantine,
tenantName
FROM azure.ad_hybrid_health_service.configurations
;
```
## `UPDATE` example

Updates a <code>configurations</code> resource.

```sql
/*+ update */
UPDATE azure.ad_hybrid_health_service.configurations
SET 
tenantId = '{{ tenantId }}',
aadLicense = '{{ aadLicense }}',
aadPremium = true|false,
agentAutoUpdate = true|false,
alertSuppressionTimeInMins = '{{ alertSuppressionTimeInMins }}',
consentedToMicrosoftDevOps = true|false,
countryLetterCode = '{{ countryLetterCode }}',
createdDate = '{{ createdDate }}',
devOpsTtl = '{{ devOpsTtl }}',
disabled = true|false,
disabledReason = '{{ disabledReason }}',
globalAdminsEmail = '{{ globalAdminsEmail }}',
initialDomain = '{{ initialDomain }}',
lastDisabled = '{{ lastDisabled }}',
lastVerified = '{{ lastVerified }}',
onboardingAllowed = true|false,
onboarded = true|false,
pksCertificate = '{{ pksCertificate }}',
privatePreviewTenant = true|false,
tenantInQuarantine = true|false,
tenantName = '{{ tenantName }}'
WHERE 
 = '{{  }}';
```
