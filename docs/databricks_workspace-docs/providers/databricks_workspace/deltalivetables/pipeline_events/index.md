---
title: pipeline_events
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - pipeline_events
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

Operations on a <code>pipeline_events</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pipeline_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.deltalivetables.pipeline_events" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="error" /> | `object` |
| <CopyableCode code="event_type" /> | `string` |
| <CopyableCode code="level" /> | `string` |
| <CopyableCode code="maturity_level" /> | `string` |
| <CopyableCode code="message" /> | `string` |
| <CopyableCode code="origin" /> | `object` |
| <CopyableCode code="sequence" /> | `object` |
| <CopyableCode code="timestamp" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listpipelineevents" /> | `SELECT` | <CopyableCode code="pipeline_id, deployment_name" /> | Retrieves events for a pipeline. |

## `SELECT` examples

```sql
SELECT
id,
error,
event_type,
level,
maturity_level,
message,
origin,
sequence,
timestamp
FROM databricks_workspace.deltalivetables.pipeline_events
WHERE pipeline_id = '{{ pipeline_id }}' AND
deployment_name = '{{ deployment_name }}';
```
