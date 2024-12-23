---
title: model_version_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - model_version_tags
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

Operations on a <code>model_version_tags</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_version_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_version_tags" /></td></tr>
</tbody></table>


`SELECT` not supported for this resource, see the methods section for supported operations.
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="deletemodelversiontag" /> | `DELETE` | <CopyableCode code="key, name, version, deployment_name" /> | Deletes a model version tag. |
| <CopyableCode code="setmodelversiontag" /> | `REPLACE` | <CopyableCode code="deployment_name" /> | Sets a model version tag. |

## `REPLACE` example

Replaces a <code>model_version_tags</code> resource.

```sql
/*+ update */
REPLACE databricks_workspace.machinelearning.model_version_tags
SET { field = value }
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>model_version_tags</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.machinelearning.model_version_tags
WHERE key = '{{ key }}' AND
name = '{{ name }}' AND
version = '{{ version }}' AND
deployment_name = '{{ deployment_name }}';
```
