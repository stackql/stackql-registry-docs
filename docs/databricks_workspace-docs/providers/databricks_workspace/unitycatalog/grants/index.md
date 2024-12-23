---
title: grants
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - grants
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

Operations on a <code>grants</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.grants" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="principal" /> | `string` |
| <CopyableCode code="privileges" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="full_name, securable_type, deployment_name" /> | Gets the permissions for a securable. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="full_name, securable_type, deployment_name" /> | Updates the permissions for a securable. |

## `SELECT` examples

```sql
SELECT
principal,
privileges
FROM databricks_workspace.unitycatalog.grants
WHERE full_name = '{{ full_name }}' AND
securable_type = '{{ securable_type }}' AND
deployment_name = '{{ deployment_name }}';
```

## `UPDATE` example

Updates a <code>grants</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.unitycatalog.grants
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE full_name = '{{ full_name }}' AND
securable_type = '{{ securable_type }}' AND
deployment_name = '{{ deployment_name }}';
```
