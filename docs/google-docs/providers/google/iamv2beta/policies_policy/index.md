
---
title: policies_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - policies_policy
  - iamv2beta
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

Creates, updates, deletes or gets an <code>policies_policy</code> resource or lists <code>policies_policy</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.iamv2beta.policies_policy" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_policy" /> | `INSERT` | <CopyableCode code="policiesId, policiesId1" /> | Creates a policy. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policies_policy</code> resource.

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
INSERT INTO google.iamv2beta.policies_policy (
policiesId,
policiesId1,
name,
uid,
kind,
displayName,
annotations,
etag,
createTime,
updateTime,
deleteTime,
rules
)
SELECT 
'{{ policiesId }}',
'{{ policiesId1 }}',
'{{ name }}',
'{{ uid }}',
'{{ kind }}',
'{{ displayName }}',
'{{ annotations }}',
'{{ etag }}',
'{{ createTime }}',
'{{ updateTime }}',
'{{ deleteTime }}',
'{{ rules }}'
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
      - name: uid
        value: '{{ uid }}'
      - name: kind
        value: '{{ kind }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: annotations
        value: '{{ annotations }}'
      - name: etag
        value: '{{ etag }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: deleteTime
        value: '{{ deleteTime }}'
      - name: rules
        value: '{{ rules }}'

```
</TabItem>
</Tabs>
