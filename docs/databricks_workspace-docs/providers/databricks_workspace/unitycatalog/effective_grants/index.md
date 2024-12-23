---
title: effective_grants
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - effective_grants
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

Operations on a <code>effective_grants</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>effective_grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.effective_grants" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="principal" /> | `string` |
| <CopyableCode code="privileges" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="geteffective" /> | `SELECT` | <CopyableCode code="full_name, securable_type, deployment_name" /> | Gets the effective permissions for a securable. |

## `SELECT` examples

```sql
SELECT
principal,
privileges
FROM databricks_workspace.unitycatalog.effective_grants
WHERE full_name = '{{ full_name }}' AND
securable_type = '{{ securable_type }}' AND
deployment_name = '{{ deployment_name }}';
```
