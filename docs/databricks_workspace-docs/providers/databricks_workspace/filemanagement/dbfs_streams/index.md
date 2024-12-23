---
title: dbfs_streams
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - dbfs_streams
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

Operations on a <code>dbfs_streams</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dbfs_streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.filemanagement.dbfs_streams" /></td></tr>
</tbody></table>


`SELECT` not supported for this resource, see the methods section for supported operations.
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Opens a stream to write to a file and returns a handle to this stream. There is a 10 minute idle timeout on this handle. If a file or directory already exists on the given path and |
| <CopyableCode code="close" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Closes the stream specified by the input handle. If the handle does not exist, this call throws an exception with |
| <CopyableCode code="addblock" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Appends a block of data to the stream specified by the input handle. If the handle does not exist, this call will throw an exception with |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dbfs_streams</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'dbfs_streams', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.filemanagement.dbfs_streams (
deployment_name,
data__path,
data__overwrite
)
SELECT 
'{{ deployment_name }}',
'{{ path }}',
'{{ overwrite }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: path
    value: /mnt/foo
  - name: overwrite
    value: false

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>dbfs_streams</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.filemanagement.dbfs_streams
WHERE deployment_name = '{{ deployment_name }}';
```
