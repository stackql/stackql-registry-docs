---
title: custom_modules_descendant
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_modules_descendant
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

Creates, updates, deletes, gets or lists a <code>custom_modules_descendant</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_modules_descendant</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.custom_modules_descendant" /></td></tr>
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
| <CopyableCode code="folders_event_threat_detection_settings_custom_modules_list_descendant" /> | `SELECT` | <CopyableCode code="foldersId" /> | Lists all resident Event Threat Detection custom modules under the given Resource Manager parent and its descendants. |
| <CopyableCode code="folders_security_health_analytics_settings_custom_modules_list_descendant" /> | `SELECT` | <CopyableCode code="foldersId" /> | Returns a list of all resident SecurityHealthAnalyticsCustomModules under the given CRM parent and all of the parent’s CRM descendants. |
| <CopyableCode code="organizations_event_threat_detection_settings_custom_modules_list_descendant" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists all resident Event Threat Detection custom modules under the given Resource Manager parent and its descendants. |
| <CopyableCode code="organizations_security_health_analytics_settings_custom_modules_list_descendant" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Returns a list of all resident SecurityHealthAnalyticsCustomModules under the given CRM parent and all of the parent’s CRM descendants. |
| <CopyableCode code="projects_event_threat_detection_settings_custom_modules_list_descendant" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists all resident Event Threat Detection custom modules under the given Resource Manager parent and its descendants. |
| <CopyableCode code="projects_security_health_analytics_settings_custom_modules_list_descendant" /> | `SELECT` | <CopyableCode code="projectsId" /> | Returns a list of all resident SecurityHealthAnalyticsCustomModules under the given CRM parent and all of the parent’s CRM descendants. |

## `SELECT` examples

Lists all resident Event Threat Detection custom modules under the given Resource Manager parent and its descendants.

```sql
SELECT
name,
ancestorModule,
customConfig,
displayName,
enablementState,
lastEditor,
updateTime
FROM google.securitycenter.custom_modules_descendant
WHERE foldersId = '{{ foldersId }}'; 
```
