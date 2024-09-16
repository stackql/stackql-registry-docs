---
title: feeds
hide_title: false
hide_table_of_contents: false
keywords:
  - feeds
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

Creates, updates, deletes, gets or lists a <code>feeds</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feeds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudasset.feeds" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="feeds" /> | `array` | A list of feeds. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | Lists all asset feeds in a parent project/folder/organization. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="parent, parentType" /> | Creates a feed in a parent project/folder/organization to listen to its asset updates. |

## `SELECT` examples

Lists all asset feeds in a parent project/folder/organization.

```sql
SELECT
feeds
FROM google.cloudasset.feeds
WHERE parent = '{{ parent }}'
AND parentType = '{{ parentType }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>feeds</code> resource.

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
INSERT INTO google.cloudasset.feeds (
parent,
parentType,
feedId,
feed
)
SELECT 
'{{ parent }}',
'{{ parentType }}',
'{{ feedId }}',
'{{ feed }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: feedId
      value: '{{ feedId }}'
    - name: feed
      value: '{{ feed }}'

```
</TabItem>
</Tabs>
