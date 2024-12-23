---
title: objects
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - objects
  - workspace
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

Operations on a <code>objects</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>objects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.objects" /></td></tr>
</tbody></table>


`SELECT` not supported for this resource, see the methods section for supported operations.
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Deletes an object or a directory (and optionally recursively deletes all objects in the directory). |
| <CopyableCode code="export" /> | `EXEC` | <CopyableCode code="path, deployment_name" /> | Exports an object or the contents of an entire directory. |
| <CopyableCode code="import" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Imports a workspace object (for example, a notebook or file) or the contents of an entire directory. If |

## `DELETE` example

Deletes a <code>objects</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.workspace.objects
WHERE deployment_name = '{{ deployment_name }}';
```
