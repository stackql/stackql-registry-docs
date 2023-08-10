---
title: effective_custom_modules
hide_title: false
hide_table_of_contents: false
keywords:
  - effective_custom_modules
  - securitycenter
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>effective_custom_modules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.effective_custom_modules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The resource name of the custom module. Its format is "organizations/&#123;organization&#125;/securityHealthAnalyticsSettings/effectiveCustomModules/&#123;customModule&#125;", or "folders/&#123;folder&#125;/securityHealthAnalyticsSettings/effectiveCustomModules/&#123;customModule&#125;", or "projects/&#123;project&#125;/securityHealthAnalyticsSettings/effectiveCustomModules/&#123;customModule&#125;" |
| `displayName` | `string` | Output only. The display name for the custom module. The name must be between 1 and 128 characters, start with a lowercase letter, and contain alphanumeric characters or underscores only. |
| `enablementState` | `string` | Output only. The effective state of enablement for the module at the given level of the hierarchy. |
| `customConfig` | `object` | Defines the properties in a custom module configuration for Security Health Analytics. Use the custom module configuration to create custom detectors that generate custom findings for resources that you specify. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_security_health_analytics_settings_effective_custom_modules_get` | `SELECT` | `effectiveCustomModulesId, foldersId` | Retrieves an EffectiveSecurityHealthAnalyticsCustomModule. |
| `folders_security_health_analytics_settings_effective_custom_modules_list` | `SELECT` | `foldersId` | Returns a list of all EffectiveSecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
| `organizations_security_health_analytics_settings_effective_custom_modules_get` | `SELECT` | `effectiveCustomModulesId, organizationsId` | Retrieves an EffectiveSecurityHealthAnalyticsCustomModule. |
| `organizations_security_health_analytics_settings_effective_custom_modules_list` | `SELECT` | `organizationsId` | Returns a list of all EffectiveSecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
| `projects_security_health_analytics_settings_effective_custom_modules_get` | `SELECT` | `effectiveCustomModulesId, projectsId` | Retrieves an EffectiveSecurityHealthAnalyticsCustomModule. |
| `projects_security_health_analytics_settings_effective_custom_modules_list` | `SELECT` | `projectsId` | Returns a list of all EffectiveSecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
| `_folders_security_health_analytics_settings_effective_custom_modules_list` | `EXEC` | `foldersId` | Returns a list of all EffectiveSecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
| `_organizations_security_health_analytics_settings_effective_custom_modules_list` | `EXEC` | `organizationsId` | Returns a list of all EffectiveSecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
| `_projects_security_health_analytics_settings_effective_custom_modules_list` | `EXEC` | `projectsId` | Returns a list of all EffectiveSecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
