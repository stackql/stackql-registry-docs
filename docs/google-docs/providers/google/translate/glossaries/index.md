---
title: glossaries
hide_title: false
hide_table_of_contents: false
keywords:
  - glossaries
  - translate
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

Creates, updates, deletes, gets or lists a <code>glossaries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>glossaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.translate.glossaries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The resource name of the glossary. Glossary names have the form `projects/{project-number-or-id}/locations/{location-id}/glossaries/{glossary-id}`. |
| <CopyableCode code="displayName" /> | `string` | Optional. The display name of the glossary. |
| <CopyableCode code="endTime" /> | `string` | Output only. When the glossary creation was finished. |
| <CopyableCode code="entryCount" /> | `integer` | Output only. The number of entries defined in the glossary. |
| <CopyableCode code="inputConfig" /> | `object` | Input configuration for glossaries. |
| <CopyableCode code="languageCodesSet" /> | `object` | Used with equivalent term set glossaries. |
| <CopyableCode code="languagePair" /> | `object` | Used with unidirectional glossaries. |
| <CopyableCode code="submitTime" /> | `string` | Output only. When CreateGlossary was called. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_glossaries_get" /> | `SELECT` | <CopyableCode code="glossariesId, locationsId, projectsId" /> | Gets a glossary. Returns NOT_FOUND, if the glossary doesn't exist. |
| <CopyableCode code="projects_locations_glossaries_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists glossaries in a project. Returns NOT_FOUND, if the project doesn't exist. |
| <CopyableCode code="projects_locations_glossaries_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a glossary and returns the long-running operation. Returns NOT_FOUND, if the project doesn't exist. |
| <CopyableCode code="projects_locations_glossaries_delete" /> | `DELETE` | <CopyableCode code="glossariesId, locationsId, projectsId" /> | Deletes a glossary, or cancels glossary construction if the glossary isn't created yet. Returns NOT_FOUND, if the glossary doesn't exist. |
| <CopyableCode code="projects_locations_glossaries_patch" /> | `UPDATE` | <CopyableCode code="glossariesId, locationsId, projectsId" /> | Updates a glossary. A LRO is used since the update can be async if the glossary's entry file is updated. |

## `SELECT` examples

Lists glossaries in a project. Returns NOT_FOUND, if the project doesn't exist.

```sql
SELECT
name,
displayName,
endTime,
entryCount,
inputConfig,
languageCodesSet,
languagePair,
submitTime
FROM google.translate.glossaries
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>glossaries</code> resource.

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
INSERT INTO google.translate.glossaries (
locationsId,
projectsId,
name,
languagePair,
languageCodesSet,
inputConfig,
displayName
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ languagePair }}',
'{{ languageCodesSet }}',
'{{ inputConfig }}',
'{{ displayName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
languagePair:
  sourceLanguageCode: string
  targetLanguageCode: string
languageCodesSet:
  languageCodes:
    - type: string
inputConfig:
  gcsSource:
    inputUri: string
entryCount: integer
submitTime: string
endTime: string
displayName: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>glossaries</code> resource.

```sql
/*+ update */
UPDATE google.translate.glossaries
SET 
name = '{{ name }}',
languagePair = '{{ languagePair }}',
languageCodesSet = '{{ languageCodesSet }}',
inputConfig = '{{ inputConfig }}',
displayName = '{{ displayName }}'
WHERE 
glossariesId = '{{ glossariesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>glossaries</code> resource.

```sql
/*+ delete */
DELETE FROM google.translate.glossaries
WHERE glossariesId = '{{ glossariesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
