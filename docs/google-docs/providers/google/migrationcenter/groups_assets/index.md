---
title: groups_assets
hide_title: false
hide_table_of_contents: false
keywords:
  - groups_assets
  - migrationcenter
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

Creates, updates, deletes, gets or lists a <code>groups_assets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups_assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.migrationcenter.groups_assets" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_assets" /> | `INSERT` | <CopyableCode code="groupsId, locationsId, projectsId" /> | Adds assets to a group. |
| <CopyableCode code="remove_assets" /> | `DELETE` | <CopyableCode code="groupsId, locationsId, projectsId" /> | Removes assets from a group. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>groups_assets</code> resource.

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
INSERT INTO google.migrationcenter.groups_assets (
groupsId,
locationsId,
projectsId,
requestId,
assets,
allowExisting
)
SELECT 
'{{ groupsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ requestId }}',
'{{ assets }}',
true|false
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: requestId
      value: '{{ requestId }}'
    - name: assets
      value:
        - name: assetIds
          value:
            - name: type
              value: '{{ type }}'
    - name: allowExisting
      value: '{{ allowExisting }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>groups_assets</code> resource.

```sql
/*+ delete */
DELETE FROM google.migrationcenter.groups_assets
WHERE groupsId = '{{ groupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
