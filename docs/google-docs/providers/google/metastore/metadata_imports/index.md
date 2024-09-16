---
title: metadata_imports
hide_title: false
hide_table_of_contents: false
keywords:
  - metadata_imports
  - metastore
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

Creates, updates, deletes, gets or lists a <code>metadata_imports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metadata_imports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.metastore.metadata_imports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The relative resource name of the metadata import, of the form:projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{metadata_import_id}. |
| <CopyableCode code="description" /> | `string` | The description of the metadata import. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time when the metadata import was started. |
| <CopyableCode code="databaseDump" /> | `object` | A specification of the location of and metadata about a database dump from a relational database management system. |
| <CopyableCode code="endTime" /> | `string` | Output only. The time when the metadata import finished. |
| <CopyableCode code="state" /> | `string` | Output only. The current state of the metadata import. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time when the metadata import was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, metadataImportsId, projectsId, servicesId" /> | Gets details of a single import. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Lists imports in a service. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, servicesId" /> | Creates a new MetadataImport in a given project and location. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, metadataImportsId, projectsId, servicesId" /> | Updates a single import. Only the description field of MetadataImport is supported to be updated. |

## `SELECT` examples

Lists imports in a service.

```sql
SELECT
name,
description,
createTime,
databaseDump,
endTime,
state,
updateTime
FROM google.metastore.metadata_imports
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>metadata_imports</code> resource.

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
INSERT INTO google.metastore.metadata_imports (
locationsId,
projectsId,
servicesId,
databaseDump,
name,
description,
createTime,
updateTime,
endTime,
state
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ servicesId }}',
'{{ databaseDump }}',
'{{ name }}',
'{{ description }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ endTime }}',
'{{ state }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: databaseDump
      value: '{{ databaseDump }}'
    - name: name
      value: '{{ name }}'
    - name: description
      value: '{{ description }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: endTime
      value: '{{ endTime }}'
    - name: state
      value: '{{ state }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>metadata_imports</code> resource.

```sql
/*+ update */
UPDATE google.metastore.metadata_imports
SET 
databaseDump = '{{ databaseDump }}',
name = '{{ name }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
endTime = '{{ endTime }}',
state = '{{ state }}'
WHERE 
locationsId = '{{ locationsId }}'
AND metadataImportsId = '{{ metadataImportsId }}'
AND projectsId = '{{ projectsId }}'
AND servicesId = '{{ servicesId }}';
```
