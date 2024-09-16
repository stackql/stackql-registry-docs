---
title: preference_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - preference_sets
  - migrationcenter
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

Creates, updates, deletes, gets or lists a <code>preference_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>preference_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.migrationcenter.preference_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the preference set. |
| <CopyableCode code="description" /> | `string` | A description of the preference set. |
| <CopyableCode code="createTime" /> | `string` | Output only. The timestamp when the preference set was created. |
| <CopyableCode code="displayName" /> | `string` | User-friendly display name. Maximum length is 63 characters. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The timestamp when the preference set was last updated. |
| <CopyableCode code="virtualMachinePreferences" /> | `object` | VirtualMachinePreferences enables you to create sets of assumptions, for example, a geographical location and pricing track, for your migrated virtual machines. The set of preferences influence recommendations for migrating virtual machine assets. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, preferenceSetsId, projectsId" /> | Gets the details of a preference set. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists all the preference sets in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new preference set in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, preferenceSetsId, projectsId" /> | Deletes a preference set. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, preferenceSetsId, projectsId" /> | Updates the parameters of a preference set. |

## `SELECT` examples

Lists all the preference sets in a given project and location.

```sql
SELECT
name,
description,
createTime,
displayName,
updateTime,
virtualMachinePreferences
FROM google.migrationcenter.preference_sets
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>preference_sets</code> resource.

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
INSERT INTO google.migrationcenter.preference_sets (
locationsId,
projectsId,
name,
createTime,
updateTime,
displayName,
description,
virtualMachinePreferences
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ displayName }}',
'{{ description }}',
'{{ virtualMachinePreferences }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: description
      value: '{{ description }}'
    - name: virtualMachinePreferences
      value: '{{ virtualMachinePreferences }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>preference_sets</code> resource.

```sql
/*+ update */
UPDATE google.migrationcenter.preference_sets
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
virtualMachinePreferences = '{{ virtualMachinePreferences }}'
WHERE 
locationsId = '{{ locationsId }}'
AND preferenceSetsId = '{{ preferenceSetsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>preference_sets</code> resource.

```sql
/*+ delete */
DELETE FROM google.migrationcenter.preference_sets
WHERE locationsId = '{{ locationsId }}'
AND preferenceSetsId = '{{ preferenceSetsId }}'
AND projectsId = '{{ projectsId }}';
```
