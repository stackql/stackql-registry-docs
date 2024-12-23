---
title: dbfs_files
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - dbfs_files
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

Operations on a <code>dbfs_files</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dbfs_files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.filemanagement.dbfs_files" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="bytes_read" /> | `integer` |
| <CopyableCode code="data" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="read" /> | `SELECT` | <CopyableCode code="path, deployment_name" /> | Returns the contents of a file. If the file does not exist, this call throws an exception with |
| <CopyableCode code="move" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Moves a file from one location to another location within DBFS. If the source file does not exist, this call throws an exception with |
| <CopyableCode code="put" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Uploads a file through the use of multipart form post. It is mainly used for streaming uploads, but can also be used as a convenient single call for data upload. |

## `SELECT` examples

```sql
SELECT
bytes_read,
data
FROM databricks_workspace.filemanagement.dbfs_files
WHERE path = '{{ path }}' AND
deployment_name = '{{ deployment_name }}';
```
