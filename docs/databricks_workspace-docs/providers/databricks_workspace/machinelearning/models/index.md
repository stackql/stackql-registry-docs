---
title: models
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - models
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

Operations on a <code>models</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>models</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.models" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="description" /> | `string` |
| <CopyableCode code="creation_timestamp" /> | `integer` |
| <CopyableCode code="last_updated_timestamp" /> | `integer` |
| <CopyableCode code="latest_versions" /> | `array` |
| <CopyableCode code="tags" /> | `array` |
| <CopyableCode code="user_id" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getmodel" /> | `SELECT` | <CopyableCode code="name, deployment_name" /> | Get the details of a model. This is a Databricks workspace version of the |
| <CopyableCode code="listmodels" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Lists all available registered models, up to the limit specified in |
| <CopyableCode code="searchmodels" /> | `SELECT` | <CopyableCode code="deployment_name" /> | Search for registered models based on the specified |
| <CopyableCode code="createmodel" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a new registered model with the name specified in the request body. |
| <CopyableCode code="deletemodel" /> | `DELETE` | <CopyableCode code="name, deployment_name" /> | Deletes a registered model. |
| <CopyableCode code="updatemodel" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | Updates a registered model. |
| <CopyableCode code="renamemodel" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Renames a registered model. |

## `SELECT` examples

<Tabs
    defaultValue="listmodels"
    values={[
        { label: 'models (listmodels)', value: 'listmodels' },
        { label: 'models (searchmodels)', value: 'searchmodels' },
        { label: 'models (getmodel)', value: 'getmodel' }
    ]
}>
<TabItem value="listmodels">

```sql
SELECT
name,
description,
creation_timestamp,
last_updated_timestamp,
latest_versions,
tags,
user_id
FROM databricks_workspace.machinelearning.models
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="searchmodels">

```sql
SELECT
name,
description,
creation_timestamp,
last_updated_timestamp,
latest_versions,
tags,
user_id
FROM databricks_workspace.machinelearning.models
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getmodel">

```sql
SELECT
name,
description,
creation_timestamp,
last_updated_timestamp,
latest_versions,
tags,
user_id
FROM databricks_workspace.machinelearning.models
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>models</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'models', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.machinelearning.models (
deployment_name,
data__name,
data__tags,
data__description
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ tags }}',
'{{ description }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: string
  - name: tags
    value:
    - key: string
      value: string
  - name: description
    value: string

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>models</code> resource.

```sql
/*+ update */
UPDATE databricks_workspace.machinelearning.models
SET { field = value }
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>models</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.machinelearning.models
WHERE name = '{{ name }}' AND
deployment_name = '{{ deployment_name }}';
```
