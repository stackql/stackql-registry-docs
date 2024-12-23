---
title: share_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - share_permissions
  - deltasharing
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

Operations on a <code>share_permissions</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>share_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.deltasharing.share_permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="principal" /> | `string` |
| <CopyableCode code="privileges" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="sharepermissions" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Gets the permissions for a data share from the metastore. The caller must be a metastore admin or the owner of the share. |
| <CopyableCode code="updatepermissions" /> | `UPDATE` | <CopyableCode code="name, deployment_name" /> | Updates the permissions for a data share in the metastore. The caller must be a metastore admin or an owner of the share. |

## `SELECT` examples

```sql
SELECT
principal,
privileges
FROM databricks_workspace.deltasharing.share_permissions
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `UPDATE` example

Updates a <code>share_permissions</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.deltasharing.share_permissions
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
