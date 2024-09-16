---
title: contexts
hide_title: false
hide_table_of_contents: false
keywords:
  - contexts
  - aiplatform
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

Creates, updates, deletes, gets or lists a <code>contexts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contexts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.contexts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the Context. |
| <CopyableCode code="description" /> | `string` | Description of the Context |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this Context was created. |
| <CopyableCode code="displayName" /> | `string` | User provided display name of the Context. May be up to 128 Unicode characters. |
| <CopyableCode code="etag" /> | `string` | An eTag used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize your Contexts. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Context (System labels are excluded). |
| <CopyableCode code="metadata" /> | `object` | Properties of the Context. Top level metadata keys' heading and trailing spaces will be trimmed. The size of this field should not exceed 200KB. |
| <CopyableCode code="parentContexts" /> | `array` | Output only. A list of resource names of Contexts that are parents of this Context. A Context may have at most 10 parent_contexts. |
| <CopyableCode code="schemaTitle" /> | `string` | The title of the schema describing the metadata. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. |
| <CopyableCode code="schemaVersion" /> | `string` | The version of the schema in schema_name to use. Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this Context was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="contextsId, locationsId, metadataStoresId, projectsId" /> | Retrieves a specific Context. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Lists Contexts on the MetadataStore. |
| <CopyableCode code="query_context_lineage_subgraph" /> | `SELECT` | <CopyableCode code="contextsId, locationsId, metadataStoresId, projectsId" /> | Retrieves Artifacts and Executions within the specified Context, connected by Event edges and returned as a LineageSubgraph. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Creates a Context associated with a MetadataStore. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="contextsId, locationsId, metadataStoresId, projectsId" /> | Deletes a stored Context. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="contextsId, locationsId, metadataStoresId, projectsId" /> | Updates a stored Context. |
| <CopyableCode code="purge" /> | `EXEC` | <CopyableCode code="locationsId, metadataStoresId, projectsId" /> | Purges Contexts. |

## `SELECT` examples

Lists Contexts on the MetadataStore.

```sql
SELECT
name,
description,
createTime,
displayName,
etag,
labels,
metadata,
parentContexts,
schemaTitle,
schemaVersion,
updateTime
FROM google.aiplatform.contexts
WHERE locationsId = '{{ locationsId }}'
AND metadataStoresId = '{{ metadataStoresId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>contexts</code> resource.

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
INSERT INTO google.aiplatform.contexts (
locationsId,
metadataStoresId,
projectsId,
description,
updateTime,
displayName,
parentContexts,
createTime,
labels,
name,
schemaTitle,
metadata,
etag,
schemaVersion
)
SELECT 
'{{ locationsId }}',
'{{ metadataStoresId }}',
'{{ projectsId }}',
'{{ description }}',
'{{ updateTime }}',
'{{ displayName }}',
'{{ parentContexts }}',
'{{ createTime }}',
'{{ labels }}',
'{{ name }}',
'{{ schemaTitle }}',
'{{ metadata }}',
'{{ etag }}',
'{{ schemaVersion }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: description
      value: '{{ description }}'
    - name: updateTime
      value: '{{ updateTime }}'
    - name: displayName
      value: '{{ displayName }}'
    - name: parentContexts
      value: '{{ parentContexts }}'
    - name: createTime
      value: '{{ createTime }}'
    - name: labels
      value: '{{ labels }}'
    - name: name
      value: '{{ name }}'
    - name: schemaTitle
      value: '{{ schemaTitle }}'
    - name: metadata
      value: '{{ metadata }}'
    - name: etag
      value: '{{ etag }}'
    - name: schemaVersion
      value: '{{ schemaVersion }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>contexts</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.contexts
SET 
description = '{{ description }}',
updateTime = '{{ updateTime }}',
displayName = '{{ displayName }}',
parentContexts = '{{ parentContexts }}',
createTime = '{{ createTime }}',
labels = '{{ labels }}',
name = '{{ name }}',
schemaTitle = '{{ schemaTitle }}',
metadata = '{{ metadata }}',
etag = '{{ etag }}',
schemaVersion = '{{ schemaVersion }}'
WHERE 
contextsId = '{{ contextsId }}'
AND locationsId = '{{ locationsId }}'
AND metadataStoresId = '{{ metadataStoresId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>contexts</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.contexts
WHERE contextsId = '{{ contextsId }}'
AND locationsId = '{{ locationsId }}'
AND metadataStoresId = '{{ metadataStoresId }}'
AND projectsId = '{{ projectsId }}';
```
