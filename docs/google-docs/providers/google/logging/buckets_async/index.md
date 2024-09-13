---
title: buckets_async
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets_async
  - logging
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

Creates, updates, deletes or gets an <code>buckets_async</code> resource or lists <code>buckets_async</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buckets_async</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.logging.buckets_async" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="billing_accounts_locations_buckets_create_async" /> | `INSERT` | <CopyableCode code="billingAccountsId, locationsId" /> | Creates a log bucket asynchronously that can be used to store log entries.After a bucket has been created, the bucket's location cannot be changed. |
| <CopyableCode code="folders_locations_buckets_create_async" /> | `INSERT` | <CopyableCode code="foldersId, locationsId" /> | Creates a log bucket asynchronously that can be used to store log entries.After a bucket has been created, the bucket's location cannot be changed. |
| <CopyableCode code="organizations_locations_buckets_create_async" /> | `INSERT` | <CopyableCode code="locationsId, organizationsId" /> | Creates a log bucket asynchronously that can be used to store log entries.After a bucket has been created, the bucket's location cannot be changed. |
| <CopyableCode code="projects_locations_buckets_create_async" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a log bucket asynchronously that can be used to store log entries.After a bucket has been created, the bucket's location cannot be changed. |
| <CopyableCode code="billing_accounts_locations_buckets_update_async" /> | `UPDATE` | <CopyableCode code="billingAccountsId, bucketsId, locationsId" /> | Updates a log bucket asynchronously.If the bucket has a lifecycle_state of DELETE_REQUESTED, then FAILED_PRECONDITION will be returned.After a bucket has been created, the bucket's location cannot be changed. |
| <CopyableCode code="folders_locations_buckets_update_async" /> | `UPDATE` | <CopyableCode code="bucketsId, foldersId, locationsId" /> | Updates a log bucket asynchronously.If the bucket has a lifecycle_state of DELETE_REQUESTED, then FAILED_PRECONDITION will be returned.After a bucket has been created, the bucket's location cannot be changed. |
| <CopyableCode code="organizations_locations_buckets_update_async" /> | `UPDATE` | <CopyableCode code="bucketsId, locationsId, organizationsId" /> | Updates a log bucket asynchronously.If the bucket has a lifecycle_state of DELETE_REQUESTED, then FAILED_PRECONDITION will be returned.After a bucket has been created, the bucket's location cannot be changed. |
| <CopyableCode code="projects_locations_buckets_update_async" /> | `UPDATE` | <CopyableCode code="bucketsId, locationsId, projectsId" /> | Updates a log bucket asynchronously.If the bucket has a lifecycle_state of DELETE_REQUESTED, then FAILED_PRECONDITION will be returned.After a bucket has been created, the bucket's location cannot be changed. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>buckets_async</code> resource.

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
INSERT INTO google.logging.buckets_async (
foldersId,
locationsId,
name,
description,
createTime,
updateTime,
retentionDays,
locked,
lifecycleState,
analyticsEnabled,
restrictedFields,
indexConfigs,
cmekSettings
)
SELECT 
'{{ foldersId }}',
'{{ locationsId }}',
'{{ name }}',
'{{ description }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ retentionDays }}',
true|false,
'{{ lifecycleState }}',
true|false,
'{{ restrictedFields }}',
'{{ indexConfigs }}',
'{{ cmekSettings }}'
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
      - name: updateTime
        value: '{{ updateTime }}'
      - name: retentionDays
        value: '{{ retentionDays }}'
      - name: locked
        value: '{{ locked }}'
      - name: lifecycleState
        value: '{{ lifecycleState }}'
      - name: analyticsEnabled
        value: '{{ analyticsEnabled }}'
      - name: restrictedFields
        value: '{{ restrictedFields }}'
      - name: indexConfigs
        value: '{{ indexConfigs }}'
      - name: cmekSettings
        value: '{{ cmekSettings }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a buckets_async only if the necessary resources are available.

```sql
UPDATE google.logging.buckets_async
SET 
name = '{{ name }}',
description = '{{ description }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
retentionDays = '{{ retentionDays }}',
locked = true|false,
lifecycleState = '{{ lifecycleState }}',
analyticsEnabled = true|false,
restrictedFields = '{{ restrictedFields }}',
indexConfigs = '{{ indexConfigs }}',
cmekSettings = '{{ cmekSettings }}'
WHERE 
bucketsId = '{{ bucketsId }}'
AND foldersId = '{{ foldersId }}'
AND locationsId = '{{ locationsId }}';
```
