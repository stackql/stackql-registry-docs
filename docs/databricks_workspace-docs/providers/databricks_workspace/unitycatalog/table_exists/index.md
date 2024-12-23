---
title: table_exists
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - table_exists
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

Operations on a <code>table_exists</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>table_exists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.table_exists" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="table_exists" /> | `boolean` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="exists" /> | `SELECT` | <CopyableCode code="full_name, deployment_name" /> | Gets if a table exists in the metastore for a specific catalog and schema. The caller must satisfy one of the following requirements: |

## `SELECT` examples

```sql
SELECT
table_exists
FROM databricks_workspace.unitycatalog.table_exists
WHERE full_name = '{{ full_name }}' AND
deployment_name = '{{ deployment_name }}';
```
