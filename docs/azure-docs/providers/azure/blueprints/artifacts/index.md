---
title: artifacts
hide_title: false
hide_table_of_contents: false
keywords:
  - artifacts
  - blueprints
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

Creates, updates, deletes, gets or lists a <code>artifacts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>artifacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.blueprints.artifacts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | String Id used to locate any resource on Azure. |
| <CopyableCode code="name" /> | `string` | Name of this resource. |
| <CopyableCode code="kind" /> | `string` | Specifies the kind of blueprint artifact. |
| <CopyableCode code="type" /> | `string` | Type of this resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="artifactName, blueprintName, resourceScope" /> | Get a blueprint artifact. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="blueprintName, resourceScope" /> | List artifacts for a given blueprint definition. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="artifactName, blueprintName, resourceScope, data__kind" /> | Create or update blueprint artifact. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="artifactName, blueprintName, resourceScope" /> | Delete a blueprint artifact. |

## `SELECT` examples

List artifacts for a given blueprint definition.


```sql
SELECT
id,
name,
kind,
type
FROM azure.blueprints.artifacts
WHERE blueprintName = '{{ blueprintName }}'
AND resourceScope = '{{ resourceScope }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>artifacts</code> resource.

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
INSERT INTO azure.blueprints.artifacts (
artifactName,
blueprintName,
resourceScope,
data__kind,
kind
)
SELECT 
'{{ artifactName }}',
'{{ blueprintName }}',
'{{ resourceScope }}',
'{{ data__kind }}',
'{{ kind }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: type
      value: string
    - name: name
      value: string
    - name: kind
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>artifacts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.blueprints.artifacts
WHERE artifactName = '{{ artifactName }}'
AND blueprintName = '{{ blueprintName }}'
AND resourceScope = '{{ resourceScope }}';
```
