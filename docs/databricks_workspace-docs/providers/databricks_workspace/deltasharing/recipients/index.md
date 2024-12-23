---
title: recipients
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - recipients
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

Operations on a <code>recipients</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>recipients</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.deltasharing.recipients" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="activated" /> | `boolean` |
| <CopyableCode code="activation_url" /> | `string` |
| <CopyableCode code="authentication_type" /> | `string` |
| <CopyableCode code="cloud" /> | `string` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="created_at" /> | `integer` |
| <CopyableCode code="created_by" /> | `string` |
| <CopyableCode code="data_recipient_global_metastore_id" /> | `string` |
| <CopyableCode code="ip_access_list" /> | `object` |
| <CopyableCode code="metastore_id" /> | `string` |
| <CopyableCode code="owner" /> | `string` |
| <CopyableCode code="properties_kvpairs" /> | `object` |
| <CopyableCode code="region" /> | `string` |
| <CopyableCode code="sharing_code" /> | `string` |
| <CopyableCode code="tokens" /> | `array` |
| <CopyableCode code="updated_at" /> | `integer` |
| <CopyableCode code="updated_by" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Gets a share recipient from the metastore if: |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets an array of all share recipients within the current metastore where: |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new recipient with the delta sharing authentication type in the metastore. The caller must be a metastore admin or has the |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, deployment_name" /> | Deletes the specified recipient from the metastore. The caller must be the owner of the recipient. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, deployment_name" /> | Updates an existing recipient in the metastore. The caller must be a metastore admin or the owner of the recipient. If the recipient name will be updated, the user must be both a metastore admin and the owner of the recipient. |
| <CopyableCode code="rotatetoken" /> | `EXEC` | <CopyableCode code="name, deployment_name" /> | Refreshes the specified recipient's delta sharing authentication token with the provided token info. The caller must be the owner of the recipient. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'recipients (list)', value: 'list' },
        { label: 'recipients (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
name,
activated,
activation_url,
authentication_type,
cloud,
comment,
created_at,
created_by,
data_recipient_global_metastore_id,
ip_access_list,
metastore_id,
owner,
properties_kvpairs,
region,
sharing_code,
tokens,
updated_at,
updated_by
FROM databricks_workspace.deltasharing.recipients
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
name,
activated,
activation_url,
authentication_type,
cloud,
comment,
created_at,
created_by,
data_recipient_global_metastore_id,
ip_access_list,
metastore_id,
owner,
properties_kvpairs,
region,
sharing_code,
tokens,
updated_at,
updated_by
FROM databricks_workspace.deltasharing.recipients
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>recipients</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'recipients', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.deltasharing.recipients (
deployment_name,
data__name,
data__authentication_type,
data__owner,
data__comment,
data__ip_access_list,
data__properties_kvpairs,
data__data_recipient_global_metastore_id,
data__sharing_code,
data__expiration_time
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ authentication_type }}',
'{{ owner }}',
'{{ comment }}',
'{{ ip_access_list }}',
'{{ properties_kvpairs }}',
'{{ data_recipient_global_metastore_id }}',
'{{ sharing_code }}',
'{{ expiration_time }}'
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
  - name: owner
    value: string
  - name: comment
    value: string
  - name: ip_access_list
    value:
      allowed_ip_addresses:
      - string
  - name: properties_kvpairs
    value:
      properties:
        property1: string
        property2: string
  - name: data_recipient_global_metastore_id
    value: string
  - name: sharing_code
    value: string
  - name: expiration_time
    value: 0

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>recipients</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.deltasharing.recipients
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>recipients</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.deltasharing.recipients
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
