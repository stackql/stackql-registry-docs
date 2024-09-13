---
title: address_groups_items
hide_title: false
hide_table_of_contents: false
keywords:
  - address_groups_items
  - networksecurity
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

Creates, updates, deletes, gets or lists a <code>address_groups_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>address_groups_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networksecurity.address_groups_items" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_address_groups_add_items" /> | `INSERT` | <CopyableCode code="addressGroupsId, locationsId, organizationsId" /> | Adds items to an address group. |
| <CopyableCode code="projects_locations_address_groups_add_items" /> | `INSERT` | <CopyableCode code="addressGroupsId, locationsId, projectsId" /> | Adds items to an address group. |
| <CopyableCode code="organizations_locations_address_groups_remove_items" /> | `DELETE` | <CopyableCode code="addressGroupsId, locationsId, organizationsId" /> | Removes items from an address group. |
| <CopyableCode code="projects_locations_address_groups_remove_items" /> | `DELETE` | <CopyableCode code="addressGroupsId, locationsId, projectsId" /> | Removes items from an address group. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>address_groups_items</code> resource.

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
INSERT INTO google.networksecurity.address_groups_items (
addressGroupsId,
locationsId,
projectsId,
items,
requestId
)
SELECT 
'{{ addressGroupsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ items }}',
'{{ requestId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: items
        value: '{{ items }}'
      - name: requestId
        value: '{{ requestId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>address_groups_items</code> resource.

```sql
/*+ delete */
DELETE FROM google.networksecurity.address_groups_items
WHERE addressGroupsId = '{{ addressGroupsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
