---
title: tags
hide_title: false
hide_table_of_contents: false
keywords:
  - tags
  - artifactregistry
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

Creates, updates, deletes, gets or lists a <code>tags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.artifactregistry.tags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the tag, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/tags/tag1". If the package part contains slashes, the slashes are escaped. The tag part can only have characters in [a-zA-Z0-9\-._~:@], anything else must be URL encoded. |
| <CopyableCode code="version" /> | `string` | The name of the version the tag refers to, for example: "projects/p1/locations/us-central1/repositories/repo1/packages/pkg1/versions/sha256:5243811" If the package or version ID parts contain slashes, the slashes are escaped. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId, tagsId" /> | Gets a tag. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId" /> | Lists tags. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId" /> | Creates a tag. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId, tagsId" /> | Deletes a tag. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, packagesId, projectsId, repositoriesId, tagsId" /> | Updates a tag. |

## `SELECT` examples

Lists tags.

```sql
SELECT
name,
version
FROM google.artifactregistry.tags
WHERE locationsId = '{{ locationsId }}'
AND packagesId = '{{ packagesId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tags</code> resource.

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
INSERT INTO google.artifactregistry.tags (
locationsId,
packagesId,
projectsId,
repositoriesId,
name,
version
)
SELECT 
'{{ locationsId }}',
'{{ packagesId }}',
'{{ projectsId }}',
'{{ repositoriesId }}',
'{{ name }}',
'{{ version }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: version
      value: '{{ version }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>tags</code> resource.

```sql
/*+ update */
UPDATE google.artifactregistry.tags
SET 
name = '{{ name }}',
version = '{{ version }}'
WHERE 
locationsId = '{{ locationsId }}'
AND packagesId = '{{ packagesId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'
AND tagsId = '{{ tagsId }}';
```

## `DELETE` example

Deletes the specified <code>tags</code> resource.

```sql
/*+ delete */
DELETE FROM google.artifactregistry.tags
WHERE locationsId = '{{ locationsId }}'
AND packagesId = '{{ packagesId }}'
AND projectsId = '{{ projectsId }}'
AND repositoriesId = '{{ repositoriesId }}'
AND tagsId = '{{ tagsId }}';
```
