---
title: data_flow_debug_sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - data_flow_debug_sessions
  - data_factory
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

Creates, updates, deletes, gets or lists a <code>data_flow_debug_sessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_flow_debug_sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.data_flow_debug_sessions" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Creates a data flow debug session. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Deletes a data flow debug session. |
| <CopyableCode code="add_data_flow" /> | `EXEC` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Add a data flow into debug session. |
| <CopyableCode code="execute_command" /> | `EXEC` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Execute a data flow debug command. |
| <CopyableCode code="query_by_factory" /> | `EXEC` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Query all active data flow debug sessions. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_flow_debug_sessions</code> resource.

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
INSERT INTO azure.data_factory.data_flow_debug_sessions (
factoryName,
resourceGroupName,
subscriptionId,
computeType,
coreCount,
timeToLive,
integrationRuntime
)
SELECT 
'{{ factoryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ computeType }}',
'{{ coreCount }}',
'{{ timeToLive }}',
'{{ integrationRuntime }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: computeType
      value: string
    - name: coreCount
      value: integer
    - name: timeToLive
      value: integer
    - name: integrationRuntime
      value:
        - name: name
          value: string
        - name: properties
          value:
            - name: type
              value: []
            - name: description
              value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>data_flow_debug_sessions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_factory.data_flow_debug_sessions
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
