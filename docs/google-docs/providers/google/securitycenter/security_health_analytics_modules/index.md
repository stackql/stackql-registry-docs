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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>security_health_analytics_module</code> resource or lists <code>security_health_analytics_modules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_health_analytics_modules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.security_health_analytics_modules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the custom module. Its format is "organizations/{organization}/securityHealthAnalyticsSettings/customModules/{customModule}", or "folders/{folder}/securityHealthAnalyticsSettings/customModules/{customModule}", or "projects/{project}/securityHealthAnalyticsSettings/customModules/{customModule}" The id {customModule} is server-generated and is not user settable. It will be a numeric id containing 1-20 digits. |
| <CopyableCode code="ancestorModule" /> | `string` | Output only. If empty, indicates that the custom module was created in the organization, folder, or project in which you are viewing the custom module. Otherwise, `ancestor_module` specifies the organization or folder from which the custom module is inherited. |
| <CopyableCode code="customConfig" /> | `object` | Defines the properties in a custom module configuration for Security Health Analytics. Use the custom module configuration to create custom detectors that generate custom findings for resources that you specify. |
| <CopyableCode code="displayName" /> | `string` | The display name of the Security Health Analytics custom module. This display name becomes the finding category for all findings that are returned by this custom module. The display name must be between 1 and 128 characters, start with a lowercase letter, and contain alphanumeric characters or underscores only. |
| <CopyableCode code="enablementState" /> | `string` | The enablement state of the custom module. |
| <CopyableCode code="lastEditor" /> | `string` | Output only. The editor that last updated the custom module. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time at which the custom module was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_security_health_analytics_settings_custom_modules_get" /> | `SELECT` | <CopyableCode code="customModulesId, foldersId" /> | Retrieves a SecurityHealthAnalyticsCustomModule. |
| <CopyableCode code="folders_security_health_analytics_settings_custom_modules_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Returns a list of all SecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
| <CopyableCode code="organizations_security_health_analytics_settings_custom_modules_get" /> | `SELECT` | <CopyableCode code="customModulesId, organizationsId" /> | Retrieves a SecurityHealthAnalyticsCustomModule. |
| <CopyableCode code="organizations_security_health_analytics_settings_custom_modules_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Returns a list of all SecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
| <CopyableCode code="projects_security_health_analytics_settings_custom_modules_get" /> | `SELECT` | <CopyableCode code="customModulesId, projectsId" /> | Retrieves a SecurityHealthAnalyticsCustomModule. |
| <CopyableCode code="projects_security_health_analytics_settings_custom_modules_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Returns a list of all SecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
| <CopyableCode code="folders_security_health_analytics_settings_custom_modules_create" /> | `INSERT` | <CopyableCode code="foldersId" /> | Creates a resident SecurityHealthAnalyticsCustomModule at the scope of the given CRM parent, and also creates inherited SecurityHealthAnalyticsCustomModules for all CRM descendants of the given parent. These modules are enabled by default. |
| <CopyableCode code="organizations_security_health_analytics_settings_custom_modules_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a resident SecurityHealthAnalyticsCustomModule at the scope of the given CRM parent, and also creates inherited SecurityHealthAnalyticsCustomModules for all CRM descendants of the given parent. These modules are enabled by default. |
| <CopyableCode code="projects_security_health_analytics_settings_custom_modules_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a resident SecurityHealthAnalyticsCustomModule at the scope of the given CRM parent, and also creates inherited SecurityHealthAnalyticsCustomModules for all CRM descendants of the given parent. These modules are enabled by default. |
| <CopyableCode code="folders_security_health_analytics_settings_custom_modules_delete" /> | `DELETE` | <CopyableCode code="customModulesId, foldersId" /> | Deletes the specified SecurityHealthAnalyticsCustomModule and all of its descendants in the CRM hierarchy. This method is only supported for resident custom modules. |
| <CopyableCode code="organizations_security_health_analytics_settings_custom_modules_delete" /> | `DELETE` | <CopyableCode code="customModulesId, organizationsId" /> | Deletes the specified SecurityHealthAnalyticsCustomModule and all of its descendants in the CRM hierarchy. This method is only supported for resident custom modules. |
| <CopyableCode code="projects_security_health_analytics_settings_custom_modules_delete" /> | `DELETE` | <CopyableCode code="customModulesId, projectsId" /> | Deletes the specified SecurityHealthAnalyticsCustomModule and all of its descendants in the CRM hierarchy. This method is only supported for resident custom modules. |

## `SELECT` examples

Returns a list of all SecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors.

```sql
SELECT
name,
ancestorModule,
customConfig,
displayName,
enablementState,
lastEditor,
updateTime
FROM google.securitycenter.security_health_analytics_modules
WHERE foldersId = '{{ foldersId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>security_health_analytics_modules</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.securitycenter.security_health_analytics_modules (
foldersId,
name,
displayName,
enablementState,
updateTime,
lastEditor,
ancestorModule,
customConfig
)
SELECT 
'{{ foldersId }}',
'{{ name }}',
'{{ displayName }}',
'{{ enablementState }}',
'{{ updateTime }}',
'{{ lastEditor }}',
'{{ ancestorModule }}',
'{{ customConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: enablementState
        value: '{{ enablementState }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: lastEditor
        value: '{{ lastEditor }}'
      - name: ancestorModule
        value: '{{ ancestorModule }}'
      - name: customConfig
        value: '{{ customConfig }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified security_health_analytics_module resource.

```sql
DELETE FROM google.securitycenter.security_health_analytics_modules
WHERE customModulesId = '{{ customModulesId }}'
AND foldersId = '{{ foldersId }}';
```
