---
title: image_imports
hide_title: false
hide_table_of_contents: false
keywords:
  - image_imports
  - vmmigration
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

Creates, updates, deletes, gets or lists a <code>image_imports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_imports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.vmmigration.image_imports" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource path of the ImageImport. |
| <CopyableCode code="cloudStorageUri" /> | `string` | Immutable. The path to the Cloud Storage file from which the image should be imported. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the image import was created. |
| <CopyableCode code="diskImageTargetDefaults" /> | `object` | The target details of the image resource that will be created by the import job. |
| <CopyableCode code="encryption" /> | `object` | Encryption message describes the details of the applied encryption. |
| <CopyableCode code="machineImageTargetDefaults" /> | `object` | The target details of the machine image resource that will be created by the image import job. |
| <CopyableCode code="recentImageImportJobs" /> | `array` | Output only. The result of the most recent runs for this ImageImport. All jobs for this ImageImport can be listed via ListImageImportJobs. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="imageImportsId, locationsId, projectsId" /> | Gets details of a single ImageImport. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists ImageImports in a given project. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new ImageImport in a given project. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="imageImportsId, locationsId, projectsId" /> | Deletes a single ImageImport. |

## `SELECT` examples

Lists ImageImports in a given project.

```sql
SELECT
name,
cloudStorageUri,
createTime,
diskImageTargetDefaults,
encryption,
machineImageTargetDefaults,
recentImageImportJobs
FROM google.vmmigration.image_imports
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>image_imports</code> resource.

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
INSERT INTO google.vmmigration.image_imports (
locationsId,
projectsId,
cloudStorageUri,
diskImageTargetDefaults,
machineImageTargetDefaults,
name,
createTime,
recentImageImportJobs,
encryption
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ cloudStorageUri }}',
'{{ diskImageTargetDefaults }}',
'{{ machineImageTargetDefaults }}',
'{{ name }}',
'{{ createTime }}',
'{{ recentImageImportJobs }}',
'{{ encryption }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: cloudStorageUri
        value: '{{ cloudStorageUri }}'
      - name: diskImageTargetDefaults
        value: '{{ diskImageTargetDefaults }}'
      - name: machineImageTargetDefaults
        value: '{{ machineImageTargetDefaults }}'
      - name: name
        value: '{{ name }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: recentImageImportJobs
        value: '{{ recentImageImportJobs }}'
      - name: encryption
        value: '{{ encryption }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>image_imports</code> resource.

```sql
/*+ delete */
DELETE FROM google.vmmigration.image_imports
WHERE imageImportsId = '{{ imageImportsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
