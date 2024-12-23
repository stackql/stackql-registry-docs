---
title: published_app_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - published_app_integrations
  - oauth
  - databricks_account
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_account/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>published_app_integrations</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>published_app_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.oauth.published_app_integrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="app_id" /> | `string` |
| <CopyableCode code="create_time" /> | `string` |
| <CopyableCode code="created_by" /> | `integer` |
| <CopyableCode code="integration_id" /> | `string` |
| <CopyableCode code="token_access_policy" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, integration_id" /> | Gets the Published OAuth App Integration for the given integration id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Get the list of published OAuth app integrations for the specified Databricks account |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Create Published OAuth App Integration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, integration_id" /> | Delete an existing Published OAuth App Integration. You can retrieve the published OAuth app integration via |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="account_id, integration_id" /> | Updates an existing published OAuth App Integration. You can retrieve the published OAuth app integration via |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'published_app_integrations (list)', value: 'list' },
        { label: 'published_app_integrations (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
name,
app_id,
create_time,
created_by,
integration_id,
token_access_policy
FROM databricks_account.oauth.published_app_integrations
WHERE account_id = '{{ account_id }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
name,
app_id,
create_time,
created_by,
integration_id,
token_access_policy
FROM databricks_account.oauth.published_app_integrations
WHERE account_id = '{{ account_id }}' AND
integration_id = '{{ integration_id }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>published_app_integrations</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'published_app_integrations', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.oauth.published_app_integrations (
account_id,
data__PowerBI,
data__TableauDesktop
)
SELECT 
'{{ account_id }}',
'{{ PowerBI }}',
'{{ TableauDesktop }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: PowerBI
    value:
      summary: Enable PowerBI OAuth Login
      value:
        app_id: power-bi
  - name: TableauDesktop
    value:
      summary: Enable Tableau Desktop OAuth Login
      value:
        app_id: tableau-desktop

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>published_app_integrations</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_account.oauth.published_app_integrations
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE account_id = '{{ account_id }}' AND
integration_id = '{{ integration_id }}';
```

## `DELETE` example

Deletes a <code>published_app_integrations</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.oauth.published_app_integrations
WHERE account_id = '{{ account_id }}' AND
integration_id = '{{ integration_id }}';
```
