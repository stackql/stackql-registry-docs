---
title: custom_modules
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_modules
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

Creates, updates, deletes, gets or lists a <code>custom_modules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_modules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.custom_modules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the Event Threat Detection custom module. Its format is: * `organizations/{organization}/eventThreatDetectionSettings/customModules/{module}`. * `folders/{folder}/eventThreatDetectionSettings/customModules/{module}`. * `projects/{project}/eventThreatDetectionSettings/customModules/{module}`. |
| <CopyableCode code="description" /> | `string` | The description for the module. |
| <CopyableCode code="ancestorModule" /> | `string` | Output only. The closest ancestor module that this module inherits the enablement state from. The format is the same as the EventThreatDetectionCustomModule resource name. |
| <CopyableCode code="config" /> | `object` | Config for the module. For the resident module, its config value is defined at this level. For the inherited module, its config value is inherited from the ancestor module. |
| <CopyableCode code="displayName" /> | `string` | The human readable name to be displayed for the module. |
| <CopyableCode code="enablementState" /> | `string` | The state of enablement for the module at the given level of the hierarchy. |
| <CopyableCode code="lastEditor" /> | `string` | Output only. The editor the module was last updated by. |
| <CopyableCode code="type" /> | `string` | Type for the module. e.g. CONFIGURABLE_BAD_IP. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time the module was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_event_threat_detection_settings_custom_modules_get" /> | `SELECT` | <CopyableCode code="customModulesId, foldersId" /> | Gets an Event Threat Detection custom module. |
| <CopyableCode code="organizations_event_threat_detection_settings_custom_modules_get" /> | `SELECT` | <CopyableCode code="customModulesId, organizationsId" /> | Gets an Event Threat Detection custom module. |
| <CopyableCode code="projects_event_threat_detection_settings_custom_modules_get" /> | `SELECT` | <CopyableCode code="customModulesId, projectsId" /> | Gets an Event Threat Detection custom module. |
| <CopyableCode code="folders_event_threat_detection_settings_custom_modules_patch" /> | `UPDATE` | <CopyableCode code="customModulesId, foldersId" /> | Updates the Event Threat Detection custom module with the given name based on the given update mask. Updating the enablement state is supported for both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name or configuration of a module is supported for resident modules only. The type of a module cannot be changed. |
| <CopyableCode code="folders_security_health_analytics_settings_custom_modules_patch" /> | `UPDATE` | <CopyableCode code="customModulesId, foldersId" /> | Updates the SecurityHealthAnalyticsCustomModule under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom config of a module is supported on resident modules only. |
| <CopyableCode code="organizations_event_threat_detection_settings_custom_modules_patch" /> | `UPDATE` | <CopyableCode code="customModulesId, organizationsId" /> | Updates the Event Threat Detection custom module with the given name based on the given update mask. Updating the enablement state is supported for both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name or configuration of a module is supported for resident modules only. The type of a module cannot be changed. |
| <CopyableCode code="organizations_security_health_analytics_settings_custom_modules_patch" /> | `UPDATE` | <CopyableCode code="customModulesId, organizationsId" /> | Updates the SecurityHealthAnalyticsCustomModule under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom config of a module is supported on resident modules only. |
| <CopyableCode code="projects_event_threat_detection_settings_custom_modules_patch" /> | `UPDATE` | <CopyableCode code="customModulesId, projectsId" /> | Updates the Event Threat Detection custom module with the given name based on the given update mask. Updating the enablement state is supported for both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name or configuration of a module is supported for resident modules only. The type of a module cannot be changed. |
| <CopyableCode code="projects_security_health_analytics_settings_custom_modules_patch" /> | `UPDATE` | <CopyableCode code="customModulesId, projectsId" /> | Updates the SecurityHealthAnalyticsCustomModule under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom config of a module is supported on resident modules only. |
| <CopyableCode code="folders_security_health_analytics_settings_custom_modules_simulate" /> | `EXEC` | <CopyableCode code="foldersId" /> | Simulates a given SecurityHealthAnalyticsCustomModule and Resource. |
| <CopyableCode code="organizations_security_health_analytics_settings_custom_modules_simulate" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Simulates a given SecurityHealthAnalyticsCustomModule and Resource. |
| <CopyableCode code="projects_security_health_analytics_settings_custom_modules_simulate" /> | `EXEC` | <CopyableCode code="projectsId" /> | Simulates a given SecurityHealthAnalyticsCustomModule and Resource. |

## `SELECT` examples

Gets an Event Threat Detection custom module.

```sql
SELECT
name,
description,
ancestorModule,
config,
displayName,
enablementState,
lastEditor,
type,
updateTime
FROM google.securitycenter.custom_modules
WHERE customModulesId = '{{ customModulesId }}'
AND foldersId = '{{ foldersId }}'; 
```

## `UPDATE` example

Updates a <code>custom_modules</code> resource.

```sql
/*+ update */
UPDATE google.securitycenter.custom_modules
SET 
name = '{{ name }}',
config = '{{ config }}',
enablementState = '{{ enablementState }}',
type = '{{ type }}',
displayName = '{{ displayName }}',
description = '{{ description }}'
WHERE 
customModulesId = '{{ customModulesId }}'
AND foldersId = '{{ foldersId }}';
```
