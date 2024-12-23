---
title: model_latest_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - model_latest_versions
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

Operations on a <code>model_latest_versions</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_latest_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_latest_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="creation_timestamp" /> | `integer` |
| <CopyableCode code="current_stage" /> | `string` |
| <CopyableCode code="last_updated_timestamp" /> | `integer` |
| <CopyableCode code="run_id" /> | `string` |
| <CopyableCode code="run_link" /> | `string` |
| <CopyableCode code="source" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="status_message" /> | `string` |
| <CopyableCode code="tags" /> | `array` |
| <CopyableCode code="user_id" /> | `string` |
| <CopyableCode code="version" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getlatestversions" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets the latest version of a registered model. |

## `SELECT` examples

```sql
SELECT
name,
description,
creation_timestamp,
current_stage,
last_updated_timestamp,
run_id,
run_link,
source,
status,
status_message,
tags,
user_id,
version
FROM databricks_workspace.machinelearning.model_latest_versions
WHERE deployment_name = '{{ deployment_name }}';
```
