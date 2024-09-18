---
title: feature_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - feature_groups
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

Creates, updates, deletes, gets or lists a <code>feature_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feature_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.feature_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Name of the FeatureGroup. Format: `projects/{project}/locations/{location}/featureGroups/{featureGroup}` |
| <CopyableCode code="description" /> | `string` | Optional. Description of the FeatureGroup. |
| <CopyableCode code="bigQuery" /> | `object` | Input source type for BigQuery Tables and Views. |
| <CopyableCode code="createTime" /> | `string` | Output only. Timestamp when this FeatureGroup was created. |
| <CopyableCode code="etag" /> | `string` | Optional. Used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. |
| <CopyableCode code="labels" /> | `object` | Optional. The labels with user-defined metadata to organize your FeatureGroup. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See https://goo.gl/xmQnxf for more information on and examples of labels. No more than 64 user labels can be associated with one FeatureGroup(System labels are excluded)." System reserved label keys are prefixed with "aiplatform.googleapis.com/" and are immutable. |
| <CopyableCode code="updateTime" /> | `string` | Output only. Timestamp when this FeatureGroup was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="featureGroupsId, locationsId, projectsId" /> | Gets details of a single FeatureGroup. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists FeatureGroups in a given project and location. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new FeatureGroup in a given project and location. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="featureGroupsId, locationsId, projectsId" /> | Deletes a single FeatureGroup. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="featureGroupsId, locationsId, projectsId" /> | Updates the parameters of a single FeatureGroup. |

## `SELECT` examples

Lists FeatureGroups in a given project and location.

```sql
SELECT
name,
description,
bigQuery,
createTime,
etag,
labels,
updateTime
FROM google.aiplatform.feature_groups
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>feature_groups</code> resource.

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
INSERT INTO google.aiplatform.feature_groups (
locationsId,
projectsId,
bigQuery,
name,
description,
labels,
etag
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ bigQuery }}',
'{{ name }}',
'{{ description }}',
'{{ labels }}',
'{{ etag }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
bigQuery:
  dense: boolean
  bigQuerySource:
    inputUri: string
  staticDataSource: boolean
  timeSeries:
    timestampColumn: string
  entityIdColumns:
    - type: string
updateTime: string
name: string
description: string
labels: object
createTime: string
etag: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>feature_groups</code> resource.

```sql
/*+ update */
UPDATE google.aiplatform.feature_groups
SET 
bigQuery = '{{ bigQuery }}',
name = '{{ name }}',
description = '{{ description }}',
labels = '{{ labels }}',
etag = '{{ etag }}'
WHERE 
featureGroupsId = '{{ featureGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>feature_groups</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.feature_groups
WHERE featureGroupsId = '{{ featureGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
