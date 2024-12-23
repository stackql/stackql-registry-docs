---
title: feature_status
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - feature_status
  - workspace
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

Operations on a <code>feature_status</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>feature_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.feature_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="property1" /> | `string` |
| <CopyableCode code="property2" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getstatus" /> | `SELECT` | <CopyableCode code="keys, deployment_name" /> | Enables or disables a specified feature for a workspace. |
| <CopyableCode code="setstatus" /> | `REPLACE` | <CopyableCode code="deployment_name" /> | Enables or disables a specified feature for a workspace. |

## `SELECT` examples

```sql
SELECT
property1,
property2
FROM databricks_workspace.workspace.feature_status
WHERE keys = '{{ keys }}' AND
deployment_name = '{{ deployment_name }}';
```

## `REPLACE` example

Replaces a <code>feature_status</code> resource.

```sql
/*+ update */
REPLACE databricks_workspace.workspace.feature_status
SET { field = value }
WHERE deployment_name = '{{ deployment_name }}';
```
