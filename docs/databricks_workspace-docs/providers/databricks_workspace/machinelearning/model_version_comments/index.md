---
title: model_version_comments
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - model_version_comments
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

Operations on a <code>model_version_comments</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>model_version_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.machinelearning.model_version_comments" /></td></tr>
</tbody></table>


`SELECT` not supported for this resource, see the methods section for supported operations.
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="createcomment" /> | `INSERT` | <CopyableCode code="deployment_name" /> | Posts a comment on a model version. A comment can be submitted either by a user or programmatically to display relevant information about the model. For example, test results or deployment errors. |
| <CopyableCode code="deletecomment" /> | `DELETE` | <CopyableCode code="id, deployment_name" /> | Deletes a comment on a model version. |
| <CopyableCode code="updatecomment" /> | `UPDATE` | <CopyableCode code="deployment_name" /> | Post an edit to a comment on a model version. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>model_version_comments</code> resource.

<Tabs
    defaultValue="create"
    values={[
        { label: 'model_version_comments', value: 'create', },
        { label: 'Manifest', value: 'manifest', },
    ]}
>
<TabItem value="create">

```sql
/*+ create */
INSERT INTO databricks_workspace.machinelearning.model_version_comments (
deployment_name,
data__name,
data__version,
data__comment
)
SELECT 
'{{ deployment_name }}',
'{{ name }}',
'{{ version }}',
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
  - name: comment
    value: This version is great!

```

</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>model_version_comments</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update        
UPDATE databricks_workspace.machinelearning.model_version_comments
SET field1 = '{{ value1 }}',
field2 = '{{ value2 }}', ...
WHERE deployment_name = '{{ deployment_name }}';
```

## `DELETE` example

Deletes a <code>model_version_comments</code> resource.

```sql
/*+ delete */
DELETE FROM databricks_workspace.machinelearning.model_version_comments
WHERE id = '{{ id }}' AND
deployment_name = '{{ deployment_name }}';
```
