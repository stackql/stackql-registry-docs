---
title: model_web_hooks
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - model_web_hooks
  - machinelearning
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

Operations on a <code>model_web_hooks</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_web_hooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_web_hooks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="creation_timestamp" /> | `integer` |
| <CopyableCode code="events" /> | `array` |
| <CopyableCode code="http_url_spec" /> | `object` |
| <CopyableCode code="last_updated_timestamp" /> | `integer` |
| <CopyableCode code="model_name" /> | `string` |
| <CopyableCode code="status" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listwebhooks" /> | `SELECT` | <CopyableCode code="deployment_name" /> | This endpoint is in Public Preview. |
| <CopyableCode code="createwebhook" /> | `INSERT` | <CopyableCode code="deployment_name" /> | : This endpoint is in Public Preview. |
| <CopyableCode code="deletewebhook" /> | `DELETE` | <CopyableCode code="deployment_name" /> | This endpoint is in Public Preview. |
| <CopyableCode code="updatewebhook" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | This endpoint is in Public Preview. |
| <CopyableCode code="testregistrywebhook" /> | `EXEC` | <CopyableCode code="deployment_name" /> | This endpoint is in Public Preview. |

## `SELECT` examples

```sql
SELECT
id,
description,
creation_timestamp,
events,
http_url_spec,
last_updated_timestamp,
model_name,
status
FROM databricks_workspace.machinelearning.model_web_hooks
WHERE deployment_name = '{{ deployment_name }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>model_web_hooks</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'model_web_hooks', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.machinelearning.model_web_hooks (
deployment_name,
data__job_spec,
data__http_url_spec,
data__events,
data__model_name,
data__description,
data__status
)
SELECT 
'{{ deployment_name }}',
'{{ job_spec }}',
'{{ http_url_spec }}',
'{{ events }}',
'{{ model_name }}',
'{{ description }}',
'{{ status }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: job_spec
    value:
      job_id: '1'
      access_token: dapi12345678935845824
      workspace_url: string
  - name: http_url_spec
    value:
      url: https://hooks.slack.com/services/...
      secret: anyRandomString
      enable_ssl_verification: true
      authorization: Bearer <access_token>
  - name: events
    value:
    - MODEL_VERSION_CREATED
    - MODEL_VERSION_TRANSITIONED_TO_STAGING
    - COMMENT_CREATED
  - name: model_name
    value: registered-model-1
  - name: description
    value: Webhook for comment creation
  - name: status
    value: ACTIVE

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>model_web_hooks</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.machinelearning.model_web_hooks
SET { field = value }
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>model_web_hooks</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.machinelearning.model_web_hooks
WHERE deployment_name = '{{ deployment_name }}';
```
