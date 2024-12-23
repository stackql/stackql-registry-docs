---
title: dbfs_directories
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - dbfs_directories
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

Operations on a <code>dbfs_directories</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dbfs_directories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.filemanagement.dbfs_directories" /></td></tr>
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
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="path, deployment_name" /> | List the contents of a directory, or details of the file. If the file or directory does not exist, this call throws an exception with |
| <CopyableCode code="mkdirs" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates the given directory and necessary parent directories if they do not exist. If a file (not a directory) exists at any prefix of the input path, this call throws an exception with |

## `SELECT` examples

```sql
SELECT
file_size,
is_dir,
modification_time,
path
FROM databricks_workspace.filemanagement.dbfs_directories
WHERE path = '{{ path }}' AND
deployment_name = '{{ deployment_name }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dbfs_directories</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'dbfs_directories', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.filemanagement.dbfs_directories (
deployment_name,
data__path
)
SELECT 
'{{ deployment_name }}',
'{{ path }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: path
    value: /mnt/foo

```

</TabItem>
</Tabs>
