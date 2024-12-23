---
title: experiments_history
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - experiments_history
  - machinelearning
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

Operations on a <code>experiments_history</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiments_history</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.experiments_history" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="key" /> | `string` |
| <CopyableCode code="step" /> | `string` |
| <CopyableCode code="timestamp" /> | `integer` |
| <CopyableCode code="value" /> | `number` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="gethistory" /> | `SELECT` | <CopyableCode code="metric_key, deployment_name" /> | Gets a list of all values for the specified metric for a given run. |

## `SELECT` examples

```sql
SELECT
key,
step,
timestamp,
value
FROM databricks_workspace.machinelearning.experiments_history
WHERE metric_key = '{{ metric_key }}' AND
deployment_name = '{{ deployment_name }}';
```
