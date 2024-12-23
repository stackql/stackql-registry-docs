---
title: pipeline_updates
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - pipeline_updates
  - deltalivetables
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

Operations on a <code>pipeline_updates</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline_updates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.deltalivetables.pipeline_updates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="cause" /> | `string` |
| <CopyableCode code="cluster_id" /> | `string` |
| <CopyableCode code="config" /> | `object` |
| <CopyableCode code="creation_time" /> | `integer` |
| <CopyableCode code="full_refresh" /> | `boolean` |
| <CopyableCode code="full_refresh_selection" /> | `array` |
| <CopyableCode code="pipeline_id" /> | `string` |
| <CopyableCode code="refresh_selection" /> | `array` |
| <CopyableCode code="state" /> | `string` |
| <CopyableCode code="update_id" /> | `string` |
| <CopyableCode code="validate_only" /> | `boolean` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getupdate" /> | `SELECT` | <CopyableCode code="pipeline_id, update_id, deployment_name" /> | Gets an update from an active pipeline. |
| <CopyableCode code="listupdates" /> | `SELECT` | <CopyableCode code="pipeline_id, deployment_name" /> | List updates for an active pipeline. |
| <CopyableCode code="startupdate" /> | `EXEC` | <CopyableCode code="pipeline_id, deployment_name" /> | Starts a new update for the pipeline. If there is already an active update for the pipeline, the request will fail and the active update will remain running. |

## `SELECT` examples

<Tabs
    defaultValue="listupdates"
    values={[
        { label: 'pipeline_updates (listupdates)', value: 'listupdates' },
        { label: 'pipeline_updates (getupdate)', value: 'getupdate' }
    ]
}>
<TabItem value="listupdates">

```sql
SELECT
cause,
cluster_id,
config,
creation_time,
full_refresh,
full_refresh_selection,
pipeline_id,
refresh_selection,
state,
update_id,
validate_only
FROM databricks_workspace.deltalivetables.pipeline_updates
WHERE pipeline_id = '{{ pipeline_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getupdate">

```sql
SELECT
cause,
cluster_id,
config,
creation_time,
full_refresh,
full_refresh_selection,
pipeline_id,
refresh_selection,
state,
update_id,
validate_only
FROM databricks_workspace.deltalivetables.pipeline_updates
WHERE pipeline_id = '{{ pipeline_id }}' AND
update_id = '{{ update_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>
