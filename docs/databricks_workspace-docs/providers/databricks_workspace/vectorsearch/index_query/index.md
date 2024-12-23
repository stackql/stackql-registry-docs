---
title: index_query
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - index_query
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

Operations on a <code>index_query</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>index_query</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.vectorsearch.index_query" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="manifest" /> | `object` |
| <CopyableCode code="next_page_token" /> | `string` |
| <CopyableCode code="result" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="queryindex" /> | `SELECT` | <CopyableCode code="index_name, deployment_name" /> | Query the specified vector index. |

## `SELECT` examples

```sql
SELECT
manifest,
next_page_token,
result
FROM databricks_workspace.vectorsearch.index_query
WHERE index_name = '{{ index_name }}' AND
deployment_name = '{{ deployment_name }}';
```
