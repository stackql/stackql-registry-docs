---
title: providers
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - providers
  - deltasharing
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
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.deltasharing.providers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="authentication_type" /> | `string` |
| <CopyableCode code="cloud" /> | `string` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="data_provider_global_metastore_id" /> | `string` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="owner" /> | `string` |
| <CopyableCode code="recipient_profile" /> | `object` |
| <CopyableCode code="recipient_profile_str" /> | `string` |
| <CopyableCode code="region" /> | `string` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Gets a specific authentication provider. The caller must supply the name of the provider, and must either be a metastore admin or the owner of the provider. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets an array of available authentication providers. The caller must either be a metastore admin or the owner of the providers. Providers not owned by the caller are not included in the response. There is no guarantee of a specific ordering of the elements in the array. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new authentication provider minimally based on a name and authentication type. The caller must be an admin on the metastore. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, deployment_name" /> | Deletes an authentication provider, if the caller is a metastore admin or is the owner of the provider. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, deployment_name" /> | Updates the information for an authentication provider, if the caller is a metastore admin or is the owner of the provider. If the update changes the provider name, the caller must be both a metastore admin and the owner of the provider. |

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
name,
authentication_type,
cloud,
comment,
created_at,
created_by,
data_provider_global_metastore_id,
metastore_id,
owner,
recipient_profile,
recipient_profile_str,
region,
updated_at,
updated_by
FROM databricks_workspace.deltasharing.providers
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
name,
authentication_type,
cloud,
comment,
created_at,
created_by,
data_provider_global_metastore_id,
metastore_id,
owner,
recipient_profile,
recipient_profile_str,
region,
updated_at,
updated_by
FROM databricks_workspace.deltasharing.providers
WHERE name = '{{ name }}' AND
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
INSERT INTO databricks_workspace.deltasharing.providers (
deployment_name,
data__name,
data__authentication_type,
data__comment,
data__recipient_profile_str
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ authentication_type }}',
'{{ comment }}',
'{{ recipient_profile_str }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: string
  - name: authentication_type
    value: TOKEN
  - name: comment
    value: string
  - name: recipient_profile_str
    value: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>providers</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.deltasharing.providers
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>providers</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.deltasharing.providers
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
