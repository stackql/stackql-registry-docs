---
title: cluster_events
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - cluster_events
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

Operations on a <code>cluster_events</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.cluster_events" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="events" /> | `array` |
| <CopyableCode code="next_page" /> | `object` |
| <CopyableCode code="total_count" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="events" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Retrieves a list of events about the activity of a cluster. This API is paginated. If there are more events to read, the response includes all the nparameters necessary to request the next page of events. |

## `SELECT` examples

```sql
SELECT
events,
next_page,
total_count
FROM databricks_workspace.compute.cluster_events
WHERE deployment_name = '{{ deployment_name }}';
```
