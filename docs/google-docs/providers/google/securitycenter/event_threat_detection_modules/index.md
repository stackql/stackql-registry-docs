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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_threat_detection_modules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.event_threat_detection_modules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the Event Threat Detection custom module. Its format is: * "organizations/&#123;organization&#125;/eventThreatDetectionSettings/customModules/&#123;module&#125;". * "folders/&#123;folder&#125;/eventThreatDetectionSettings/customModules/&#123;module&#125;". * "projects/&#123;project&#125;/eventThreatDetectionSettings/customModules/&#123;module&#125;". |
| <CopyableCode code="description" /> | `string` | The description for the module. |
| <CopyableCode code="config" /> | `object` | Config for the module. For the resident module, its config value is defined at this level. For the inherited module, its config value is inherited from the ancestor module. |
| <CopyableCode code="displayName" /> | `string` | The human readable name to be displayed for the module. |
| <CopyableCode code="enablementState" /> | `string` | The state of enablement for the module at the given level of the hierarchy. |
| <CopyableCode code="lastEditor" /> | `string` | Output only. The editor the module was last updated by. |
| <CopyableCode code="type" /> | `string` | Type for the module. e.g. CONFIGURABLE_BAD_IP. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time the module was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_event_threat_detection_settings_custom_modules_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists Event Threat Detection custom modules. |
| <CopyableCode code="organizations_event_threat_detection_settings_custom_modules_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates an Event Threat Detection custom module. |
| <CopyableCode code="organizations_event_threat_detection_settings_custom_modules_delete" /> | `DELETE` | <CopyableCode code="customModulesId, organizationsId" /> | Deletes an Event Threat Detection custom module. |
| <CopyableCode code="_organizations_event_threat_detection_settings_custom_modules_list" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Lists Event Threat Detection custom modules. |
