---
title: system_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - system_schemas
  - unitycatalog
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

Operations on a <code>system_schemas</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>system_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.system_schemas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="schema" /> | `string` |
| <CopyableCode code="state" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="metastore_id, deployment_name" /> | Gets an array of system schemas for a metastore. The caller must be an account admin or a metastore admin. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="metastore_id, schema_name, deployment_name" /> | Disables the system schema and removes it from the system catalog. The caller must be an account admin or a metastore admin. |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="metastore_id, schema_name, deployment_name" /> | Enables the system schema and adds it to the system catalog. The caller must be an account admin or a metastore admin. |

## `SELECT` examples

```sql
SELECT
schema,
state
FROM databricks_workspace.unitycatalog.system_schemas
WHERE metastore_id = '{{ metastore_id }}' AND
deployment_name = '{{ deployment_name }}';
```
