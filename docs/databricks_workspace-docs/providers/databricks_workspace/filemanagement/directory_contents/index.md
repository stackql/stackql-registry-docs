---
title: directory_contents
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - directory_contents
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

Operations on a <code>directory_contents</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directory_contents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.filemanagement.directory_contents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="file_size" /> | `integer` |
| <CopyableCode code="is_directory" /> | `boolean` |
| <CopyableCode code="last_modified" /> | `integer` |
| <CopyableCode code="path" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listdirectorycontents" /> | `SELECT` | <CopyableCode code="directory_path, deployment_name" /> | Returns the contents of a directory. If there is no directory at the specified path, the API returns a HTTP 404 error. |

## `SELECT` examples

```sql
SELECT
name,
file_size,
is_directory,
last_modified,
path
FROM databricks_workspace.filemanagement.directory_contents
WHERE directory_path = '{{ directory_path }}' AND
deployment_name = '{{ deployment_name }}';
```
