---
title: mute_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - mute_configs
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
<tr><td><b>Name</b></td><td><code>mute_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.mute_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | This field will be ignored if provided on config creation. Format "organizations/&#123;organization&#125;/muteConfigs/&#123;mute_config&#125;" "folders/&#123;folder&#125;/muteConfigs/&#123;mute_config&#125;" "projects/&#123;project&#125;/muteConfigs/&#123;mute_config&#125;" "organizations/&#123;organization&#125;/locations/global/muteConfigs/&#123;mute_config&#125;" "folders/&#123;folder&#125;/locations/global/muteConfigs/&#123;mute_config&#125;" "projects/&#123;project&#125;/locations/global/muteConfigs/&#123;mute_config&#125;" |
| <CopyableCode code="description" /> | `string` | A description of the mute config. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which the mute config was created. This field is set by the server and will be ignored if provided on config creation. |
| <CopyableCode code="displayName" /> | `string` | The human readable name to be displayed for the mute config. |
| <CopyableCode code="filter" /> | `string` | Required. An expression that defines the filter to apply across create/update events of findings. While creating a filter string, be mindful of the scope in which the mute configuration is being created. E.g., If a filter contains project = X but is created under the project = Y scope, it might not match any findings. The following field and operator combinations are supported: * severity: `=`, `:` * category: `=`, `:` * resource.name: `=`, `:` * resource.project_name: `=`, `:` * resource.project_display_name: `=`, `:` * resource.folders.resource_folder: `=`, `:` * resource.parent_name: `=`, `:` * resource.parent_display_name: `=`, `:` * resource.type: `=`, `:` * finding_class: `=`, `:` * indicator.ip_addresses: `=`, `:` * indicator.domains: `=`, `:` |
| <CopyableCode code="mostRecentEditor" /> | `string` | Output only. Email address of the user who last edited the mute config. This field is set by the server and will be ignored if provided on config creation or update. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The most recent time at which the mute config was updated. This field is set by the server and will be ignored if provided on config creation or update. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_locations_mute_configs_get" /> | `SELECT` | <CopyableCode code="foldersId, locationsId, muteConfigsId" /> | Gets a mute config. |
| <CopyableCode code="folders_locations_mute_configs_list" /> | `SELECT` | <CopyableCode code="foldersId, locationsId" /> | Lists mute configs. |
| <CopyableCode code="folders_mute_configs_get" /> | `SELECT` | <CopyableCode code="foldersId, muteConfigsId" /> | Gets a mute config. |
| <CopyableCode code="folders_mute_configs_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Lists mute configs. |
| <CopyableCode code="organizations_locations_mute_configs_get" /> | `SELECT` | <CopyableCode code="locationsId, muteConfigsId, organizationsId" /> | Gets a mute config. |
| <CopyableCode code="organizations_locations_mute_configs_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists mute configs. |
| <CopyableCode code="organizations_mute_configs_get" /> | `SELECT` | <CopyableCode code="muteConfigsId, organizationsId" /> | Gets a mute config. |
| <CopyableCode code="organizations_mute_configs_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists mute configs. |
| <CopyableCode code="projects_locations_mute_configs_get" /> | `SELECT` | <CopyableCode code="locationsId, muteConfigsId, projectsId" /> | Gets a mute config. |
| <CopyableCode code="projects_locations_mute_configs_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists mute configs. |
| <CopyableCode code="projects_mute_configs_get" /> | `SELECT` | <CopyableCode code="muteConfigsId, projectsId" /> | Gets a mute config. |
| <CopyableCode code="projects_mute_configs_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists mute configs. |
| <CopyableCode code="folders_locations_mute_configs_create" /> | `INSERT` | <CopyableCode code="foldersId, locationsId" /> | Creates a mute config. |
| <CopyableCode code="folders_mute_configs_create" /> | `INSERT` | <CopyableCode code="foldersId" /> | Creates a mute config. |
| <CopyableCode code="organizations_locations_mute_configs_create" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a mute config. |
| <CopyableCode code="organizations_mute_configs_create" /> | `INSERT` | <CopyableCode code="organizationsId" /> | Creates a mute config. |
| <CopyableCode code="projects_locations_mute_configs_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a mute config. |
| <CopyableCode code="projects_mute_configs_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a mute config. |
| <CopyableCode code="folders_locations_mute_configs_delete" /> | `DELETE` | <CopyableCode code="foldersId, locationsId, muteConfigsId" /> | Deletes an existing mute config. |
| <CopyableCode code="folders_mute_configs_delete" /> | `DELETE` | <CopyableCode code="foldersId, muteConfigsId" /> | Deletes an existing mute config. |
| <CopyableCode code="organizations_locations_mute_configs_delete" /> | `DELETE` | <CopyableCode code="locationsId, muteConfigsId, organizationsId" /> | Deletes an existing mute config. |
| <CopyableCode code="organizations_mute_configs_delete" /> | `DELETE` | <CopyableCode code="muteConfigsId, organizationsId" /> | Deletes an existing mute config. |
| <CopyableCode code="projects_locations_mute_configs_delete" /> | `DELETE` | <CopyableCode code="locationsId, muteConfigsId, projectsId" /> | Deletes an existing mute config. |
| <CopyableCode code="projects_mute_configs_delete" /> | `DELETE` | <CopyableCode code="muteConfigsId, projectsId" /> | Deletes an existing mute config. |
| <CopyableCode code="folders_locations_mute_configs_patch" /> | `UPDATE` | <CopyableCode code="foldersId, locationsId, muteConfigsId" /> | Updates a mute config. |
| <CopyableCode code="folders_mute_configs_patch" /> | `UPDATE` | <CopyableCode code="foldersId, muteConfigsId" /> | Updates a mute config. |
| <CopyableCode code="organizations_locations_mute_configs_patch" /> | `UPDATE` | <CopyableCode code="locationsId, muteConfigsId, organizationsId" /> | Updates a mute config. |
| <CopyableCode code="organizations_mute_configs_patch" /> | `UPDATE` | <CopyableCode code="muteConfigsId, organizationsId" /> | Updates a mute config. |
| <CopyableCode code="projects_locations_mute_configs_patch" /> | `UPDATE` | <CopyableCode code="locationsId, muteConfigsId, projectsId" /> | Updates a mute config. |
| <CopyableCode code="projects_mute_configs_patch" /> | `UPDATE` | <CopyableCode code="muteConfigsId, projectsId" /> | Updates a mute config. |
| <CopyableCode code="_folders_locations_mute_configs_list" /> | `EXEC` | <CopyableCode code="foldersId, locationsId" /> | Lists mute configs. |
| <CopyableCode code="_folders_mute_configs_list" /> | `EXEC` | <CopyableCode code="foldersId" /> | Lists mute configs. |
| <CopyableCode code="_organizations_locations_mute_configs_list" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Lists mute configs. |
| <CopyableCode code="_organizations_mute_configs_list" /> | `EXEC` | <CopyableCode code="organizationsId" /> | Lists mute configs. |
| <CopyableCode code="_projects_locations_mute_configs_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists mute configs. |
| <CopyableCode code="_projects_mute_configs_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists mute configs. |
