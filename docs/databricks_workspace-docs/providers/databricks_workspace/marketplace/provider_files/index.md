---
title: provider_files
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - provider_files
  - marketplace
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

Operations on a <code>provider_files</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provider_files</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.provider_files" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="display_name" /> | `string` |
| <CopyableCode code="download_link" /> | `string` |
| <CopyableCode code="file_parent" /> | `object` |
| <CopyableCode code="marketplace_file_type" /> | `string` |
| <CopyableCode code="mime_type" /> | `string` |
| <CopyableCode code="status" /> | `string` |
| <CopyableCode code="status_message" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="file_id, deployment_name" /> | Get a file |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | List files attached to a parent entity. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Create a file. Currently, only provider icons and attached notebooks are supported. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="file_id, deployment_name" /> | Delete a file |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'provider_files (list)', value: 'list' },
        { label: 'provider_files (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
created_at,
display_name,
download_link,
file_parent,
marketplace_file_type,
mime_type,
status,
status_message,
updated_at
FROM databricks_workspace.marketplace.provider_files
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
created_at,
display_name,
download_link,
file_parent,
marketplace_file_type,
mime_type,
status,
status_message,
updated_at
FROM databricks_workspace.marketplace.provider_files
WHERE file_id = '{{ file_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>provider_files</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'provider_files', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.marketplace.provider_files (
deployment_name,
data__file_parent,
data__marketplace_file_type,
data__mime_type,
data__display_name
)
SELECT 
'{{ deployment_name }}',
'{{ file_parent }}',
'{{ marketplace_file_type }}',
'{{ mime_type }}',
'{{ display_name }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: file_parent
    value:
      parent_id: string
      file_parent_type: PROVIDER
  - name: marketplace_file_type
    value: PROVIDER_ICON
  - name: mime_type
    value: string
  - name: display_name
    value: string

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>provider_files</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.marketplace.provider_files
WHERE file_id = '{{ file_id }}' AND
deployment_name = '{{ deployment_name }}';
```
