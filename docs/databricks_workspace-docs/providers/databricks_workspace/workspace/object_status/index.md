---
title: object_status
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - object_status
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

Operations on a <code>object_status</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>object_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.object_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="language" /> | `string` |
| <CopyableCode code="object_id" /> | `integer` |
| <CopyableCode code="object_type" /> | `string` |
| <CopyableCode code="path" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getstatus" /> | `SELECT` | <CopyableCode code="path, deployment_name" /> | Gets the status of an object or a directory. If |

## `SELECT` examples

```sql
SELECT
language,
object_id,
object_type,
path
FROM databricks_workspace.workspace.object_status
WHERE path = '{{ path }}' AND
deployment_name = '{{ deployment_name }}';
```
