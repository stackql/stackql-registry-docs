---
title: quality_monitor_refreshes
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - quality_monitor_refreshes
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

Operations on a <code>quality_monitor_refreshes</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>quality_monitor_refreshes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.quality_monitor_refreshes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="end_time_ms" /> | `integer` |
| <CopyableCode code="message" /> | `string` |
| <CopyableCode code="refresh_id" /> | `integer` |
| <CopyableCode code="start_time_ms" /> | `integer` |
| <CopyableCode code="state" /> | `string` |
| <CopyableCode code="trigger" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getrefresh" /> | `SELECT` | <CopyableCode code="refresh_id, table_name, deployment_name" /> | Gets info about a specific monitor refresh using the given refresh ID. |
| <CopyableCode code="listrefreshes" /> | `SELECT` | <CopyableCode code="table_name, deployment_name" /> | Gets an array containing the history of the most recent refreshes (up to 25) for this table. |
| <CopyableCode code="runrefresh" /> | `EXEC` | <CopyableCode code="table_name, deployment_name" /> | Queues a metric refresh on the monitor for the specified table. The refresh will execute in the background. |

## `SELECT` examples

<Tabs
    defaultValue="listrefreshes"
    values={[
        { label: 'quality_monitor_refreshes (listrefreshes)', value: 'listrefreshes' },
        { label: 'quality_monitor_refreshes (getrefresh)', value: 'getrefresh' }
    ]
}>
<TabItem value="listrefreshes">

```sql
SELECT
end_time_ms,
message,
refresh_id,
start_time_ms,
state,
trigger
FROM databricks_workspace.unitycatalog.quality_monitor_refreshes
WHERE table_name = '{{ table_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getrefresh">

```sql
SELECT
end_time_ms,
message,
refresh_id,
start_time_ms,
state,
trigger
FROM databricks_workspace.unitycatalog.quality_monitor_refreshes
WHERE refresh_id = '{{ refresh_id }}' AND
table_name = '{{ table_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>
