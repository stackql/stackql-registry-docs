---
title: security_health_analytics_modules
hide_title: false
hide_table_of_contents: false
keywords:
  - security_health_analytics_modules
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
<tr><td><b>Name</b></td><td><code>security_health_analytics_modules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.security_health_analytics_modules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the custom module. Its format is "organizations/&#123;organization&#125;/securityHealthAnalyticsSettings/customModules/&#123;customModule&#125;", or "folders/&#123;folder&#125;/securityHealthAnalyticsSettings/customModules/&#123;customModule&#125;", or "projects/&#123;project&#125;/securityHealthAnalyticsSettings/customModules/&#123;customModule&#125;" The id &#123;customModule&#125; is server-generated and is not user settable. It will be a numeric id containing 1-20 digits. |
| `enablementState` | `string` | The enablement state of the custom module. |
| `lastEditor` | `string` | Output only. The editor that last updated the custom module. |
| `updateTime` | `string` | Output only. The time at which the custom module was last updated. |
| `ancestorModule` | `string` | Output only. If empty, indicates that the custom module was created in the organization, folder, or project in which you are viewing the custom module. Otherwise, `ancestor_module` specifies the organization or folder from which the custom module is inherited. |
| `customConfig` | `object` | Defines the properties in a custom module configuration for Security Health Analytics. Use the custom module configuration to create custom detectors that generate custom findings for resources that you specify. |
| `displayName` | `string` | The display name of the Security Health Analytics custom module. This display name becomes the finding category for all findings that are returned by this custom module. The display name must be between 1 and 128 characters, start with a lowercase letter, and contain alphanumeric characters or underscores only. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_security_health_analytics_settings_custom_modules_get` | `SELECT` | `customModulesId, foldersId` | Retrieves a SecurityHealthAnalyticsCustomModule. |
| `folders_security_health_analytics_settings_custom_modules_list` | `SELECT` | `foldersId` | Returns a list of all SecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
| `organizations_security_health_analytics_settings_custom_modules_get` | `SELECT` | `customModulesId, organizationsId` | Retrieves a SecurityHealthAnalyticsCustomModule. |
| `organizations_security_health_analytics_settings_custom_modules_list` | `SELECT` | `organizationsId` | Returns a list of all SecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
| `projects_security_health_analytics_settings_custom_modules_get` | `SELECT` | `customModulesId, projectsId` | Retrieves a SecurityHealthAnalyticsCustomModule. |
| `projects_security_health_analytics_settings_custom_modules_list` | `SELECT` | `projectsId` | Returns a list of all SecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
| `folders_security_health_analytics_settings_custom_modules_create` | `INSERT` | `foldersId` | Creates a resident SecurityHealthAnalyticsCustomModule at the scope of the given CRM parent, and also creates inherited SecurityHealthAnalyticsCustomModules for all CRM descendants of the given parent. These modules are enabled by default. |
| `organizations_security_health_analytics_settings_custom_modules_create` | `INSERT` | `organizationsId` | Creates a resident SecurityHealthAnalyticsCustomModule at the scope of the given CRM parent, and also creates inherited SecurityHealthAnalyticsCustomModules for all CRM descendants of the given parent. These modules are enabled by default. |
| `projects_security_health_analytics_settings_custom_modules_create` | `INSERT` | `projectsId` | Creates a resident SecurityHealthAnalyticsCustomModule at the scope of the given CRM parent, and also creates inherited SecurityHealthAnalyticsCustomModules for all CRM descendants of the given parent. These modules are enabled by default. |
| `folders_security_health_analytics_settings_custom_modules_delete` | `DELETE` | `customModulesId, foldersId` | Deletes the specified SecurityHealthAnalyticsCustomModule and all of its descendants in the CRM hierarchy. This method is only supported for resident custom modules. |
| `organizations_security_health_analytics_settings_custom_modules_delete` | `DELETE` | `customModulesId, organizationsId` | Deletes the specified SecurityHealthAnalyticsCustomModule and all of its descendants in the CRM hierarchy. This method is only supported for resident custom modules. |
| `projects_security_health_analytics_settings_custom_modules_delete` | `DELETE` | `customModulesId, projectsId` | Deletes the specified SecurityHealthAnalyticsCustomModule and all of its descendants in the CRM hierarchy. This method is only supported for resident custom modules. |
| `_folders_security_health_analytics_settings_custom_modules_list` | `EXEC` | `foldersId` | Returns a list of all SecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
| `_organizations_security_health_analytics_settings_custom_modules_list` | `EXEC` | `organizationsId` | Returns a list of all SecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
| `_projects_security_health_analytics_settings_custom_modules_list` | `EXEC` | `projectsId` | Returns a list of all SecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
