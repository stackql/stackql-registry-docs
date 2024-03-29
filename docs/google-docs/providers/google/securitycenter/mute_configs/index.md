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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mute_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.mute_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | This field will be ignored if provided on config creation. Format "organizations/&#123;organization&#125;/muteConfigs/&#123;mute_config&#125;" "folders/&#123;folder&#125;/muteConfigs/&#123;mute_config&#125;" "projects/&#123;project&#125;/muteConfigs/&#123;mute_config&#125;" |
| `description` | `string` | A description of the mute config. |
| `updateTime` | `string` | Output only. The most recent time at which the mute config was updated. This field is set by the server and will be ignored if provided on config creation or update. |
| `createTime` | `string` | Output only. The time at which the mute config was created. This field is set by the server and will be ignored if provided on config creation. |
| `displayName` | `string` | The human readable name to be displayed for the mute config. |
| `filter` | `string` | Required. An expression that defines the filter to apply across create/update events of findings. While creating a filter string, be mindful of the scope in which the mute configuration is being created. E.g., If a filter contains project = X but is created under the project = Y scope, it might not match any findings. The following field and operator combinations are supported: * severity: `=`, `:` * category: `=`, `:` * resource.name: `=`, `:` * resource.project_name: `=`, `:` * resource.project_display_name: `=`, `:` * resource.folders.resource_folder: `=`, `:` * resource.parent_name: `=`, `:` * resource.parent_display_name: `=`, `:` * resource.type: `=`, `:` * finding_class: `=`, `:` * indicator.ip_addresses: `=`, `:` * indicator.domains: `=`, `:` |
| `mostRecentEditor` | `string` | Output only. Email address of the user who last edited the mute config. This field is set by the server and will be ignored if provided on config creation or update. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_mute_configs_get` | `SELECT` | `foldersId, muteConfigsId` | Gets a mute config. |
| `folders_mute_configs_list` | `SELECT` | `foldersId` | Lists mute configs. |
| `organizations_mute_configs_get` | `SELECT` | `muteConfigsId, organizationsId` | Gets a mute config. |
| `organizations_mute_configs_list` | `SELECT` | `organizationsId` | Lists mute configs. |
| `projects_mute_configs_get` | `SELECT` | `muteConfigsId, projectsId` | Gets a mute config. |
| `projects_mute_configs_list` | `SELECT` | `projectsId` | Lists mute configs. |
| `folders_mute_configs_create` | `INSERT` | `foldersId` | Creates a mute config. |
| `organizations_mute_configs_create` | `INSERT` | `organizationsId` | Creates a mute config. |
| `projects_mute_configs_create` | `INSERT` | `projectsId` | Creates a mute config. |
| `folders_mute_configs_delete` | `DELETE` | `foldersId, muteConfigsId` | Deletes an existing mute config. |
| `organizations_mute_configs_delete` | `DELETE` | `muteConfigsId, organizationsId` | Deletes an existing mute config. |
| `projects_mute_configs_delete` | `DELETE` | `muteConfigsId, projectsId` | Deletes an existing mute config. |
| `_folders_mute_configs_list` | `EXEC` | `foldersId` | Lists mute configs. |
| `_organizations_mute_configs_list` | `EXEC` | `organizationsId` | Lists mute configs. |
| `_projects_mute_configs_list` | `EXEC` | `projectsId` | Lists mute configs. |
| `folders_mute_configs_patch` | `EXEC` | `foldersId, muteConfigsId` | Updates a mute config. |
| `organizations_mute_configs_patch` | `EXEC` | `muteConfigsId, organizationsId` | Updates a mute config. |
| `projects_mute_configs_patch` | `EXEC` | `muteConfigsId, projectsId` | Updates a mute config. |
