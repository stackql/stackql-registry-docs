---
title: attestors
hide_title: false
hide_table_of_contents: false
keywords:
  - attestors
  - binaryauthorization
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

Creates, updates, deletes, gets or lists a <code>attestors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>attestors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.binaryauthorization.attestors" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name, in the format: `projects/*/attestors/*`. This field may not be updated. |
| <CopyableCode code="description" /> | `string` | Optional. A descriptive comment. This field may be updated. The field may be displayed in chooser dialogs. |
| <CopyableCode code="etag" /> | `string` | Optional. A checksum, returned by the server, that can be sent on update requests to ensure the attestor has an up-to-date value before attempting to update it. See https://google.aip.dev/154. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Time when the attestor was last updated. |
| <CopyableCode code="userOwnedGrafeasNote" /> | `object` | An user owned Grafeas note references a Grafeas Attestation.Authority Note created by the user. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="attestorsId, projectsId" /> | Gets an attestor. Returns `NOT_FOUND` if the attestor does not exist. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists attestors. Returns `INVALID_ARGUMENT` if the project does not exist. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates an attestor, and returns a copy of the new attestor. Returns `NOT_FOUND` if the project does not exist, `INVALID_ARGUMENT` if the request is malformed, `ALREADY_EXISTS` if the attestor already exists. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="attestorsId, projectsId" /> | Deletes an attestor. Returns `NOT_FOUND` if the attestor does not exist. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="attestorsId, projectsId" /> | Updates an attestor. Returns `NOT_FOUND` if the attestor does not exist. |
| <CopyableCode code="validate_attestation_occurrence" /> | `EXEC` | <CopyableCode code="attestorsId, projectsId" /> | Returns whether the given `Attestation` for the given image URI was signed by the given `Attestor` |

## `SELECT` examples

Lists attestors. Returns `INVALID_ARGUMENT` if the project does not exist.

```sql
SELECT
name,
description,
etag,
updateTime,
userOwnedGrafeasNote
FROM google.binaryauthorization.attestors
WHERE projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>attestors</code> resource.

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
INSERT INTO google.binaryauthorization.attestors (
projectsId,
name,
description,
userOwnedGrafeasNote,
updateTime,
etag
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ description }}',
'{{ userOwnedGrafeasNote }}',
'{{ updateTime }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: userOwnedGrafeasNote
      value: '{{ userOwnedGrafeasNote }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: etag
      value: '{{ etag }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Replaces all fields in the specified <code>attestors</code> resource.

```sql
/*+ update */
REPLACE google.binaryauthorization.attestors
SET 
name = '{{ name }}',
description = '{{ description }}',
userOwnedGrafeasNote = '{{ userOwnedGrafeasNote }}',
updateTime = '{{ updateTime }}',
etag = '{{ etag }}'
WHERE 
attestorsId = '{{ attestorsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>attestors</code> resource.

```sql
/*+ delete */
DELETE FROM google.binaryauthorization.attestors
WHERE attestorsId = '{{ attestorsId }}'
AND projectsId = '{{ projectsId }}';
```
