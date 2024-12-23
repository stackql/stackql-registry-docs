---
title: table_summaries
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - table_summaries
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

Operations on a <code>table_summaries</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>table_summaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.table_summaries" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="full_name" /> | `string` |
| <CopyableCode code="table_type" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listsummaries" /> | `SELECT` | <CopyableCode code="catalog_name, deployment_name" /> | Gets an array of summaries for tables for a schema and catalog within the metastore. The table summaries returned are either: |

## `SELECT` examples

```sql
SELECT
full_name,
table_type
FROM databricks_workspace.unitycatalog.table_summaries
WHERE catalog_name = '{{ catalog_name }}' AND
deployment_name = '{{ deployment_name }}';
```
