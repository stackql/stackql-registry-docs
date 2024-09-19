---
title: backend_buckets_signed_url_key
hide_title: false
hide_table_of_contents: false
keywords:
  - backend_buckets_signed_url_key
  - compute
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

Creates, updates, deletes, gets or lists a <code>backend_buckets_signed_url_key</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backend_buckets_signed_url_key</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.compute.backend_buckets_signed_url_key" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_signed_url_key" /> | `INSERT` | <CopyableCode code="backendBucket, project" /> | Adds a key for validating requests with signed URLs for this backend bucket. |
| <CopyableCode code="delete_signed_url_key" /> | `DELETE` | <CopyableCode code="backendBucket, keyName, project" /> | Deletes a key for validating requests with signed URLs for this backend bucket. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>backend_buckets_signed_url_key</code> resource.

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
INSERT INTO google.compute.backend_buckets_signed_url_key (
backendBucket,
project,
keyName,
keyValue
)
SELECT 
'{{ backendBucket }}',
'{{ project }}',
'{{ keyName }}',
'{{ keyValue }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: keyName
      value: string
    - name: keyValue
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>backend_buckets_signed_url_key</code> resource.

```sql
/*+ delete */
DELETE FROM google.compute.backend_buckets_signed_url_key
WHERE backendBucket = '{{ backendBucket }}'
AND keyName = '{{ keyName }}'
AND project = '{{ project }}';
```
