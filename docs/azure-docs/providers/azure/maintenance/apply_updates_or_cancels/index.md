---
title: apply_updates_or_cancels
hide_title: false
hide_table_of_contents: false
keywords:
  - apply_updates_or_cancels
  - maintenance
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

Creates, updates, deletes, gets or lists a <code>apply_updates_or_cancels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apply_updates_or_cancels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.maintenance.apply_updates_or_cancels" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="applyUpdateName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId" /> | Apply maintenance updates to resource |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>apply_updates_or_cancels</code> resource.

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
INSERT INTO azure.maintenance.apply_updates_or_cancels (
applyUpdateName,
providerName,
resourceGroupName,
resourceName,
resourceType,
subscriptionId,
properties
)
SELECT 
'{{ applyUpdateName }}',
'{{ providerName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ resourceType }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: status
          value: string
        - name: resourceId
          value: string
        - name: lastUpdateTime
          value: string

```
</TabItem>
</Tabs>
