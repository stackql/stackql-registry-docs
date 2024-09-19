---
title: synonym_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - synonym_sets
  - contentwarehouse
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

Creates, updates, deletes, gets or lists a <code>synonym_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>synonym_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contentwarehouse.synonym_sets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the SynonymSet This is mandatory for google.api.resource. Format: projects/{project_number}/locations/{location}/synonymSets/{context}. |
| <CopyableCode code="context" /> | `string` | This is a freeform field. Example contexts can be "sales," "engineering," "real estate," "accounting," etc. The context can be supplied during search requests. |
| <CopyableCode code="synonyms" /> | `array` | List of Synonyms for the context. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, synonymSetsId" /> | Gets a SynonymSet for a particular context. Throws a NOT_FOUND exception if the Synonymset does not exist |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns all SynonymSets (for all contexts) for the specified location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a SynonymSet for a single context. Throws an ALREADY_EXISTS exception if a synonymset already exists for the context. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId, synonymSetsId" /> | Deletes a SynonymSet for a given context. Throws a NOT_FOUND exception if the SynonymSet is not found. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId, synonymSetsId" /> | Remove the existing SynonymSet for the context and replaces it with a new one. Throws a NOT_FOUND exception if the SynonymSet is not found. |

## `SELECT` examples

Returns all SynonymSets (for all contexts) for the specified location.

```sql
SELECT
name,
context,
synonyms
FROM google.contentwarehouse.synonym_sets
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>synonym_sets</code> resource.

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
INSERT INTO google.contentwarehouse.synonym_sets (
locationsId,
projectsId,
synonyms,
context,
name
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ synonyms }}',
'{{ context }}',
'{{ name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: synonyms
      value:
        - - name: words
            value:
              - string
    - name: context
      value: string
    - name: name
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>synonym_sets</code> resource.

```sql
/*+ update */
UPDATE google.contentwarehouse.synonym_sets
SET 
synonyms = '{{ synonyms }}',
context = '{{ context }}',
name = '{{ name }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND synonymSetsId = '{{ synonymSetsId }}';
```

## `DELETE` example

Deletes the specified <code>synonym_sets</code> resource.

```sql
/*+ delete */
DELETE FROM google.contentwarehouse.synonym_sets
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND synonymSetsId = '{{ synonymSetsId }}';
```
