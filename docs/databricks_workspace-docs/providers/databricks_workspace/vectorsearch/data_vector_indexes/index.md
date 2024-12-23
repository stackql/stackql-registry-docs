---
title: data_vector_indexes
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - data_vector_indexes
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

Operations on a <code>data_vector_indexes</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_vector_indexes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.vectorsearch.data_vector_indexes" /></td></tr>
</tbody></table>


`SELECT` not supported for this resource, see the methods section for supported operations.
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="deletedatavectorindex" /> | `DELETE` | <CopyableCode code="index_name, deployment_name" /> | Handles the deletion of data from a specified vector index. |
| <CopyableCode code="upsertdatavectorindex" /> | `REPLACE` | <CopyableCode code="index_name, deployment_name" /> | Handles the upserting of data into a specified vector index. |

## `REPLACE` example

Replaces a <code>data_vector_indexes</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_workspace.vectorsearch.data_vector_indexes
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE index_name = '{{ index_name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>data_vector_indexes</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.vectorsearch.data_vector_indexes
WHERE index_name = '{{ index_name }}' AND
deployment_name = '{{ deployment_name }}';
```
