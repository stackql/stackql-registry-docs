---
title: debugsessions
hide_title: false
hide_table_of_contents: false
keywords:
  - debugsessions
  - apigee
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

Creates, updates, deletes, gets or lists a <code>debugsessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>debugsessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.apigee.debugsessions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | A unique ID for this DebugSession. |
| <CopyableCode code="count" /> | `integer` | Optional. The number of request to be traced. Min = 1, Max = 15, Default = 10. |
| <CopyableCode code="createTime" /> | `string` | Output only. The first transaction creation timestamp, recorded by UAP. |
| <CopyableCode code="filter" /> | `string` | Optional. A conditional statement which is evaluated against the request message to determine if it should be traced. Syntax matches that of on API Proxy bundle flow Condition. |
| <CopyableCode code="timeout" /> | `string` | Optional. The time in seconds after which this DebugSession should end. This value will override the value in query param, if both are provided. |
| <CopyableCode code="tracesize" /> | `integer` | Optional. The maximum number of bytes captured from the response payload. Min = 0, Max = 5120, Default = 5120. |
| <CopyableCode code="validity" /> | `integer` | Optional. The length of time, in seconds, that this debug session is valid, starting from when it's received in the control plane. Min = 1, Max = 15, Default = 10. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_environments_apis_revisions_debugsessions_get" /> | `SELECT` | <CopyableCode code="apisId, debugsessionsId, environmentsId, organizationsId, revisionsId" /> | Retrieves a debug session. |
| <CopyableCode code="organizations_environments_apis_revisions_debugsessions_list" /> | `SELECT` | <CopyableCode code="apisId, environmentsId, organizationsId, revisionsId" /> | Lists debug sessions that are currently active in the given API Proxy revision. |
| <CopyableCode code="organizations_environments_apis_revisions_debugsessions_create" /> | `INSERT` | <CopyableCode code="apisId, environmentsId, organizationsId, revisionsId" /> | Creates a debug session for a deployed API Proxy revision. |

## `SELECT` examples

Lists debug sessions that are currently active in the given API Proxy revision.

```sql
SELECT
name,
count,
createTime,
filter,
timeout,
tracesize,
validity
FROM google.apigee.debugsessions
WHERE apisId = '{{ apisId }}'
AND environmentsId = '{{ environmentsId }}'
AND organizationsId = '{{ organizationsId }}'
AND revisionsId = '{{ revisionsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>debugsessions</code> resource.

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
INSERT INTO google.apigee.debugsessions (
apisId,
environmentsId,
organizationsId,
revisionsId,
timeout,
validity,
name,
count,
filter,
tracesize
)
SELECT 
'{{ apisId }}',
'{{ environmentsId }}',
'{{ organizationsId }}',
'{{ revisionsId }}',
'{{ timeout }}',
'{{ validity }}',
'{{ name }}',
'{{ count }}',
'{{ filter }}',
'{{ tracesize }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: timeout
      value: string
    - name: validity
      value: integer
    - name: name
      value: string
    - name: count
      value: integer
    - name: filter
      value: string
    - name: tracesize
      value: integer
    - name: createTime
      value: string

```
</TabItem>
</Tabs>
