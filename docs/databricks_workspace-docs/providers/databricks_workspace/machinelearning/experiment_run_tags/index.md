---
title: experiment_run_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - experiment_run_tags
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

Operations on a <code>experiment_run_tags</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>experiment_run_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.experiment_run_tags" /></td></tr>
</tbody></table>


`SELECT` not supported for this resource, see the methods section for supported operations.
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="settag" /> | `REPLACE` | <CopyableCode code="deployment_name" /> | Sets a tag on a run. Tags are run metadata that can be updated during a run and after a run completes. |

## `REPLACE` example

Replaces a <code>experiment_run_tags</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_workspace.machinelearning.experiment_run_tags
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE deployment_name = '{{ deployment_name }}';
```
