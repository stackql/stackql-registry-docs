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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_modules_descendant</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.custom_modules_descendant" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the custom module. Its format is "organizations/&#123;organization&#125;/securityHealthAnalyticsSettings/customModules/&#123;customModule&#125;", or "folders/&#123;folder&#125;/securityHealthAnalyticsSettings/customModules/&#123;customModule&#125;", or "projects/&#123;project&#125;/securityHealthAnalyticsSettings/customModules/&#123;customModule&#125;" The id &#123;customModule&#125; is server-generated and is not user settable. It will be a numeric id containing 1-20 digits. |
| <CopyableCode code="ancestorModule" /> | `string` | Output only. If empty, indicates that the custom module was created in the organization, folder, or project in which you are viewing the custom module. Otherwise, `ancestor_module` specifies the organization or folder from which the custom module is inherited. |
| <CopyableCode code="customConfig" /> | `object` | Defines the properties in a custom module configuration for Security Health Analytics. Use the custom module configuration to create custom detectors that generate custom findings for resources that you specify. |
| <CopyableCode code="displayName" /> | `string` | The display name of the Security Health Analytics custom module. This display name becomes the finding category for all findings that are returned by this custom module. The display name must be between 1 and 128 characters, start with a lowercase letter, and contain alphanumeric characters or underscores only. |
| <CopyableCode code="enablementState" /> | `string` | The enablement state of the custom module. |
| <CopyableCode code="lastEditor" /> | `string` | Output only. The editor that last updated the custom module. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time at which the custom module was last updated. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="folders_security_health_analytics_settings_custom_modules_list_descendant" /> | `SELECT` | <CopyableCode code="foldersId" /> |
| <CopyableCode code="organizations_security_health_analytics_settings_custom_modules_list_descendant" /> | `SELECT` | <CopyableCode code="organizationsId" /> |
| <CopyableCode code="projects_security_health_analytics_settings_custom_modules_list_descendant" /> | `SELECT` | <CopyableCode code="projectsId" /> |
| <CopyableCode code="_folders_security_health_analytics_settings_custom_modules_list_descendant" /> | `EXEC` | <CopyableCode code="foldersId" /> |
| <CopyableCode code="_organizations_security_health_analytics_settings_custom_modules_list_descendant" /> | `EXEC` | <CopyableCode code="organizationsId" /> |
| <CopyableCode code="_projects_security_health_analytics_settings_custom_modules_list_descendant" /> | `EXEC` | <CopyableCode code="projectsId" /> |
