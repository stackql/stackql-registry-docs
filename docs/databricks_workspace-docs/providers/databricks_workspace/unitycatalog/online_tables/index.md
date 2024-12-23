---
title: online_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - online_tables
  - unitycatalog
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

Operations on a <code>online_tables</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>online_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.online_tables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="spec" /> | `object` |
| <CopyableCode code="status" /> | `object` |
| <CopyableCode code="table_serving_url" /> | `string` |
| <CopyableCode code="unity_catalog_provisioning_state" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Get information about an existing online table and its status. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Create a new Online Table. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, deployment_name" /> | Delete an online table. Warning: This will delete all the data in the online table. If the source Delta table was deleted or modified since this Online Table was created, this will lose the data forever! |

## `SELECT` examples

```sql
SELECT
name,
spec,
status,
table_serving_url,
unity_catalog_provisioning_state
FROM databricks_workspace.unitycatalog.online_tables
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>online_tables</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'online_tables', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.unitycatalog.online_tables (
deployment_name,
data__name,
data__spec
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ spec }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: string
  - name: spec
    value:
      run_continuously: {}
      run_triggered: {}
      source_table_full_name: string
      primary_key_columns:
      - string
      timeseries_key: string
      perform_full_copy: false
      pipeline_id: string

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>online_tables</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.online_tables
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
