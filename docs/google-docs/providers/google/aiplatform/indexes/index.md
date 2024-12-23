---
title: indexes
hide_title: false
hide_table_of_contents: false
keywords:
  - indexes
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

Creates, updates, deletes, gets or lists a <code>indexes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>indexes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.indexes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. The resource name of the Index. |
| <CopyableCode code="description" /> | `string` | The description of the Index. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this Index was created. |
| <CopyableCode code="deployedIndexes" /> | `array` | Output only. The pointers to DeployedIndexes created from this Index. An Index can be only deleted if all its DeployedIndexes had been undeployed first. |
| <CopyableCode code="displayName" /> | `string` | Required. The display name of the Index. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="etag" /> | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="indexStats" /> | `object` | Stats of the Index. |
| <CopyableCode code="indexUpdateMethod" /> | `string` | Immutable. The update method to use with this Index. If not set, BATCH_UPDATE will be used by default. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize your Indexes. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information and examples of labels. |
| <CopyableCode code="metadata" /> | `any` | An additional information about the Index; the schema of the metadata can be found in metadata_schema. |
| <CopyableCode code="metadataSchemaUri" /> | `string` | Immutable. Points to a YAML file stored on Google Cloud Storage describing additional information about the Index, that is specific to it. Unset if the Index does not have any additional information. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schemaObject). Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this Index was most recently updated. This also includes any update to the contents of the Index. Note that Operations working on this Index may have their Operations.metadata.generic_metadata.update_time a little after the value of this timestamp, yet that does not mean their results are not already reflected in the Index. Result of any successfully completed Operation on the Index is reflected in it. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="indexesId, locationsId, projectsId" /> | Gets an Index. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Indexes in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an Index. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="indexesId, locationsId, projectsId" /> | Deletes an Index. An Index can only be deleted when all its DeployedIndexes had been undeployed. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="indexesId, locationsId, projectsId" /> | Updates an Index. |
| <CopyableCode code="upsert_datapoints" /> | `EXEC` | <CopyableCode code="indexesId, locationsId, projectsId" /> | Add/update Datapoints into an Index. |

## `SELECT` examples

Lists Indexes in a Location.

```sql
SELECT
name,
description,
createTime,
deployedIndexes,
displayName,
encryptionSpec,
etag,
indexStats,
indexUpdateMethod,
labels,
metadata,
metadataSchemaUri,
satisfiesPzi,
satisfiesPzs,
updateTime
FROM google.aiplatform.indexes
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>indexes</code> resource.

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
INSERT INTO google.aiplatform.indexes (
locationsId,
projectsId,
metadataSchemaUri,
indexUpdateMethod,
labels,
etag,
encryptionSpec,
displayName,
description,
metadata
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ metadataSchemaUri }}',
'{{ indexUpdateMethod }}',
'{{ labels }}',
'{{ etag }}',
'{{ encryptionSpec }}',
'{{ displayName }}',
'{{ description }}',
'{{ metadata }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: metadataSchemaUri
      value: string
    - name: indexStats
      value:
        - name: sparseVectorsCount
          value: string
        - name: shardsCount
          value: integer
        - name: vectorsCount
          value: string
    - name: indexUpdateMethod
      value: string
    - name: labels
      value: object
    - name: createTime
      value: string
    - name: satisfiesPzi
      value: boolean
    - name: etag
      value: string
    - name: encryptionSpec
      value:
        - name: kmsKeyName
          value: string
    - name: updateTime
      value: string
    - name: deployedIndexes
      value:
        - - name: deployedIndexId
            value: string
          - name: displayName
            value: string
          - name: indexEndpoint
            value: string
    - name: displayName
      value: string
    - name: satisfiesPzs
      value: boolean
    - name: description
      value: string
    - name: metadata
      value: any
    - name: name
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>indexes</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.indexes
SET 
metadataSchemaUri = '{{ metadataSchemaUri }}',
indexUpdateMethod = '{{ indexUpdateMethod }}',
labels = '{{ labels }}',
etag = '{{ etag }}',
encryptionSpec = '{{ encryptionSpec }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
metadata = '{{ metadata }}'
WHERE 
indexesId = '{{ indexesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>indexes</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.indexes
WHERE indexesId = '{{ indexesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
