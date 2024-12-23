---
title: policy_families
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - policy_families
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

Operations on a <code>policy_families</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_families</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.policy_families" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="definition" /> | `object` |
| <CopyableCode code="policy_family_id" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policy_family_id, deployment_name" /> | Retrieve the information for an policy family based on its identifier and version |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Returns the list of policy definition types available to use at their latest version. This API is paginated. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'policy_families (list)', value: 'list' },
        { label: 'policy_families (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
name,
description,
definition,
policy_family_id
FROM databricks_workspace.compute.policy_families
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
name,
description,
definition,
policy_family_id
FROM databricks_workspace.compute.policy_families
WHERE policy_family_id = '{{ policy_family_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>
