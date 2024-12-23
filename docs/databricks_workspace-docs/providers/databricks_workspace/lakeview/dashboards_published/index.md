---
title: dashboards_published
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - dashboards_published
  - lakeview
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

Operations on a <code>dashboards_published</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboards_published</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.lakeview.dashboards_published" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="display_name" /> | `string` |
| <CopyableCode code="embed_credentials" /> | `boolean` |
| <CopyableCode code="revision_create_time" /> | `string` |
| <CopyableCode code="warehouse_id" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getpublished" /> | `SELECT` | <CopyableCode code="dashboard_id, deployment_name" /> | Get the current published dashboard. |

## `SELECT` examples

```sql
SELECT
display_name,
embed_credentials,
revision_create_time,
warehouse_id
FROM databricks_workspace.lakeview.dashboards_published
WHERE dashboard_id = '{{ dashboard_id }}' AND
deployment_name = '{{ deployment_name }}';
```
