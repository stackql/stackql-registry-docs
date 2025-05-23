---
title: featurestores
hide_title: false
hide_table_of_contents: false
keywords:
  - featurestores
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

Creates, updates, deletes, gets or lists a <code>featurestores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>featurestores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.featurestores" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the Featurestore. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}` |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this Featurestore was created. |
| <CopyableCode code="encryptionSpec" /> | `object` | Represents a customer-managed encryption key spec that can be applied to a top-level resource. |
| <CopyableCode code="etag" /> | `string` | Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels with user-defined metadata to organize your Featurestore. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one Featurestore(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| <CopyableCode code="onlineServingConfig" /> | `object` | OnlineServingConfig specifies the details for provisioning online serving resources. |
| <CopyableCode code="onlineStorageTtlDays" /> | `integer` | Optional. TTL in days for feature values that will be stored in online serving storage. The Feature Store online storage periodically removes obsolete feature values older than `online_storage_ttl_days` since the feature generation time. Note that `online_storage_ttl_days` should be less than or equal to `offline_storage_ttl_days` for each EntityType under a featurestore. If not set, default to 4000 days |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="state" /> | `string` | Output only. State of the featurestore. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this Featurestore was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="featurestoresId, locationsId, projectsId" /> | Gets details of a single Featurestore. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists Featurestores in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new Featurestore in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="featurestoresId, locationsId, projectsId" /> | Deletes a single Featurestore. The Featurestore must not contain any EntityTypes or `force` must be set to true for the request to succeed. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="featurestoresId, locationsId, projectsId" /> | Updates the parameters of a single Featurestore. |
| <CopyableCode code="batch_read_feature_values" /> | `EXEC` | <CopyableCode code="featurestoresId, locationsId, projectsId" /> | Batch reads Feature values from a Featurestore. This API enables batch reading Feature values, where each read instance in the batch may read Feature values of entities from one or more EntityTypes. Point-in-time correctness is guaranteed for Feature values of each read instance as of each instance's read timestamp. |
| <CopyableCode code="search_features" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Searches Features matching a query in a given project. |

## `SELECT` examples

Lists Featurestores in a given project and location.

```sql
SELECT
name,
createTime,
encryptionSpec,
etag,
labels,
onlineServingConfig,
onlineStorageTtlDays,
satisfiesPzi,
satisfiesPzs,
state,
updateTime
FROM google.aiplatform.featurestores
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>featurestores</code> resource.

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
INSERT INTO google.aiplatform.featurestores (
locationsId,
projectsId,
onlineStorageTtlDays,
labels,
encryptionSpec,
etag,
onlineServingConfig
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ onlineStorageTtlDays }}',
'{{ labels }}',
'{{ encryptionSpec }}',
'{{ etag }}',
'{{ onlineServingConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: onlineStorageTtlDays
      value: integer
    - name: updateTime
      value: string
    - name: satisfiesPzs
      value: boolean
    - name: labels
      value: object
    - name: encryptionSpec
      value:
        - name: kmsKeyName
          value: string
    - name: etag
      value: string
    - name: satisfiesPzi
      value: boolean
    - name: state
      value: string
    - name: name
      value: string
    - name: onlineServingConfig
      value:
        - name: fixedNodeCount
          value: integer
        - name: scaling
          value:
            - name: cpuUtilizationTarget
              value: integer
            - name: minNodeCount
              value: integer
            - name: maxNodeCount
              value: integer
    - name: createTime
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>featurestores</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.featurestores
SET 
onlineStorageTtlDays = '{{ onlineStorageTtlDays }}',
labels = '{{ labels }}',
encryptionSpec = '{{ encryptionSpec }}',
etag = '{{ etag }}',
onlineServingConfig = '{{ onlineServingConfig }}'
WHERE 
featurestoresId = '{{ featurestoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>featurestores</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.featurestores
WHERE featurestoresId = '{{ featurestoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
