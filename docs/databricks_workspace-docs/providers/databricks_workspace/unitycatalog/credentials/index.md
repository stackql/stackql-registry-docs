---
title: credentials
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - credentials
  - unitycatalog
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

Operations on a <code>credentials</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>credentials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.credentials" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="aws_temp_credentials" /> | `object` |
| <CopyableCode code="expiration_time" /> | `integer` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="generatetemporaryservicecredential" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Returns a set of temporary credentials generated using the specified service credential. The caller must be a metastore admin or have the metastore privilege |
| <CopyableCode code="getcredential" /> | `SELECT` | <CopyableCode code="name_arg, deployment_name" /> | Gets a service or storage credential from the metastore. The caller must be a metastore admin, the owner of the credential, or have any permission on the credential. |
| <CopyableCode code="listcredentials" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Gets an array of credentials (as |
| <CopyableCode code="createcredential" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new credential. The type of credential to be created is determined by the |
| <CopyableCode code="deletecredential" /> | `DELETE` | <CopyableCode code="name_arg, deployment_name" /> | Deletes a service or storage credential from the metastore. The caller must be an owner of the credential. |
| <CopyableCode code="updatecredential" /> | `UPDATE` | <CopyableCode code="name_arg, deployment_name" /> | Updates a service or storage credential on the metastore. |

## `SELECT` examples

<Tabs
    defaultValue="generatetemporaryservicecredential"
    values={[
        { label: 'credentials (generatetemporaryservicecredential)', value: 'generatetemporaryservicecredential' },
        { label: 'credentials (listcredentials)', value: 'listcredentials' },
        { label: 'credentials (getcredential)', value: 'getcredential' }
    ]
}>
<TabItem value="generatetemporaryservicecredential">

```sql
SELECT
aws_temp_credentials,
expiration_time
FROM databricks_workspace.unitycatalog.credentials
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="listcredentials">

```sql
SELECT
aws_temp_credentials,
expiration_time
FROM databricks_workspace.unitycatalog.credentials
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getcredential">

```sql
SELECT
aws_temp_credentials,
expiration_time
FROM databricks_workspace.unitycatalog.credentials
WHERE name_arg = '{{ name_arg }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>credentials</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'credentials', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.unitycatalog.credentials (
deployment_name,
data__name,
data__aws_iam_role,
data__comment,
data__read_only,
data__purpose,
data__skip_validation
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ aws_iam_role }}',
'{{ comment }}',
'{{ read_only }}',
'{{ purpose }}',
'{{ skip_validation }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: string
  - name: aws_iam_role
    value:
      role_arn: string
      unity_catalog_iam_arn: string
      external_id: string
  - name: comment
    value: string
  - name: read_only
    value: true
  - name: purpose
    value: STORAGE
  - name: skip_validation
    value: false

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>credentials</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.unitycatalog.credentials
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE name_arg = '{{ name_arg }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>credentials</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.unitycatalog.credentials
WHERE name_arg = '{{ name_arg }}' AND
deployment_name = '{{ deployment_name }}';
```
