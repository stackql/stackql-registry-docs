---
title: datasets
hide_title: false
hide_table_of_contents: false
keywords:
  - datasets
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

Creates, updates, deletes or gets an <code>dataset</code> resource or lists <code>datasets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datasets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.datasets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Identifier. The resource name of the Dataset. |
| <CopyableCode code="description" /> | `string` | The description of the Dataset. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this Dataset was created. |
| <CopyableCode code="dataItemCount" /> | `string` | Output only. The number of DataItems in this Dataset. Only apply for non-structured Dataset. |
| <CopyableCode code="displayName" /> | `string` | Required. The user-defined name of the Dataset. The name can be up to 128 characters long and can consist of any UTF-8 characters. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="etag" /> | `string` | Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | The labels with user-defined metadata to organize your Datasets. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Dataset (System labels are excluded). See https://goo.gl/xmQnxf for more information and examples of labels. System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. Following system labels exist for each Dataset: * "aiplatform.googleapis.com/dataset_metadata_schema": output only, its value is the metadata_schema's title. |
| <CopyableCode code="metadata" /> | `any` | Required. Additional information about the Dataset. |
| <CopyableCode code="metadataArtifact" /> | `string` | Output only. The resource name of the Artifact that was created in MetadataStore when creating the Dataset. The Artifact resource name pattern is `projects/{project}/locations/{location}/metadataStores/{metadata_store}/artifacts/{artifact}`. |
| <CopyableCode code="metadataSchemaUri" /> | `string` | Required. Points to a YAML file stored on Google Cloud Storage describing additional information about the Dataset. The schema is defined as an OpenAPI 3.0.2 Schema Object. The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/metadata/. |
| <CopyableCode code="modelReference" /> | `string` | Optional. Reference to the public base model last used by the dataset. Only set for prompt datasets. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="savedQueries" /> | `array` | All SavedQueries belong to the Dataset will be returned in List/Get Dataset response. The annotation_specs field will not be populated except for UI cases which will only use annotation_spec_count. In CreateDataset request, a SavedQuery is created together if this field is set, up to one SavedQuery can be set in CreateDatasetRequest. The SavedQuery should not contain any AnnotationSpec. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this Dataset was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="datasetsId" /> | Gets a Dataset. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="" /> | Lists Datasets in a Location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="" /> | Creates a Dataset. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="datasetsId" /> | Deletes a Dataset. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="datasetsId" /> | Updates a Dataset. |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Exports data from a Dataset. |
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Imports data into a Dataset. |
| <CopyableCode code="search_data_items" /> | `EXEC` | <CopyableCode code="datasetsId, locationsId, projectsId" /> | Searches DataItems in a Dataset. |

## `SELECT` examples

Lists Datasets in a Location.

```sql
SELECT
name,
description,
createTime,
dataItemCount,
displayName,
encryptionSpec,
etag,
labels,
metadata,
metadataArtifact,
metadataSchemaUri,
modelReference,
satisfiesPzi,
satisfiesPzs,
savedQueries,
updateTime
FROM google.aiplatform.datasets
WHERE  = '{{  }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>datasets</code> resource.

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
INSERT INTO google.aiplatform.datasets (
,
metadataSchemaUri,
updateTime,
satisfiesPzi,
metadataArtifact,
description,
createTime,
satisfiesPzs,
metadata,
etag,
displayName,
dataItemCount,
name,
labels,
modelReference,
encryptionSpec,
savedQueries
)
SELECT 
'{{  }}',
'{{ metadataSchemaUri }}',
'{{ updateTime }}',
true|false,
'{{ metadataArtifact }}',
'{{ description }}',
'{{ createTime }}',
true|false,
'{{ metadata }}',
'{{ etag }}',
'{{ displayName }}',
'{{ dataItemCount }}',
'{{ name }}',
'{{ labels }}',
'{{ modelReference }}',
'{{ encryptionSpec }}',
'{{ savedQueries }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: metadataSchemaUri
        value: '{{ metadataSchemaUri }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: satisfiesPzi
        value: '{{ satisfiesPzi }}'
      - name: metadataArtifact
        value: '{{ metadataArtifact }}'
      - name: description
        value: '{{ description }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: satisfiesPzs
        value: '{{ satisfiesPzs }}'
      - name: metadata
        value: '{{ metadata }}'
      - name: etag
        value: '{{ etag }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: dataItemCount
        value: '{{ dataItemCount }}'
      - name: name
        value: '{{ name }}'
      - name: labels
        value: '{{ labels }}'
      - name: modelReference
        value: '{{ modelReference }}'
      - name: encryptionSpec
        value: '{{ encryptionSpec }}'
      - name: savedQueries
        value: '{{ savedQueries }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a dataset only if the necessary resources are available.

```sql
UPDATE google.aiplatform.datasets
SET 
metadataSchemaUri = '{{ metadataSchemaUri }}',
updateTime = '{{ updateTime }}',
satisfiesPzi = true|false,
metadataArtifact = '{{ metadataArtifact }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
satisfiesPzs = true|false,
metadata = '{{ metadata }}',
etag = '{{ etag }}',
displayName = '{{ displayName }}',
dataItemCount = '{{ dataItemCount }}',
name = '{{ name }}',
labels = '{{ labels }}',
modelReference = '{{ modelReference }}',
encryptionSpec = '{{ encryptionSpec }}',
savedQueries = '{{ savedQueries }}'
WHERE 
datasetsId = '{{ datasetsId }}';
```

## `DELETE` example

Deletes the specified dataset resource.

```sql
DELETE FROM google.aiplatform.datasets
WHERE datasetsId = '{{ datasetsId }}';
```
