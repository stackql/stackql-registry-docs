---
title: endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - endpoints
  - vectorsearch
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

Operations on a <code>endpoints</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.vectorsearch.endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="creation_timestamp" /> | `integer` |
| <CopyableCode code="creator" /> | `string` |
| <CopyableCode code="endpoint_status" /> | `object` |
| <CopyableCode code="endpoint_type" /> | `string` |
| <CopyableCode code="last_updated_timestamp" /> | `integer` |
| <CopyableCode code="last_updated_user" /> | `string` |
| <CopyableCode code="num_indexes" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getendpoint" /> | `SELECT` | <CopyableCode code="endpoint_name, deployment_name" /> |  |
| <CopyableCode code="listendpoints" /> | `SELECT` | <CopyableCode code="deployment_name" /> |  |
| <CopyableCode code="createendpoint" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Create a new endpoint. |
| <CopyableCode code="deleteendpoint" /> | `DELETE` | <CopyableCode code="endpoint_name, deployment_name" /> |  |

## `SELECT` examples

<Tabs
    defaultValue="listendpoints"
    values={[
        { label: 'endpoints (listendpoints)', value: 'listendpoints' },
        { label: 'endpoints (getendpoint)', value: 'getendpoint' }
    ]
}>
<TabItem value="listendpoints">

```sql
SELECT
id,
name,
creation_timestamp,
creator,
endpoint_status,
endpoint_type,
last_updated_timestamp,
last_updated_user,
num_indexes
FROM databricks_workspace.vectorsearch.endpoints
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getendpoint">

```sql
SELECT
id,
name,
creation_timestamp,
creator,
endpoint_status,
endpoint_type,
last_updated_timestamp,
last_updated_user,
num_indexes
FROM databricks_workspace.vectorsearch.endpoints
WHERE endpoint_name = '{{ endpoint_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>endpoints</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'endpoints', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.vectorsearch.endpoints (
deployment_name,
data__name,
data__endpoint_type
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ endpoint_type }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: docs-endpoint
  - name: endpoint_type
    value: STANDARD

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.vectorsearch.endpoints
WHERE endpoint_name = '{{ endpoint_name }}' AND
deployment_name = '{{ deployment_name }}';
```
