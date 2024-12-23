---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - secrets
  - secrets
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

Operations on a <code>secrets</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.secrets.secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="key" /> | `string` |
| <CopyableCode code="last_updated_timestamp" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getsecret" /> | `SELECT` | <CopyableCode code="key, scope, deployment_name" /> | Gets the bytes representation of a secret value for the specified scope and key. |
| <CopyableCode code="listsecrets" /> | `SELECT` | <CopyableCode code="scope, deployment_name" /> | Lists the secret keys that are stored at this scope.  This is a metadata-only operation; secret data cannot be retrieved using this API.  Users need the READ permission to make this call. |
| <CopyableCode code="deletesecret" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Deletes the secret stored in this secret scope.  You must have |
| <CopyableCode code="putsecret" /> | `REPLACE` | <CopyableCode code="deployment_name" /> | Inserts a secret under the provided scope with the given name.  If a secret already exists with the same name, this command overwrites the existing secret's value. The server encrypts the secret using the secret scope's encryption settings before storing it. |

## `SELECT` examples

<Tabs
    defaultValue="listsecrets"
    values={[
        { label: 'secrets (listsecrets)', value: 'listsecrets' },
        { label: 'secrets (getsecret)', value: 'getsecret' }
    ]
}>
<TabItem value="listsecrets">

```sql
SELECT
key,
last_updated_timestamp
FROM databricks_workspace.secrets.secrets
WHERE scope = '{{ scope }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getsecret">

```sql
SELECT
key,
last_updated_timestamp
FROM databricks_workspace.secrets.secrets
WHERE key = '{{ key }}' AND
scope = '{{ scope }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `REPLACE` example

Replaces a <code>secrets</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_workspace.secrets.secrets
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>secrets</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.secrets.secrets
WHERE deployment_name = '{{ deployment_name }}';
```
