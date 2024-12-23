---
title: logs
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - logs
  - realtimeserving
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

Operations on a <code>logs</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.realtimeserving.logs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="logs" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="logs" /> | `SELECT` | <CopyableCode code="name, served_model_name, deployment_name" /> | Retrieves the service logs associated with the provided served model. |

## `SELECT` examples

```sql
SELECT
logs
FROM databricks_workspace.realtimeserving.logs
WHERE name = '{{ name }}' AND
served_model_name = '{{ served_model_name }}' AND
deployment_name = '{{ deployment_name }}';
```
