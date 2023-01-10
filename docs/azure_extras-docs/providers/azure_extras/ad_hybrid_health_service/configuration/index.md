---
title: configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration
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
<tr><td><b>Name</b></td><td><code>configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.ad_hybrid_health_service.configuration</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `onboarded` | `boolean` | Indicates if the tenant is already onboarded to Azure Active Directory Connect Health. |
| `consentedToMicrosoftDevOps` | `boolean` | Indicates if the tenant data can be seen by Microsoft through Azure portal. |
| `countryLetterCode` | `string` | The country letter code of the tenant. |
| `tenantInQuarantine` | `boolean` | Indicates if data collection for this tenant is disabled or not. |
| `agentAutoUpdate` | `boolean` | Indicates if the tenant is configured to automatically receive updates for Azure Active Directory Connect Health client side features. |
| `createdDate` | `string` | The date, in UTC, when the tenant was onboarded to Azure Active Directory Connect Health. |
| `aadPremium` | `boolean` | Indicate if the tenant has Azure Active Directory Premium license or not. |
| `tenantId` | `string` | The Id of the tenant. |
| `tenantName` | `string` | The name of the tenant. |
| `initialDomain` | `string` | The initial domain of the tenant. |
| `privatePreviewTenant` | `boolean` | Indicates if the tenant has signed up for private preview of Azure Active Directory Connect Health features. |
| `disabledReason` | `integer` | The reason due to which the tenant was disabled in Azure Active Directory Connect Health. |
| `lastDisabled` | `string` | The date and time, in UTC, when the tenant was last disabled in Azure Active Directory Connect Health. |
| `lastVerified` | `string` | The date and time, in UTC, when the tenant onboarding status in Azure Active Directory Connect Health was last verified. |
| `globalAdminsEmail` | `array` | The list of global administrators for the tenant. |
| `aadLicense` | `string` | The Azure Active Directory license of the tenant. |
| `disabled` | `boolean` | Indicates if the tenant is disabled in Azure Active Directory Connect Health. |
| `onboardingAllowed` | `boolean` | Indicates if the tenant is allowed to  onboard to Azure Active Directory Connect Health. |
| `pksCertificate` | `object` | The certificate associated with the tenant to onboard data to Azure Active Directory Connect Health. |
| `alertSuppressionTimeInMins` | `integer` | The time in minutes after which an alert will be auto-suppressed. |
| `devOpsTtl` | `string` | The date and time, in UTC, till when the tenant data can be seen by Microsoft through Azure portal. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` |  | Gets the details of a tenant onboarded to Azure Active Directory Connect Health. |
| `add` | `INSERT` |  | Onboards a tenant in Azure Active Directory Connect Health. |
| `listAddsConfigurations` | `EXEC` | `serviceName` | Gets the service configurations. |
| `update` | `EXEC` |  | Updates tenant properties for tenants onboarded to Azure Active Directory Connect Health. |
