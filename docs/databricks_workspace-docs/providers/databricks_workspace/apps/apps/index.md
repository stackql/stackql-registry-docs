---
title: apps
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - apps
  - apps
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

Operations on a <code>apps</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.apps.apps" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="active_deployment" /> | `object` |
| <CopyableCode code="app_status" /> | `object` |
| <CopyableCode code="compute_status" /> | `object` |
| <CopyableCode code="create_time" /> | `string` |
| <CopyableCode code="creator" /> | `string` |
| <CopyableCode code="default_source_code_path" /> | `string` |
| <CopyableCode code="pending_deployment" /> | `object` |
| <CopyableCode code="resources" /> | `array` |
| <CopyableCode code="service_principal_client_id" /> | `string` |
| <CopyableCode code="service_principal_id" /> | `integer` |
| <CopyableCode code="service_principal_name" /> | `string` |
| <CopyableCode code="update_time" /> | `string` |
| <CopyableCode code="updater" /> | `string` |
| <CopyableCode code="url" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Retrieves information for the app with the supplied name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Lists all apps in the workspace. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new app. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, deployment_name" /> | Deletes an app. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, deployment_name" /> | Updates the app with the supplied name. |
| <CopyableCode code="deploy" /> | `EXEC` | <CopyableCode code="app_name, deployment_name" /> | Creates an app deployment for the app with the supplied name. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="name, deployment_name" /> | Start the last active deployment of the app in the workspace. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="name, deployment_name" /> | Stops the active deployment of the app in the workspace. |

## `SELECT` examples

<Tabs
    defaultValue="list"
    values={[
        { label: 'apps (list)', value: 'list' },
        { label: 'apps (get)', value: 'get' }
    ]
}>
<TabItem value="list">

```sql
SELECT
name,
description,
active_deployment,
app_status,
compute_status,
create_time,
creator,
default_source_code_path,
pending_deployment,
resources,
service_principal_client_id,
service_principal_id,
service_principal_name,
update_time,
updater,
url
FROM databricks_workspace.apps.apps
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="get">

```sql
SELECT
name,
description,
active_deployment,
app_status,
compute_status,
create_time,
creator,
default_source_code_path,
pending_deployment,
resources,
service_principal_client_id,
service_principal_id,
service_principal_name,
update_time,
updater,
url
FROM databricks_workspace.apps.apps
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>apps</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'apps', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.apps.apps (
deployment_name,
data__name,
data__description,
data__resources
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ description }}',
'{{ resources }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: my-custom-app
  - name: description
    value: My app description.
  - name: resources
    value:
    - name: api-key
      description: API key for external service.
      secret:
        scope: my-scope
        key: my-key
        permission: READ
      sql_warehouse:
        id: e9ca293f79a74b5c
        permission: CAN_MANAGE
      serving_endpoint:
        name: databricks-meta-llama-3-1-70b-instruct
        permission: CAN_MANAGE
      job:
        id: '1234'
        permission: CAN_MANAGE

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>apps</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.apps.apps
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>apps</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.apps.apps
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
