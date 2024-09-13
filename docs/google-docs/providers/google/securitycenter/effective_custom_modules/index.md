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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>effective_custom_module</code> resource or lists <code>effective_custom_modules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>effective_custom_modules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.effective_custom_modules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the custom module. Its format is "organizations/{organization}/securityHealthAnalyticsSettings/effectiveCustomModules/{customModule}", or "folders/{folder}/securityHealthAnalyticsSettings/effectiveCustomModules/{customModule}", or "projects/{project}/securityHealthAnalyticsSettings/effectiveCustomModules/{customModule}" |
| <CopyableCode code="customConfig" /> | `object` | Defines the properties in a custom module configuration for Security Health Analytics. Use the custom module configuration to create custom detectors that generate custom findings for resources that you specify. |
| <CopyableCode code="displayName" /> | `string` | Output only. The display name for the custom module. The name must be between 1 and 128 characters, start with a lowercase letter, and contain alphanumeric characters or underscores only. |
| <CopyableCode code="enablementState" /> | `string` | Output only. The effective state of enablement for the module at the given level of the hierarchy. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_event_threat_detection_settings_effective_custom_modules_get" /> | `SELECT` | <CopyableCode code="effectiveCustomModulesId, foldersId" /> | Gets an effective Event Threat Detection custom module at the given level. |
| <CopyableCode code="folders_event_threat_detection_settings_effective_custom_modules_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors. |
| <CopyableCode code="folders_security_health_analytics_settings_effective_custom_modules_get" /> | `SELECT` | <CopyableCode code="effectiveCustomModulesId, foldersId" /> | Retrieves an EffectiveSecurityHealthAnalyticsCustomModule. |
| <CopyableCode code="folders_security_health_analytics_settings_effective_custom_modules_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Returns a list of all EffectiveSecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
| <CopyableCode code="organizations_event_threat_detection_settings_effective_custom_modules_get" /> | `SELECT` | <CopyableCode code="effectiveCustomModulesId, organizationsId" /> | Gets an effective Event Threat Detection custom module at the given level. |
| <CopyableCode code="organizations_event_threat_detection_settings_effective_custom_modules_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors. |
| <CopyableCode code="organizations_security_health_analytics_settings_effective_custom_modules_get" /> | `SELECT` | <CopyableCode code="effectiveCustomModulesId, organizationsId" /> | Retrieves an EffectiveSecurityHealthAnalyticsCustomModule. |
| <CopyableCode code="organizations_security_health_analytics_settings_effective_custom_modules_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Returns a list of all EffectiveSecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |
| <CopyableCode code="projects_event_threat_detection_settings_effective_custom_modules_get" /> | `SELECT` | <CopyableCode code="effectiveCustomModulesId, projectsId" /> | Gets an effective Event Threat Detection custom module at the given level. |
| <CopyableCode code="projects_event_threat_detection_settings_effective_custom_modules_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors. |
| <CopyableCode code="projects_security_health_analytics_settings_effective_custom_modules_get" /> | `SELECT` | <CopyableCode code="effectiveCustomModulesId, projectsId" /> | Retrieves an EffectiveSecurityHealthAnalyticsCustomModule. |
| <CopyableCode code="projects_security_health_analytics_settings_effective_custom_modules_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Returns a list of all EffectiveSecurityHealthAnalyticsCustomModules for the given parent. This includes resident modules defined at the scope of the parent, and inherited modules, inherited from CRM ancestors. |

## `SELECT` examples

Lists all effective Event Threat Detection custom modules for the given parent. This includes resident modules defined at the scope of the parent along with modules inherited from its ancestors.

```sql
SELECT
name,
customConfig,
displayName,
enablementState
FROM google.securitycenter.effective_custom_modules
WHERE foldersId = '{{ foldersId }}'; 
```
