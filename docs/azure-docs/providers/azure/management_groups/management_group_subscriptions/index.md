---
title: management_group_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - management_group_subscriptions
  - management_groups
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

Creates, updates, deletes, gets or lists a <code>management_group_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>management_group_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.management_groups.management_group_subscriptions" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="groupId, subscriptionId" /> | Associates existing subscription with the management group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="groupId, subscriptionId" /> | De-associates subscription from the management group. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>management_group_subscriptions</code> resource.

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
INSERT INTO azure.management_groups.management_group_subscriptions (
groupId,
subscriptionId
)
SELECT 
'{{ groupId }}',
'{{ subscriptionId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>management_group_subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.management_groups.management_group_subscriptions
WHERE groupId = '{{ groupId }}'
AND subscriptionId = '{{ subscriptionId }}';
```
