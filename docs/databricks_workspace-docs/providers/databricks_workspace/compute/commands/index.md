---
title: commands
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - commands
  - compute
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>commands</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>commands</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.commands" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="results" /> | `object` |
| <CopyableCode code="status" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="commandstatus" /> | `SELECT` | <CopyableCode code="clusterId, commandId, contextId, deployment_name" /> | Gets the status of and, if available, the results from a currently executing command. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates an execution context for running cluster commands. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Cancels a currently running command within an execution context. |
| <CopyableCode code="destroy" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Deletes an execution context. |
| <CopyableCode code="execute" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Runs a cluster command in the given execution context, using the provided language. |

## `SELECT` examples

```sql
SELECT
id,
results,
status
FROM databricks_workspace.compute.commands
WHERE clusterId = '{{ clusterId }}' AND
commandId = '{{ commandId }}' AND
contextId = '{{ contextId }}' AND
deployment_name = '{{ deployment_name }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>commands</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'commands', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.compute.commands (
deployment_name,
data__clusterId,
data__language
)
SELECT 
'{{ deployment_name }}',
'{{ clusterId }}',
'{{ language }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: clusterId
    value: string
  - name: language
    value: python

```

</TabItem>
</Tabs>
