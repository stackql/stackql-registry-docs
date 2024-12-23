---
title: service_principals
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - service_principals
  - iam
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

Operations on a <code>service_principals</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_principals</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_account.iam.service_principals" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="active" /> | `boolean` |
| <CopyableCode code="applicationId" /> | `string` |
| <CopyableCode code="displayName" /> | `string` |
| <CopyableCode code="externalId" /> | `string` |
| <CopyableCode code="roles" /> | `array` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="account_id, id" /> | Gets the details for a single service principal define in the Databricks account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="account_id" /> | Gets the set of service principals associated with a Databricks account. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="account_id" /> | Creates a new service principal in the Databricks account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="account_id, id" /> | Delete a single service principal in the Databricks account. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="account_id, id" /> | Partially updates the details of a single service principal in the Databricks account. |
| <CopyableCode code="update" /> | `REPLACE` | <CopyableCode code="account_id, id" /> | Updates the details of a single service principal. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'service_principals (list)', value: 'list' },
        { label: 'service_principals (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
id,
active,
applicationId,
displayName,
externalId,
roles
FROM databricks_account.iam.service_principals
WHERE account_id = '{{ account_id }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
id,
active,
applicationId,
displayName,
externalId,
roles
FROM databricks_account.iam.service_principals
WHERE account_id = '{{ account_id }}' AND
id = '{{ id }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service_principals</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'service_principals', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_account.iam.service_principals (
account_id,
data__applicationId,
data__displayName,
data__roles,
data__externalId,
data__active
)
SELECT 
'{{ account_id }}',
'{{ applicationId }}',
'{{ displayName }}',
'{{ roles }}',
'{{ externalId }}',
'{{ active }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: applicationId
    value: 97ab27fa-30e2-43e3-92a3-160e80f4c0d5
  - name: displayName
    value: etl-service
  - name: roles
    value:
    - $ref: string
      value: string
      display: string
      primary: true
      type: string
  - name: externalId
    value: string
  - name: active
    value: true

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>service_principals</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_account.iam.service_principals
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE account_id = '{{ account_id }}' AND
id = '{{ id }}';
```

## `REPLACE` example

Replaces a <code>service_principals</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_account.iam.service_principals
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE account_id = '{{ account_id }}' AND
id = '{{ id }}';
```

## `DELETE` example

Deletes a <code>service_principals</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_account.iam.service_principals
WHERE account_id = '{{ account_id }}' AND
id = '{{ id }}';
```
