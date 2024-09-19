---
title: agent_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools
  - storagetransfer
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

Creates, updates, deletes, gets or lists a <code>agent_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agent_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.storagetransfer.agent_pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. Specifies a unique string that identifies the agent pool. Format: `projects/{project_id}/agentPools/{agent_pool_id}` |
| <CopyableCode code="bandwidthLimit" /> | `object` | Specifies a bandwidth limit for an agent pool. |
| <CopyableCode code="displayName" /> | `string` | Specifies the client-specified AgentPool description. |
| <CopyableCode code="state" /> | `string` | Output only. Specifies the state of the AgentPool. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="agentPoolsId, projectsId" /> | Gets an agent pool. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists agent pools. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates an agent pool resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="agentPoolsId, projectsId" /> | Deletes an agent pool. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="agentPoolsId, projectsId" /> | Updates an existing agent pool resource. |

## `SELECT` examples

Lists agent pools.

```sql
SELECT
name,
bandwidthLimit,
displayName,
state
FROM google.storagetransfer.agent_pools
WHERE projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>agent_pools</code> resource.

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
INSERT INTO google.storagetransfer.agent_pools (
projectsId,
name,
displayName,
bandwidthLimit
)
SELECT 
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ bandwidthLimit }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: displayName
      value: string
    - name: state
      value: string
    - name: bandwidthLimit
      value:
        - name: limitMbps
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>agent_pools</code> resource.

```sql
/*+ update */
UPDATE google.storagetransfer.agent_pools
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
bandwidthLimit = '{{ bandwidthLimit }}'
WHERE 
agentPoolsId = '{{ agentPoolsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>agent_pools</code> resource.

```sql
/*+ delete */
DELETE FROM google.storagetransfer.agent_pools
WHERE agentPoolsId = '{{ agentPoolsId }}'
AND projectsId = '{{ projectsId }}';
```
