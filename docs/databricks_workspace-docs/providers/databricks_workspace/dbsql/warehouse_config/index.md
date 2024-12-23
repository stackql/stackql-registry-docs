---
title: warehouse_config
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - warehouse_config
  - dbsql
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

Operations on a <code>warehouse_config</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>warehouse_config</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.dbsql.warehouse_config" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="channel" /> | `object` |
| <CopyableCode code="config_param" /> | `object` |
| <CopyableCode code="data_access_config" /> | `array` |
| <CopyableCode code="enabled_warehouse_types" /> | `array` |
| <CopyableCode code="global_param" /> | `object` |
| <CopyableCode code="google_service_account" /> | `string` |
| <CopyableCode code="instance_profile_arn" /> | `string` |
| <CopyableCode code="security_policy" /> | `string` |
| <CopyableCode code="sql_configuration_parameters" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getworkspacewarehouseconfig" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets the workspace level configuration that is shared by all SQL warehouses in a workspace. |
| <CopyableCode code="setworkspacewarehouseconfig" /> | `REPLACE` | <CopyableCode code="deployment_name" /> | Sets the workspace level configuration that is shared by all SQL warehouses in a workspace. |

## `SELECT` examples

```sql
SELECT
channel,
config_param,
data_access_config,
enabled_warehouse_types,
global_param,
google_service_account,
instance_profile_arn,
security_policy,
sql_configuration_parameters
FROM databricks_workspace.dbsql.warehouse_config
WHERE deployment_name = '{{ deployment_name }}';
```

## `REPLACE` example

Replaces a <code>warehouse_config</code> resource.

```sql
/*+ update */
REPLACE databricks_workspace.dbsql.warehouse_config
SET { field = value }
WHERE deployment_name = '{{ deployment_name }}';
```
