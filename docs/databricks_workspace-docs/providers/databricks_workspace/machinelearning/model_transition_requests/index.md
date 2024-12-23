---
title: model_transition_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - model_transition_requests
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

Operations on a <code>model_transition_requests</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_transition_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_transition_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="activity_type" /> | `string` |
| <CopyableCode code="comment" /> | `string` |
| <CopyableCode code="creation_timestamp" /> | `integer` |
| <CopyableCode code="from_stage" /> | `string` |
| <CopyableCode code="last_updated_timestamp" /> | `integer` |
| <CopyableCode code="system_comment" /> | `string` |
| <CopyableCode code="to_stage" /> | `string` |
| <CopyableCode code="user_id" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listtransitionrequests" /> | `SELECT` | <CopyableCode code="name, version, deployment_name" /> | Gets a list of all open stage transition requests for the model version. |
| <CopyableCode code="createtransitionrequest" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Creates a model version stage transition request. |
| <CopyableCode code="deletetransitionrequest" /> | `DELETE` | <CopyableCode code="creator, name, stage, version, deployment_name" /> | Cancels a model version stage transition request. |
| <CopyableCode code="approvetransitionrequest" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Approves a model version stage transition request. |
| <CopyableCode code="rejecttransitionrequest" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Rejects a model version stage transition request. |
| <CopyableCode code="transitionstage" /> | `EXEC` | <CopyableCode code="deployment_name" /> | Transition a model version's stage. This is a Databricks workspace version of the |

## `SELECT` examples

```sql
SELECT
id,
activity_type,
comment,
creation_timestamp,
from_stage,
last_updated_timestamp,
system_comment,
to_stage,
user_id
FROM databricks_workspace.machinelearning.model_transition_requests
WHERE name = '{{ name }}' AND
version = '{{ version }}' AND
deployment_name = '{{ deployment_name }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>model_transition_requests</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'model_transition_requests', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.machinelearning.model_transition_requests (
deployment_name,
data__name,
data__version,
data__stage,
data__comment
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ version }}',
'{{ stage }}',
'{{ comment }}'
;
```

</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
  - name: name
    value: search_ads_model
  - name: version
    value: '1'
  - name: stage
    value: Staging
  - name: comment
    value: This version is great!

```

</TabItem>
</Tabs>

## `DELETE` example

Deletes a <code>model_transition_requests</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.machinelearning.model_transition_requests
WHERE creator = '{{ creator }}' AND
name = '{{ name }}' AND
stage = '{{ stage }}' AND
version = '{{ version }}' AND
deployment_name = '{{ deployment_name }}';
```
