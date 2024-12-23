---
title: recipient_share_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - recipient_share_permissions
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

Operations on a <code>recipient_share_permissions</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recipient_share_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.deltasharing.recipient_share_permissions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="privilege_assignments" /> | `array` |
| <CopyableCode code="share_name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="sharepermissions" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Gets the share permissions for the specified Recipient. The caller must be a metastore admin or the owner of the Recipient. |

## `SELECT` examples

```sql
SELECT
privilege_assignments,
share_name
FROM databricks_workspace.deltasharing.recipient_share_permissions
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
