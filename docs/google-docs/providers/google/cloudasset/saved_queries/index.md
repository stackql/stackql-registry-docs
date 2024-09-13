
---
title: saved_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - saved_queries
  - cloudasset
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

Creates, updates, deletes or gets an <code>saved_query</code> resource or lists <code>saved_queries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>saved_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudasset.saved_queries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the saved query. The format must be: * projects/project_number/savedQueries/saved_query_id * folders/folder_number/savedQueries/saved_query_id * organizations/organization_number/savedQueries/saved_query_id |
| <CopyableCode code="description" /> | `string` | The description of this saved query. This value should be fewer than 255 characters. |
| <CopyableCode code="content" /> | `object` | The query content. |
| <CopyableCode code="createTime" /> | `string` | Output only. The create time of this saved query. |
| <CopyableCode code="creator" /> | `string` | Output only. The account's email address who has created this saved query. |
| <CopyableCode code="labels" /> | `object` | Labels applied on the resource. This value should not contain more than 10 entries. The key and value of each entry must be non-empty and fewer than 64 characters. |
| <CopyableCode code="lastUpdateTime" /> | `string` | Output only. The last update time of this saved query. |
| <CopyableCode code="lastUpdater" /> | `string` | Output only. The account's email address who has updated this saved query most recently. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name" /> | Gets details about a saved query. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | Lists all saved queries in a parent project/folder/organization. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="parent, parentType" /> | Creates a saved query in a parent project/folder/organization. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name" /> | Deletes a saved query. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="name" /> | Updates a saved query. |

## `SELECT` examples

Gets details about a saved query.

```sql
SELECT
name,
description,
content,
createTime,
creator,
labels,
lastUpdateTime,
lastUpdater
FROM google.cloudasset.saved_queries
WHERE name = '{{ name }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>saved_queries</code> resource.

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
INSERT INTO google.cloudasset.saved_queries (
parent,
parentType,
name,
description,
createTime,
creator,
lastUpdateTime,
lastUpdater,
labels,
content
)
SELECT 
'{{ parent }}',
'{{ parentType }}',
'{{ name }}',
'{{ description }}',
'{{ createTime }}',
'{{ creator }}',
'{{ lastUpdateTime }}',
'{{ lastUpdater }}',
'{{ labels }}',
'{{ content }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: description
        value: '{{ description }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: creator
        value: '{{ creator }}'
      - name: lastUpdateTime
        value: '{{ lastUpdateTime }}'
      - name: lastUpdater
        value: '{{ lastUpdater }}'
      - name: labels
        value: '{{ labels }}'
      - name: content
        value: '{{ content }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a saved_query only if the necessary resources are available.

```sql
UPDATE google.cloudasset.saved_queries
SET 
name = '{{ name }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
creator = '{{ creator }}',
lastUpdateTime = '{{ lastUpdateTime }}',
lastUpdater = '{{ lastUpdater }}',
labels = '{{ labels }}',
content = '{{ content }}'
WHERE 
name = '{{ name }}';
```

## `DELETE` example

Deletes the specified saved_query resource.

```sql
DELETE FROM google.cloudasset.saved_queries
WHERE name = '{{ name }}';
```
