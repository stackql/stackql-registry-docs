---
title: artifact_allow_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - artifact_allow_lists
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

Operations on a <code>artifact_allow_lists</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>artifact_allow_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.artifact_allow_lists" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="artifact_matchers" /> | `array` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="metastore_id" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="artifact_type, deployment_name" /> | Get the artifact allowlist of a certain artifact type. The caller must be a metastore admin or have the |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="artifact_type, deployment_name" /> | Set the artifact allowlist of a certain artifact type. The whole artifact allowlist is replaced with the new allowlist. The caller must be a metastore admin or have the |

## `SELECT` examples

```sql
SELECT
artifact_matchers,
created_at,
created_by,
metastore_id
FROM databricks_workspace.unitycatalog.artifact_allow_lists
WHERE artifact_type = '{{ artifact_type }}' AND
deployment_name = '{{ deployment_name }}';
```

## `UPDATE` example

Updates a <code>artifact_allow_lists</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.unitycatalog.artifact_allow_lists
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE artifact_type = '{{ artifact_type }}' AND
deployment_name = '{{ deployment_name }}';
```
