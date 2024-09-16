---
title: entity_types
hide_title: false
hide_table_of_contents: false
keywords:
  - entity_types
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

Creates, updates, deletes, gets or lists a <code>entity_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entity_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.entity_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Name of the EntityType. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` The last part entity_type is assigned by the client. The entity_type can be up to 64 characters long and can consist only of ASCII Latin letters A-Z and a-z and underscore(_), and ASCII digits 0-9 starting with a letter. The value will be unique given a featurestore. |
| <CopyableCode code="description" /> | `string` | Optional. Description of the EntityType. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this EntityType was created. |
| <CopyableCode code="etag" /> | `string` | Optional. Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels with user-defined metadata to organize your EntityTypes. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one EntityType (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| <CopyableCode code="monitoringConfig" /> | `object` | Configuration of how features in Featurestore are monitored. |
| <CopyableCode code="offlineStorageTtlDays" /> | `integer` | Optional. Config for data retention policy in offline storage. TTL in days for feature values that will be stored in offline storage. The Feature Store offline storage periodically removes obsolete feature values older than `offline_storage_ttl_days` since the feature generation time. If unset (or explicitly set to 0), default to 4000 days TTL. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this EntityType was most recently updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="entityTypesId, featurestoresId, locationsId, projectsId" /> | Gets details of a single EntityType. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="featurestoresId, locationsId, projectsId" /> | Lists EntityTypes in a given Featurestore. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="featurestoresId, locationsId, projectsId" /> | Creates a new EntityType in a given Featurestore. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="entityTypesId, featurestoresId, locationsId, projectsId" /> | Deletes a single EntityType. The EntityType must not have any Features or `force` must be set to true for the request to succeed. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="entityTypesId, featurestoresId, locationsId, projectsId" /> | Updates the parameters of a single EntityType. |
| <CopyableCode code="export_feature_values" /> | `EXEC` | <CopyableCode code="entityTypesId, featurestoresId, locationsId, projectsId" /> | Exports Feature values from all the entities of a target EntityType. |
| <CopyableCode code="import_feature_values" /> | `EXEC` | <CopyableCode code="entityTypesId, featurestoresId, locationsId, projectsId" /> | Imports Feature values into the Featurestore from a source storage. The progress of the import is tracked by the returned operation. The imported features are guaranteed to be visible to subsequent read operations after the operation is marked as successfully done. If an import operation fails, the Feature values returned from reads and exports may be inconsistent. If consistency is required, the caller must retry the same import request again and wait till the new operation returned is marked as successfully done. There are also scenarios where the caller can cause inconsistency. - Source data for import contains multiple distinct Feature values for the same entity ID and timestamp. - Source is modified during an import. This includes adding, updating, or removing source data and/or metadata. Examples of updating metadata include but are not limited to changing storage location, storage class, or retention policy. - Online serving cluster is under-provisioned. |
| <CopyableCode code="read_feature_values" /> | `EXEC` | <CopyableCode code="entityTypesId, featurestoresId, locationsId, projectsId" /> | Reads Feature values of a specific entity of an EntityType. For reading feature values of multiple entities of an EntityType, please use StreamingReadFeatureValues. |
| <CopyableCode code="streaming_read_feature_values" /> | `EXEC` | <CopyableCode code="entityTypesId, featurestoresId, locationsId, projectsId" /> | Reads Feature values for multiple entities. Depending on their size, data for different entities may be broken up across multiple responses. |
| <CopyableCode code="write_feature_values" /> | `EXEC` | <CopyableCode code="entityTypesId, featurestoresId, locationsId, projectsId" /> | Writes Feature values of one or more entities of an EntityType. The Feature values are merged into existing entities if any. The Feature values to be written must have timestamp within the online storage retention. |

## `SELECT` examples

Lists EntityTypes in a given Featurestore.

```sql
SELECT
name,
description,
createTime,
etag,
labels,
monitoringConfig,
offlineStorageTtlDays,
satisfiesPzi,
satisfiesPzs,
updateTime
FROM google.aiplatform.entity_types
WHERE featurestoresId = '{{ featurestoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>entity_types</code> resource.

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
INSERT INTO google.aiplatform.entity_types (
featurestoresId,
locationsId,
projectsId,
etag,
name,
offlineStorageTtlDays,
description,
monitoringConfig,
labels
)
SELECT 
'{{ featurestoresId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ etag }}',
'{{ name }}',
'{{ offlineStorageTtlDays }}',
'{{ description }}',
'{{ monitoringConfig }}',
'{{ labels }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: etag
      value: '{{ etag }}'
    - name: name
      value: '{{ name }}'
    - name: offlineStorageTtlDays
      value: '{{ offlineStorageTtlDays }}'
    - name: description
      value: '{{ description }}'
    - name: monitoringConfig
      value:
        - name: snapshotAnalysis
          value:
            - name: stalenessDays
              value: '{{ stalenessDays }}'
            - name: disabled
              value: '{{ disabled }}'
            - name: monitoringIntervalDays
              value: '{{ monitoringIntervalDays }}'
        - name: categoricalThresholdConfig
          value:
            - name: value
              value: '{{ value }}'
        - name: importFeaturesAnalysis
          value:
            - name: anomalyDetectionBaseline
              value: '{{ anomalyDetectionBaseline }}'
            - name: state
              value: '{{ state }}'
    - name: labels
      value: '{{ labels }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>entity_types</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.entity_types
SET 
etag = '{{ etag }}',
name = '{{ name }}',
offlineStorageTtlDays = '{{ offlineStorageTtlDays }}',
description = '{{ description }}',
monitoringConfig = '{{ monitoringConfig }}',
labels = '{{ labels }}'
WHERE 
entityTypesId = '{{ entityTypesId }}'
AND featurestoresId = '{{ featurestoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>entity_types</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.entity_types
WHERE entityTypesId = '{{ entityTypesId }}'
AND featurestoresId = '{{ featurestoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
