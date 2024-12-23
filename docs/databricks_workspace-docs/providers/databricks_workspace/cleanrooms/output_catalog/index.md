---
title: output_catalog
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - output_catalog
  - cleanrooms
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

Operations on a <code>output_catalog</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>output_catalog</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.cleanrooms.output_catalog" /></td></tr>
</tbody></table>


`SELECT` not supported for this resource, see the methods section for supported operations.
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="createoutputcatalog" /> | `INSERT` | <CopyableCode code="clean_room_name, deployment_name" /> | Create the output catalog of the clean room. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>output_catalog</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'output_catalog', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.cleanrooms.output_catalog (
clean_room_name,
deployment_name,
data__catalog_name
)
SELECT 
'{{ clean_room_name }}',
'{{ deployment_name }}',
'{{ catalog_name }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: catalog_name
    value: string

```

</TabItem>
</Tabs>
