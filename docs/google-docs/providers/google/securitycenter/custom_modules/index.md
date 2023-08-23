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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_modules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.custom_modules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the Event Threat Detection custom module. Its format is: * "organizations/&#123;organization&#125;/eventThreatDetectionSettings/customModules/&#123;module&#125;". * "folders/&#123;folder&#125;/eventThreatDetectionSettings/customModules/&#123;module&#125;". * "projects/&#123;project&#125;/eventThreatDetectionSettings/customModules/&#123;module&#125;". |
| `description` | `string` | The description for the module. |
| `config` | `object` | Config for the module. For the resident module, its config value is defined at this level. For the inherited module, its config value is inherited from the ancestor module. |
| `displayName` | `string` | The human readable name to be displayed for the module. |
| `enablementState` | `string` | The state of enablement for the module at the given level of the hierarchy. |
| `lastEditor` | `string` | Output only. The editor the module was last updated by. |
| `type` | `string` | Type for the module. e.g. CONFIGURABLE_BAD_IP. |
| `updateTime` | `string` | Output only. The time the module was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_event_threat_detection_settings_custom_modules_get` | `SELECT` | `customModulesId, organizationsId` | Gets an Event Threat Detection custom module. |
| `folders_security_health_analytics_settings_custom_modules_patch` | `EXEC` | `customModulesId, foldersId` | Updates the SecurityHealthAnalyticsCustomModule under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom config of a module is supported on resident modules only. |
| `organizations_event_threat_detection_settings_custom_modules_patch` | `EXEC` | `customModulesId, organizationsId` | Updates an Event Threat Detection custom module. |
| `organizations_security_health_analytics_settings_custom_modules_patch` | `EXEC` | `customModulesId, organizationsId` | Updates the SecurityHealthAnalyticsCustomModule under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom config of a module is supported on resident modules only. |
| `projects_security_health_analytics_settings_custom_modules_patch` | `EXEC` | `customModulesId, projectsId` | Updates the SecurityHealthAnalyticsCustomModule under the given name based on the given update mask. Updating the enablement state is supported on both resident and inherited modules (though resident modules cannot have an enablement state of "inherited"). Updating the display name and custom config of a module is supported on resident modules only. |
