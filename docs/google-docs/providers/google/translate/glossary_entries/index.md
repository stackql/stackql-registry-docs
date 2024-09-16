---
title: glossary_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - glossary_entries
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

Creates, updates, deletes, gets or lists a <code>glossary_entries</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>glossary_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.translate.glossary_entries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. The resource name of the entry. Format: `projects/*/locations/*/glossaries/*/glossaryEntries/*` |
| <CopyableCode code="description" /> | `string` | Describes the glossary entry. |
| <CopyableCode code="termsPair" /> | `object` | Represents a single entry for an unidirectional glossary. |
| <CopyableCode code="termsSet" /> | `object` | Represents a single entry for an equivalent term set glossary. This is used for equivalent term sets where each term can be replaced by the other terms in the set. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_glossaries_glossary_entries_get" /> | `SELECT` | <CopyableCode code="glossariesId, glossaryEntriesId, locationsId, projectsId" /> | Gets a single glossary entry by the given id. |
| <CopyableCode code="projects_locations_glossaries_glossary_entries_list" /> | `SELECT` | <CopyableCode code="glossariesId, locationsId, projectsId" /> | List the entries for the glossary. |
| <CopyableCode code="projects_locations_glossaries_glossary_entries_create" /> | `INSERT` | <CopyableCode code="glossariesId, locationsId, projectsId" /> | Creates a glossary entry. |
| <CopyableCode code="projects_locations_glossaries_glossary_entries_delete" /> | `DELETE` | <CopyableCode code="glossariesId, glossaryEntriesId, locationsId, projectsId" /> | Deletes a single entry from the glossary |
| <CopyableCode code="projects_locations_glossaries_glossary_entries_patch" /> | `UPDATE` | <CopyableCode code="glossariesId, glossaryEntriesId, locationsId, projectsId" /> | Updates a glossary entry. |

## `SELECT` examples

List the entries for the glossary.

```sql
SELECT
name,
description,
termsPair,
termsSet
FROM google.translate.glossary_entries
WHERE glossariesId = '{{ glossariesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>glossary_entries</code> resource.

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
INSERT INTO google.translate.glossary_entries (
glossariesId,
locationsId,
projectsId,
name,
termsPair,
termsSet,
description
)
SELECT 
'{{ glossariesId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ termsPair }}',
'{{ termsSet }}',
'{{ description }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: '{{ name }}'
    - name: termsPair
      value:
        - name: sourceTerm
          value:
            - name: languageCode
              value: '{{ languageCode }}'
            - name: text
              value: '{{ text }}'
    - name: termsSet
      value:
        - name: terms
          value:
            - name: $ref
              value: '{{ $ref }}'
    - name: description
      value: '{{ description }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>glossary_entries</code> resource.

```sql
/*+ update */
UPDATE google.translate.glossary_entries
SET 
name = '{{ name }}',
termsPair = '{{ termsPair }}',
termsSet = '{{ termsSet }}',
description = '{{ description }}'
WHERE 
glossariesId = '{{ glossariesId }}'
AND glossaryEntriesId = '{{ glossaryEntriesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>glossary_entries</code> resource.

```sql
/*+ delete */
DELETE FROM google.translate.glossary_entries
WHERE glossariesId = '{{ glossariesId }}'
AND glossaryEntriesId = '{{ glossaryEntriesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
