---
title: directories
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - directories
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

Operations on a <code>directories</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.filemanagement.directories" /></td></tr>
</tbody></table>


`SELECT` not supported for this resource, see the methods section for supported operations.
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="createdirectory" /> | `INSERT` | <CopyableCode code="directory_path, deployment_name" /> | Creates an empty directory. If necessary, also creates any parent directories of the new, empty directory (like the shell command |
| <CopyableCode code="deletedirectory" /> | `DELETE` | <CopyableCode code="directory_path, deployment_name" /> | Deletes an empty directory. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>directories</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'directories', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.filemanagement.directories (
directory_path,
deployment_name
)
SELECT 
'{{ directory_path }}',
'{{ deployment_name }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props: []  # No request body parameters required
```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>directories</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.filemanagement.directories
WHERE directory_path = '{{ directory_path }}' AND
deployment_name = '{{ deployment_name }}';
```
