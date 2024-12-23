---
title: dbfs_objects
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - dbfs_objects
  - filemanagement
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

Operations on a <code>dbfs_objects</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dbfs_objects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.filemanagement.dbfs_objects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="file_size" /> | `integer` |
| <CopyableCode code="is_dir" /> | `boolean` |
| <CopyableCode code="modification_time" /> | `integer` |
| <CopyableCode code="path" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getstatus" /> | `SELECT` | <CopyableCode code="path, deployment_name" /> | Gets the file information for a file or directory. If the file or directory does not exist, this call throws an exception with |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Delete the file or directory (optionally recursively delete all files in the directory). This call throws an exception with |

## `SELECT` examples

```sql
SELECT
file_size,
is_dir,
modification_time,
path
FROM databricks_workspace.filemanagement.dbfs_objects
WHERE path = '{{ path }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>dbfs_objects</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.filemanagement.dbfs_objects
WHERE deployment_name = '{{ deployment_name }}';
```
