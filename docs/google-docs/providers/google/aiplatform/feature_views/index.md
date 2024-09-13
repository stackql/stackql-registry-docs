
---
title: feature_views
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_views
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

Creates, updates, deletes or gets an <code>feature_view</code> resource or lists <code>feature_views</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feature_views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.feature_views" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the FeatureView. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}` |
| <CopyableCode code="bigQuerySource" /> | `object` |  |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this FeatureView was created. |
| <CopyableCode code="etag" /> | `string` | Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="featureRegistrySource" /> | `object` | A Feature Registry source for features that need to be synced to Online Store. |
| <CopyableCode code="indexConfig" /> | `object` | Configuration for vector indexing. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels with user-defined metadata to organize your FeatureViews. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureOnlineStore(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| <CopyableCode code="satisfiesPzi" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="satisfiesPzs" /> | `boolean` | Output only. Reserved for future use. |
| <CopyableCode code="syncConfig" /> | `object` | Configuration for Sync. Only one option is set. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this FeatureView was last updated. |
| <CopyableCode code="vertexRagSource" /> | `object` | A Vertex Rag source for features that need to be synced to Online Store. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="featureOnlineStoresId, featureViewsId, locationsId, projectsId" /> | Gets details of a single FeatureView. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="featureOnlineStoresId, locationsId, projectsId" /> | Lists FeatureViews in a given FeatureOnlineStore. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="featureOnlineStoresId, locationsId, projectsId" /> | Creates a new FeatureView in a given FeatureOnlineStore. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="featureOnlineStoresId, featureViewsId, locationsId, projectsId" /> | Deletes a single FeatureView. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="featureOnlineStoresId, featureViewsId, locationsId, projectsId" /> | Updates the parameters of a single FeatureView. |
| <CopyableCode code="search_nearest_entities" /> | `EXEC` | <CopyableCode code="featureOnlineStoresId, featureViewsId, locationsId, projectsId" /> | Search the nearest entities under a FeatureView. Search only works for indexable feature view; if a feature view isn't indexable, returns Invalid argument response. |
| <CopyableCode code="sync" /> | `EXEC` | <CopyableCode code="featureOnlineStoresId, featureViewsId, locationsId, projectsId" /> | Triggers on-demand sync for the FeatureView. |

## `SELECT` examples

Lists FeatureViews in a given FeatureOnlineStore.

```sql
SELECT
name,
bigQuerySource,
createTime,
etag,
featureRegistrySource,
indexConfig,
labels,
satisfiesPzi,
satisfiesPzs,
syncConfig,
updateTime,
vertexRagSource
FROM google.aiplatform.feature_views
WHERE featureOnlineStoresId = '{{ featureOnlineStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>feature_views</code> resource.

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
INSERT INTO google.aiplatform.feature_views (
featureOnlineStoresId,
locationsId,
projectsId,
satisfiesPzs,
createTime,
etag,
satisfiesPzi,
labels,
bigQuerySource,
name,
updateTime,
featureRegistrySource,
indexConfig,
vertexRagSource,
syncConfig
)
SELECT 
'{{ featureOnlineStoresId }}',
'{{ locationsId }}',
'{{ projectsId }}',
true|false,
'{{ createTime }}',
'{{ etag }}',
true|false,
'{{ labels }}',
'{{ bigQuerySource }}',
'{{ name }}',
'{{ updateTime }}',
'{{ featureRegistrySource }}',
'{{ indexConfig }}',
'{{ vertexRagSource }}',
'{{ syncConfig }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: satisfiesPzs
        value: '{{ satisfiesPzs }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: etag
        value: '{{ etag }}'
      - name: satisfiesPzi
        value: '{{ satisfiesPzi }}'
      - name: labels
        value: '{{ labels }}'
      - name: bigQuerySource
        value: '{{ bigQuerySource }}'
      - name: name
        value: '{{ name }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: featureRegistrySource
        value: '{{ featureRegistrySource }}'
      - name: indexConfig
        value: '{{ indexConfig }}'
      - name: vertexRagSource
        value: '{{ vertexRagSource }}'
      - name: syncConfig
        value: '{{ syncConfig }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a feature_view only if the necessary resources are available.

```sql
UPDATE google.aiplatform.feature_views
SET 
satisfiesPzs = true|false,
createTime = '{{ createTime }}',
etag = '{{ etag }}',
satisfiesPzi = true|false,
labels = '{{ labels }}',
bigQuerySource = '{{ bigQuerySource }}',
name = '{{ name }}',
updateTime = '{{ updateTime }}',
featureRegistrySource = '{{ featureRegistrySource }}',
indexConfig = '{{ indexConfig }}',
vertexRagSource = '{{ vertexRagSource }}',
syncConfig = '{{ syncConfig }}'
WHERE 
featureOnlineStoresId = '{{ featureOnlineStoresId }}'
AND featureViewsId = '{{ featureViewsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified feature_view resource.

```sql
DELETE FROM google.aiplatform.feature_views
WHERE featureOnlineStoresId = '{{ featureOnlineStoresId }}'
AND featureViewsId = '{{ featureViewsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
