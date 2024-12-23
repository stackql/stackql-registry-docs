---
title: registered_model_aliases
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - registered_model_aliases
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

Operations on a <code>registered_model_aliases</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registered_model_aliases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.registered_model_aliases" /></td></tr>
</tbody></table>


`SELECT` not supported for this resource, see the methods section for supported operations.
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="deletealias" /> | `DELETE` | <CopyableCode code="alias, full_name, deployment_name" /> | Deletes a registered model alias. |
| <CopyableCode code="setalias" /> | `REPLACE` | <CopyableCode code="alias, full_name, deployment_name" /> | Set an alias on the specified registered model. |

## `REPLACE` example

Replaces a <code>registered_model_aliases</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_workspace.unitycatalog.registered_model_aliases
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE alias = '{{ alias }}' AND
full_name = '{{ full_name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>registered_model_aliases</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.registered_model_aliases
WHERE alias = '{{ alias }}' AND
full_name = '{{ full_name }}' AND
deployment_name = '{{ deployment_name }}';
```
