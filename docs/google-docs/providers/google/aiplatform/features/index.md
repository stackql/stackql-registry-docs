
---
title: features
hide_title: false
hide_table_of_contents: false
keywords:
  - features
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

Creates, updates, deletes or gets an <code>feature</code> resource or lists <code>features</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>features</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.features" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Name of the Feature. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}` `projects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}` The last part feature is assigned by the client. The feature can be up to 64 characters long and can consist only of ASCII Latin letters A-Z and a-z, underscore(_), and ASCII digits 0-9 starting with a letter. The value will be unique given an entity type. |
| <CopyableCode code="description" /> | `string` | Description of the Feature. |
| <CopyableCode code="createTime" /> | `string` | Output only. Only applicable for Vertex AI Feature Store (Legacy). Timestamp when this EntityType was created. |
| <CopyableCode code="disableMonitoring" /> | `boolean` | Optional. Only applicable for Vertex AI Feature Store (Legacy). If not set, use the monitoring_config defined for the EntityType this Feature belongs to. Only Features with type (Feature.ValueType) BOOL, STRING, DOUBLE or INT64 can enable monitoring. If set to true, all types of data monitoring are disabled despite the config on EntityType. |
| <CopyableCode code="etag" /> | `string` | Used to perform a consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels with user-defined metadata to organize your Features. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one Feature (System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| <CopyableCode code="monitoringStatsAnomalies" /> | `array` | Output only. Only applicable for Vertex AI Feature Store (Legacy). The list of historical stats and anomalies with specified objectives. |
| <CopyableCode code="pointOfContact" /> | `string` | Entity responsible for maintaining this feature. Can be comma separated list of email addresses or URIs. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Only applicable for Vertex AI Feature Store (Legacy). Timestamp when this EntityType was most recently updated. |
| <CopyableCode code="valueType" /> | `string` | Immutable. Only applicable for Vertex AI Feature Store (Legacy). Type of Feature value. |
| <CopyableCode code="versionColumnName" /> | `string` | Only applicable for Vertex AI Feature Store. The name of the BigQuery Table/View column hosting data for this version. If no value is provided, will use feature_id. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="featureGroupsId, featuresId, locationsId, projectsId" /> | Gets details of a single Feature. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="featureGroupsId, locationsId, projectsId" /> | Lists Features in a given FeatureGroup. |
| <CopyableCode code="batch_create" /> | `INSERT` | <CopyableCode code="entityTypesId, featurestoresId, locationsId, projectsId" /> | Creates a batch of Features in a given EntityType. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="featureGroupsId, locationsId, projectsId" /> | Creates a new Feature in a given FeatureGroup. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="featureGroupsId, featuresId, locationsId, projectsId" /> | Deletes a single Feature. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="featureGroupsId, featuresId, locationsId, projectsId" /> | Updates the parameters of a single Feature. |

## `SELECT` examples

Lists Features in a given FeatureGroup.

```sql
SELECT
name,
description,
createTime,
disableMonitoring,
etag,
labels,
monitoringStatsAnomalies,
pointOfContact,
updateTime,
valueType,
versionColumnName
FROM google.aiplatform.features
WHERE featureGroupsId = '{{ featureGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>features</code> resource.

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
INSERT INTO google.aiplatform.features (
featureGroupsId,
locationsId,
projectsId,
labels,
createTime,
versionColumnName,
valueType,
disableMonitoring,
etag,
description,
updateTime,
name,
monitoringStatsAnomalies,
pointOfContact
)
SELECT 
'{{ featureGroupsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ labels }}',
'{{ createTime }}',
'{{ versionColumnName }}',
'{{ valueType }}',
true|false,
'{{ etag }}',
'{{ description }}',
'{{ updateTime }}',
'{{ name }}',
'{{ monitoringStatsAnomalies }}',
'{{ pointOfContact }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: labels
        value: '{{ labels }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: versionColumnName
        value: '{{ versionColumnName }}'
      - name: valueType
        value: '{{ valueType }}'
      - name: disableMonitoring
        value: '{{ disableMonitoring }}'
      - name: etag
        value: '{{ etag }}'
      - name: description
        value: '{{ description }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: name
        value: '{{ name }}'
      - name: monitoringStatsAnomalies
        value: '{{ monitoringStatsAnomalies }}'
      - name: pointOfContact
        value: '{{ pointOfContact }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a feature only if the necessary resources are available.

```sql
UPDATE google.aiplatform.features
SET 
labels = '{{ labels }}',
createTime = '{{ createTime }}',
versionColumnName = '{{ versionColumnName }}',
valueType = '{{ valueType }}',
disableMonitoring = true|false,
etag = '{{ etag }}',
description = '{{ description }}',
updateTime = '{{ updateTime }}',
name = '{{ name }}',
monitoringStatsAnomalies = '{{ monitoringStatsAnomalies }}',
pointOfContact = '{{ pointOfContact }}'
WHERE 
featureGroupsId = '{{ featureGroupsId }}'
AND featuresId = '{{ featuresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified feature resource.

```sql
DELETE FROM google.aiplatform.features
WHERE featureGroupsId = '{{ featureGroupsId }}'
AND featuresId = '{{ featuresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
