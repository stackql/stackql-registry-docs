---
title: command_status
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - command_status
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

Operations on a <code>command_status</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>command_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.command_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="status" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="contextstatus" /> | `SELECT` | <CopyableCode code="clusterId, contextId, deployment_name" /> | Gets the status for an execution context. |

## `SELECT` examples

```sql
SELECT
id,
status
FROM databricks_workspace.compute.command_status
WHERE clusterId = '{{ clusterId }}' AND
contextId = '{{ contextId }}' AND
deployment_name = '{{ deployment_name }}';
```
