---
title: contexts_context_children
hide_title: false
hide_table_of_contents: false
keywords:
  - contexts_context_children
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

Creates, updates, deletes, gets or lists a <code>contexts_context_children</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contexts_context_children</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.aiplatform.contexts_context_children" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="add_context_children" /> | `INSERT` | <CopyableCode code="contextsId, locationsId, metadataStoresId, projectsId" /> | Adds a set of Contexts as children to a parent Context. If any of the child Contexts have already been added to the parent Context, they are simply skipped. If this call would create a cycle or cause any Context to have more than 10 parents, the request will fail with an INVALID_ARGUMENT error. |
| <CopyableCode code="remove_context_children" /> | `DELETE` | <CopyableCode code="contextsId, locationsId, metadataStoresId, projectsId" /> | Remove a set of children contexts from a parent Context. If any of the child Contexts were NOT added to the parent Context, they are simply skipped. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>contexts_context_children</code> resource.

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
INSERT INTO google.aiplatform.contexts_context_children (
contextsId,
locationsId,
metadataStoresId,
projectsId,
childContexts
)
SELECT 
'{{ contextsId }}',
'{{ locationsId }}',
'{{ metadataStoresId }}',
'{{ projectsId }}',
'{{ childContexts }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: childContexts
      value: '{{ childContexts }}'

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>contexts_context_children</code> resource.

```sql
/*+ delete */
DELETE FROM google.aiplatform.contexts_context_children
WHERE contextsId = '{{ contextsId }}'
AND locationsId = '{{ locationsId }}'
AND metadataStoresId = '{{ metadataStoresId }}'
AND projectsId = '{{ projectsId }}';
```
