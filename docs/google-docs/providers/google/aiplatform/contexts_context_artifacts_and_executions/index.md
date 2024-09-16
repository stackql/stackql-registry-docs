---
title: contexts_context_artifacts_and_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - contexts_context_artifacts_and_executions
  - aiplatform
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>contexts_context_artifacts_and_executions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contexts_context_artifacts_and_executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.contexts_context_artifacts_and_executions" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_context_artifacts_and_executions" /> | `INSERT` | <CopyableCode code="contextsId, locationsId, metadataStoresId, projectsId" /> | Adds a set of Artifacts and Executions to a Context. If any of the Artifacts or Executions have already been added to a Context, they are simply skipped. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>contexts_context_artifacts_and_executions</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.aiplatform.contexts_context_artifacts_and_executions (
contextsId,
locationsId,
metadataStoresId,
projectsId,
artifacts,
executions
)
SELECT 
'{{ contextsId }}',
'{{ locationsId }}',
'{{ metadataStoresId }}',
'{{ projectsId }}',
'{{ artifacts }}',
'{{ executions }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: artifacts
      value:
        - name: type
          value: '{{ type }}'
    - name: executions
      value:
        - name: type
          value: '{{ type }}'

```
</TabItem>
</Tabs>
