---
title: associations
hide_title: false
hide_table_of_contents: false
keywords:
  - associations
  - custom_providers
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

Creates, updates, deletes, gets or lists a <code>associations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.custom_providers.associations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The association id. |
| <CopyableCode code="name" /> | `string` | The association name. |
| <CopyableCode code="properties" /> | `object` | The properties of the association. |
| <CopyableCode code="type" /> | `string` | The association type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="associationName, scope" /> | Get an association. |
| <CopyableCode code="list_all" /> | `SELECT` | <CopyableCode code="scope" /> | Gets all association for the given scope. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="associationName, scope" /> | Create or update an association. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="associationName, scope" /> | Delete an association. |

## `SELECT` examples

Gets all association for the given scope.


```sql
SELECT
id,
name,
properties,
type
FROM azure.custom_providers.associations
WHERE scope = '{{ scope }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>associations</code> resource.

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
INSERT INTO azure.custom_providers.associations (
associationName,
scope,
properties
)
SELECT 
'{{ associationName }}',
'{{ scope }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: targetResourceId
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>associations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.custom_providers.associations
WHERE associationName = '{{ associationName }}'
AND scope = '{{ scope }}';
```
