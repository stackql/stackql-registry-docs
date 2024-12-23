---
title: index_scan
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - index_scan
  - vectorsearch
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

Operations on a <code>index_scan</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>index_scan</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.vectorsearch.index_scan" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="data" /> | `array` |
| <CopyableCode code="last_primary_key" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="scanindex" /> | `SELECT` | <CopyableCode code="index_name, deployment_name" /> | Scan the specified vector index and return the first |

## `SELECT` examples

```sql
SELECT
data,
last_primary_key
FROM databricks_workspace.vectorsearch.index_scan
WHERE index_name = '{{ index_name }}' AND
deployment_name = '{{ deployment_name }}';
```
