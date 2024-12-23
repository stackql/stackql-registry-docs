---
title: providers
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - providers
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

Operations on a <code>providers</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>providers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.marketplace.providers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="business_contact_email" /> | `string` |
| <CopyableCode code="company_website_link" /> | `string` |
| <CopyableCode code="dark_mode_icon_file_id" /> | `string` |
| <CopyableCode code="dark_mode_icon_file_path" /> | `string` |
| <CopyableCode code="icon_file_id" /> | `string` |
| <CopyableCode code="icon_file_path" /> | `string` |
| <CopyableCode code="is_featured" /> | `boolean` |
| <CopyableCode code="privacy_policy_link" /> | `string` |
| <CopyableCode code="published_by" /> | `string` |
| <CopyableCode code="support_contact_email" /> | `string` |
| <CopyableCode code="term_of_service_link" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="id, deployment_name" /> | Get provider profile |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | List provider profiles for account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Create a provider |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="id, deployment_name" /> | Delete provider |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="id, deployment_name" /> | Update provider profile |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'providers (list)', value: 'list' },
        { label: 'providers (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
name,
description,
business_contact_email,
company_website_link,
dark_mode_icon_file_id,
dark_mode_icon_file_path,
icon_file_id,
icon_file_path,
is_featured,
privacy_policy_link,
published_by,
support_contact_email,
term_of_service_link
FROM databricks_workspace.marketplace.providers
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
name,
description,
business_contact_email,
company_website_link,
dark_mode_icon_file_id,
dark_mode_icon_file_path,
icon_file_id,
icon_file_path,
is_featured,
privacy_policy_link,
published_by,
support_contact_email,
term_of_service_link
FROM databricks_workspace.marketplace.providers
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>providers</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'providers', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.marketplace.providers (
deployment_name,
data__provider
)
SELECT 
'{{ deployment_name }}',
'{{ provider }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: provider
    value:
      id: string
      name: string
      description: string
      icon_file_path: string
      business_contact_email: string
      support_contact_email: string
      is_featured: true
      published_by: string
      company_website_link: string
      icon_file_id: string
      term_of_service_link: string
      privacy_policy_link: string
      dark_mode_icon_file_id: string
      dark_mode_icon_file_path: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>providers</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.marketplace.providers
SET { field = value }
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>providers</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.marketplace.providers
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
