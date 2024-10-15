---
title: host_secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - host_secrets
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

Creates, updates, deletes, gets or lists a <code>host_secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>host_secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.host_secrets" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="keyName, keyType, name, resourceGroupName, subscriptionId" /> | Description for Add or update a host level secret. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="keyName, keyType, name, resourceGroupName, subscriptionId" /> | Description for Delete a host level secret. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>host_secrets</code> resource.

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
INSERT INTO azure.app_service.host_secrets (
keyName,
keyType,
name,
resourceGroupName,
subscriptionId,
name,
value
)
SELECT 
'{{ keyName }}',
'{{ keyType }}',
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

Deletes the specified <code>host_secrets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.host_secrets
WHERE keyName = '{{ keyName }}'
AND keyType = '{{ keyType }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
