---
title: instance_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - instance_profiles
  - compute
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

Operations on a <code>instance_profiles</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>instance_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.instance_profiles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="instance_profile_arn" /> | `string` |
| <CopyableCode code="is_meta_instance_profile" /> | `boolean` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | List the instance profiles that the calling user can use to launch a cluster. |
| <CopyableCode code="add" /> | `INSERT` | <CopyableCode code="deployment_name" /> | In the UI, you can select the instance profile when launching clusters. This API is only available to admin users. |
| <CopyableCode code="remove" /> | `DELETE` | <CopyableCode code="deployment_name" /> | Remove the instance profile with the provided ARN. Existing clusters with this instance profile will continue to function. |
| <CopyableCode code="edit" /> | `REPLACE` | <CopyableCode code="deployment_name" /> | The only supported field to change is the optional IAM role ARN associated with the instance profile. It is required to specify the IAM role ARN if both of the following are true: |

## `SELECT` examples

```sql
SELECT
instance_profile_arn,
is_meta_instance_profile
FROM databricks_workspace.compute.instance_profiles
WHERE deployment_name = '{{ deployment_name }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>instance_profiles</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'instance_profiles', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.compute.instance_profiles (
deployment_name,
data__instance_profile_arn
)
SELECT 
'{{ deployment_name }}',
'{{ instance_profile_arn }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: instance_profile_arn
    value: arn:aws:iam::123456789012:instance-profile/my-profile

```

</TabItem>
</Tabs>

## `REPLACE` example

Replaces a <code>instance_profiles</code> resource.

```sql
/*+ update */
REPLACE databricks_workspace.compute.instance_profiles
SET { field = value }
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>instance_profiles</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.compute.instance_profiles
WHERE deployment_name = '{{ deployment_name }}';
```
