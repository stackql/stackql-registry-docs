---
title: event_threat_detection_modules
hide_title: false
hide_table_of_contents: false
keywords:
  - event_threat_detection_modules
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
<tr><td><b>Name</b></td><td><code>event_threat_detection_modules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.event_threat_detection_modules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the Event Threat Detection custom module. Its format is: * "organizations/&#123;organization&#125;/eventThreatDetectionSettings/customModules/&#123;module&#125;". * "folders/&#123;folder&#125;/eventThreatDetectionSettings/customModules/&#123;module&#125;". * "projects/&#123;project&#125;/eventThreatDetectionSettings/customModules/&#123;module&#125;". |
| `description` | `string` | The description for the module. |
| `enablementState` | `string` | The state of enablement for the module at the given level of the hierarchy. |
| `lastEditor` | `string` | Output only. The editor the module was last updated by. |
| `type` | `string` | Type for the module. e.g. CONFIGURABLE_BAD_IP. |
| `updateTime` | `string` | Output only. The time the module was last updated. |
| `config` | `object` | Config for the module. For the resident module, its config value is defined at this level. For the inherited module, its config value is inherited from the ancestor module. |
| `displayName` | `string` | The human readable name to be displayed for the module. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_event_threat_detection_settings_custom_modules_list` | `SELECT` | `organizationsId` | Lists Event Threat Detection custom modules. |
| `organizations_event_threat_detection_settings_custom_modules_create` | `INSERT` | `organizationsId` | Creates an Event Threat Detection custom module. |
| `organizations_event_threat_detection_settings_custom_modules_delete` | `DELETE` | `customModulesId, organizationsId` | Deletes an Event Threat Detection custom module. |
| `_organizations_event_threat_detection_settings_custom_modules_list` | `EXEC` | `organizationsId` | Lists Event Threat Detection custom modules. |
