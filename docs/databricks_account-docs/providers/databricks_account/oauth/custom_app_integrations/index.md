---
title: custom_app_integrations
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - custom_app_integrations
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

Operations on a <code>custom_app_integrations</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_app_integrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.oauth.custom_app_integrations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="client_id" /> | `string` |
| <CopyableCode code="confidential" /> | `boolean` |
| <CopyableCode code="create_time" /> | `string` |
| <CopyableCode code="created_by" /> | `integer` |
| <CopyableCode code="creator_username" /> | `string` |
| <CopyableCode code="integration_id" /> | `string` |
| <CopyableCode code="redirect_urls" /> | `array` |
| <CopyableCode code="scopes" /> | `array` |
| <CopyableCode code="token_access_policy" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, integration_id" /> | Gets the Custom OAuth App Integration for the given integration id. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Get the list of custom OAuth app integrations for the specified Databricks account |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Create Custom OAuth App Integration. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, integration_id" /> | Delete an existing Custom OAuth App Integration. You can retrieve the custom OAuth app integration via |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="account_id, integration_id" /> | Updates an existing custom OAuth App Integration. You can retrieve the custom OAuth app integration via |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'custom_app_integrations (list)', value: 'list' },
        { label: 'custom_app_integrations (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
name,
client_id,
confidential,
create_time,
created_by,
creator_username,
integration_id,
redirect_urls,
scopes,
token_access_policy
FROM databricks_account.oauth.custom_app_integrations
WHERE account_id = '{{ account_id }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
name,
client_id,
confidential,
create_time,
created_by,
creator_username,
integration_id,
redirect_urls,
scopes,
token_access_policy
FROM databricks_account.oauth.custom_app_integrations
WHERE account_id = '{{ account_id }}' AND
integration_id = '{{ integration_id }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_app_integrations</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'custom_app_integrations', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.oauth.custom_app_integrations (
account_id,
data__summary,
data__value
)
SELECT 
'{{ account_id }}',
'{{ summary }}',
'{{ value }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: summary
    value: Create Tableau Cloud OAuth App Integration
  - name: value
    value:
      name: Example Tableau Server
      scopes:
      - all-apis
      - offline_access
      token_access_policy:
        access_token_ttl_in_minutes: 120
        refresh_token_ttl_in_minutes: 200
      redirect_urls:
      - https://example.online.tableau.com/auth/add_oauth_token
      confidential: true

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>custom_app_integrations</code> resource.

```sql
/*+ update */
UPDATE databricks_account.oauth.custom_app_integrations
SET { field = value }
WHERE account_id = '{{ account_id }}' AND
integration_id = '{{ integration_id }}';
```

## `DELETE` example

Deletes a <code>custom_app_integrations</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.oauth.custom_app_integrations
WHERE account_id = '{{ account_id }}' AND
integration_id = '{{ integration_id }}';
```
