---
title: function_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - function_secrets
  - app_service
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

Creates, updates, deletes, gets or lists a <code>function_secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>function_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.function_secrets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="key" /> | `string` | Secret key. |
| <CopyableCode code="trigger_url" /> | `string` | Trigger URL. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="functionName, name, resourceGroupName, subscriptionId" /> | Description for Get function secrets for a function in a web site, or a deployment slot. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="functionName, keyName, name, resourceGroupName, subscriptionId" /> | Description for Add or update a function secret. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="functionName, keyName, name, resourceGroupName, subscriptionId" /> | Description for Delete a function secret. |

## `SELECT` examples

Description for Get function secrets for a function in a web site, or a deployment slot.


```sql
SELECT
key,
trigger_url
FROM azure.app_service.function_secrets
WHERE functionName = '{{ functionName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>function_secrets</code> resource.

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
INSERT INTO azure.app_service.function_secrets (
functionName,
keyName,
name,
resourceGroupName,
subscriptionId,
name,
value
)
SELECT 
'{{ functionName }}',
'{{ keyName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ name }}',
'{{ value }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: value
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>function_secrets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.function_secrets
WHERE functionName = '{{ functionName }}'
AND keyName = '{{ keyName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
