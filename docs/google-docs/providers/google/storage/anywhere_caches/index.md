---
title: anywhere_caches
hide_title: false
hide_table_of_contents: false
keywords:
  - anywhere_caches
  - storage
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

Creates, updates, deletes, gets or lists a <code>anywhere_caches</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>anywhere_caches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storage.anywhere_caches" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the resource, including the project number, bucket name and anywhere cache ID. |
| <CopyableCode code="admissionPolicy" /> | `string` | The cache-level entry admission policy. |
| <CopyableCode code="anywhereCacheId" /> | `string` | The ID of the Anywhere cache instance. |
| <CopyableCode code="bucket" /> | `string` | The name of the bucket containing this cache instance. |
| <CopyableCode code="createTime" /> | `string` | The creation time of the cache instance in RFC 3339 format. |
| <CopyableCode code="kind" /> | `string` | The kind of item this is. For Anywhere Cache, this is always storage#anywhereCache. |
| <CopyableCode code="pendingUpdate" /> | `boolean` | True if the cache instance has an active Update long-running operation. |
| <CopyableCode code="selfLink" /> | `string` | The link to this cache instance. |
| <CopyableCode code="state" /> | `string` | The current state of the cache instance. |
| <CopyableCode code="ttl" /> | `string` | The TTL of all cache entries in whole seconds. e.g., "7200s".  |
| <CopyableCode code="updateTime" /> | `string` | The modification time of the cache instance metadata in RFC 3339 format. |
| <CopyableCode code="zone" /> | `string` | The zone in which the cache instance is running. For example, us-central1-a. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="anywhereCacheId, bucket" /> | Returns the metadata of an Anywhere Cache instance. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="bucket" /> | Returns a list of Anywhere Cache instances of the bucket matching the criteria. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="bucket" /> | Creates an Anywhere Cache instance. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="anywhereCacheId, bucket" /> | Updates the config(ttl and admissionPolicy) of an Anywhere Cache instance. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="anywhereCacheId, bucket" /> | Disables an Anywhere Cache instance. |
| <CopyableCode code="pause" /> | `EXEC` | <CopyableCode code="anywhereCacheId, bucket" /> | Pauses an Anywhere Cache instance. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="anywhereCacheId, bucket" /> | Resumes a paused or disabled Anywhere Cache instance. |

## `SELECT` examples

Returns a list of Anywhere Cache instances of the bucket matching the criteria.

```sql
SELECT
id,
admissionPolicy,
anywhereCacheId,
bucket,
createTime,
kind,
pendingUpdate,
selfLink,
state,
ttl,
updateTime,
zone
FROM google.storage.anywhere_caches
WHERE bucket = '{{ bucket }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>anywhere_caches</code> resource.

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
INSERT INTO google.storage.anywhere_caches (
bucket,
bucket,
anywhereCacheId,
zone,
state,
ttl,
admissionPolicy,
pendingUpdate
)
SELECT 
'{{ bucket }}',
'{{ bucket }}',
'{{ anywhereCacheId }}',
'{{ zone }}',
'{{ state }}',
'{{ ttl }}',
'{{ admissionPolicy }}',
{{ pendingUpdate }}
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: kind
      value: string
    - name: id
      value: string
    - name: selfLink
      value: string
    - name: bucket
      value: string
    - name: anywhereCacheId
      value: string
    - name: zone
      value: string
    - name: state
      value: string
    - name: createTime
      value: string
    - name: updateTime
      value: string
    - name: ttl
      value: string
    - name: admissionPolicy
      value: string
    - name: pendingUpdate
      value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>anywhere_caches</code> resource.

```sql
/*+ update */
UPDATE google.storage.anywhere_caches
SET 
bucket = '{{ bucket }}',
anywhereCacheId = '{{ anywhereCacheId }}',
zone = '{{ zone }}',
state = '{{ state }}',
ttl = '{{ ttl }}',
admissionPolicy = '{{ admissionPolicy }}',
pendingUpdate = true|false
WHERE 
anywhereCacheId = '{{ anywhereCacheId }}'
AND bucket = '{{ bucket }}';
```
