---
title: model_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - model_tags
  - machinelearning
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

Operations on a <code>model_tags</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_tags" /></td></tr>
</tbody></table>


`SELECT` not supported for this resource, see the methods section for supported operations.
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="deletemodeltag" /> | `DELETE` | <CopyableCode code="key, name, deployment_name" /> | Deletes the tag for a registered model. |
| <CopyableCode code="setmodeltag" /> | `REPLACE` | <CopyableCode code="deployment_name" /> | Sets a tag on a registered model. |

## `REPLACE` example

Replaces a <code>model_tags</code> resource.

```sql
/*+ update */
REPLACE databricks_workspace.machinelearning.model_tags
SET { field = value }
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>model_tags</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.machinelearning.model_tags
WHERE key = '{{ key }}' AND
name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
