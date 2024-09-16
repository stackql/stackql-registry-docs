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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>mute_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mute_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.securitycenter.mute_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | This field will be ignored if provided on config creation. Format `organizations/{organization}/muteConfigs/{mute_config}` `folders/{folder}/muteConfigs/{mute_config}` `projects/{project}/muteConfigs/{mute_config}` `organizations/{organization}/locations/global/muteConfigs/{mute_config}` `folders/{folder}/locations/global/muteConfigs/{mute_config}` `projects/{project}/locations/global/muteConfigs/{mute_config}` |
| <CopyableCode code="description" /> | `string` | A description of the mute config. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which the mute config was created. This field is set by the server and will be ignored if provided on config creation. |
| <CopyableCode code="displayName" /> | `string` | The human readable name to be displayed for the mute config. |
| <CopyableCode code="expiryTime" /> | `string` | Optional. The expiry of the mute config. Only applicable for dynamic configs. If the expiry is set, when the config expires, it is removed from all findings. |
| <CopyableCode code="filter" /> | `string` | Required. An expression that defines the filter to apply across create/update events of findings. While creating a filter string, be mindful of the scope in which the mute configuration is being created. E.g., If a filter contains project = X but is created under the project = Y scope, it might not match any findings. The following field and operator combinations are supported: * severity: `=`, `:` * category: `=`, `:` * resource.name: `=`, `:` * resource.project_name: `=`, `:` * resource.project_display_name: `=`, `:` * resource.folders.resource_folder: `=`, `:` * resource.parent_name: `=`, `:` * resource.parent_display_name: `=`, `:` * resource.type: `=`, `:` * finding_class: `=`, `:` * indicator.ip_addresses: `=`, `:` * indicator.domains: `=`, `:` |
| <CopyableCode code="mostRecentEditor" /> | `string` | Output only. Email address of the user who last edited the mute config. This field is set by the server and will be ignored if provided on config creation or update. |
| <CopyableCode code="type" /> | `string` | Optional. The type of the mute config, which determines what type of mute state the config affects. The static mute state takes precedence over the dynamic mute state. Immutable after creation. STATIC by default if not set during creation. |
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

## `SELECT` examples

Lists mute configs.

```sql
SELECT
name,
description,
createTime,
displayName,
expiryTime,
filter,
mostRecentEditor,
type,
updateTime
FROM google.securitycenter.mute_configs
WHERE foldersId = '{{ foldersId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>mute_configs</code> resource.

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
INSERT INTO google.securitycenter.mute_configs (
foldersId,
name,
displayName,
description,
filter,
type,
expiryTime
)
SELECT 
'{{ foldersId }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ filter }}',
'{{ type }}',
'{{ expiryTime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: description
      value: '{{ description }}'
    - name: filter
      value: '{{ filter }}'
    - name: type
      value: '{{ type }}'
    - name: expiryTime
      value: '{{ expiryTime }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>mute_configs</code> resource.

```sql
/*+ update */
UPDATE google.securitycenter.mute_configs
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
filter = '{{ filter }}',
type = '{{ type }}',
expiryTime = '{{ expiryTime }}'
WHERE 
foldersId = '{{ foldersId }}'
AND muteConfigsId = '{{ muteConfigsId }}';
```

## `DELETE` example

Deletes the specified <code>mute_configs</code> resource.

```sql
/*+ delete */
DELETE FROM google.securitycenter.mute_configs
WHERE foldersId = '{{ foldersId }}'
AND muteConfigsId = '{{ muteConfigsId }}';
```
