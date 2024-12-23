---
title: directories
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - directories
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

Operations on a <code>directories</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>directories</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workspace.directories" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="object_id" /> | `integer` |
| <CopyableCode code="object_type" /> | `string` |
| <CopyableCode code="path" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="path, deployment_name" /> | Lists the contents of a directory, or the object if it is not a directory. If the input path does not exist, this call returns an error |
| <CopyableCode code="mkdirs" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates the specified directory (and necessary parent directories if they do not exist).  If there is an object (not a directory) at any prefix of the input path, this call returns  an error |

## `SELECT` examples

```sql
SELECT
object_id,
object_type,
path
FROM databricks_workspace.workspace.directories
WHERE path = '{{ path }}' AND
deployment_name = '{{ deployment_name }}';
```

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
INSERT INTO databricks_workspace.workspace.directories (
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
    value: /Users/user@example.com/project

```

</TabItem>
</Tabs>
