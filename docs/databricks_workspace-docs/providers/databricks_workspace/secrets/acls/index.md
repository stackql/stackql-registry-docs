---
title: acls
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - acls
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

Operations on a <code>acls</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>acls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.secrets.acls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="permission" /> | `string` |
| <CopyableCode code="principal" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getacl" /> | `SELECT` | <CopyableCode code="principal, scope, deployment_name" /> | Gets the details about the given ACL, such as the group and permission. Users must have the |
| <CopyableCode code="listacls" /> | `SELECT` | <CopyableCode code="scope, deployment_name" /> | List the ACLs for a given secret scope. Users must have the |
| <CopyableCode code="deleteacl" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Deletes the given ACL on the given scope. |
| <CopyableCode code="putacl" /> | `REPLACE` | <CopyableCode code="deployment_name" /> | Creates or overwrites the Access Control List (ACL) associated with the given principal (user or group) on the specified scope point. |

## `SELECT` examples

<Tabs
    defaultValue="listacls"
    values={[
        { label: 'acls (listacls)', value: 'listacls' },
        { label: 'acls (getacl)', value: 'getacl' }
    ]
}>
<TabItem value="listacls">

```sql
SELECT
permission,
principal
FROM databricks_workspace.secrets.acls
WHERE scope = '{{ scope }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getacl">

```sql
SELECT
permission,
principal
FROM databricks_workspace.secrets.acls
WHERE principal = '{{ principal }}' AND
scope = '{{ scope }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `REPLACE` example

Replaces a <code>acls</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_workspace.secrets.acls
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>acls</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.secrets.acls
WHERE deployment_name = '{{ deployment_name }}';
```
