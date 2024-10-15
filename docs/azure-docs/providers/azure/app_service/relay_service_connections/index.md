---
title: relay_service_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - relay_service_connections
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

Creates, updates, deletes, gets or lists a <code>relay_service_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>relay_service_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.relay_service_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | RelayServiceConnectionEntity resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="entityName, name, resourceGroupName, subscriptionId" /> | Description for Gets a hybrid connection configuration by its name. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Gets hybrid connections configured for an app (or deployment slot, if specified). |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="entityName, name, resourceGroupName, subscriptionId" /> | Description for Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH). |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="entityName, name, resourceGroupName, subscriptionId" /> | Description for Deletes a relay service connection by its name. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="entityName, name, resourceGroupName, subscriptionId" /> | Description for Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH). |

## `SELECT` examples

Description for Gets hybrid connections configured for an app (or deployment slot, if specified).


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.relay_service_connections
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>relay_service_connections</code> resource.

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
INSERT INTO azure.app_service.relay_service_connections (
entityName,
name,
resourceGroupName,
subscriptionId,
kind,
properties
)
SELECT 
'{{ entityName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ kind }}',
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
    - name: kind
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: entityName
          value: string
        - name: entityConnectionString
          value: string
        - name: resourceType
          value: string
        - name: resourceConnectionString
          value: string
        - name: hostname
          value: string
        - name: port
          value: integer
        - name: biztalkUri
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>relay_service_connections</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.relay_service_connections
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
entityName = '{{ entityName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>relay_service_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.relay_service_connections
WHERE entityName = '{{ entityName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
