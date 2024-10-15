---
title: hybrid_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_connections
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

Creates, updates, deletes, gets or lists a <code>hybrid_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hybrid_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_service.hybrid_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource Name. |
| <CopyableCode code="kind" /> | `string` | Kind of resource. |
| <CopyableCode code="properties" /> | `object` | HybridConnection resource specific properties |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, namespaceName, relayName, resourceGroupName, subscriptionId" /> | Description for Retrieves a specific Service Bus Hybrid Connection used by this Web App. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Description for Retrieves all Service Bus Hybrid Connections used by this Web App. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, namespaceName, relayName, resourceGroupName, subscriptionId" /> | Description for Creates a new Hybrid Connection using a Service Bus relay. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, namespaceName, relayName, resourceGroupName, subscriptionId" /> | Description for Removes a Hybrid Connection from this site. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, namespaceName, relayName, resourceGroupName, subscriptionId" /> | Description for Creates a new Hybrid Connection using a Service Bus relay. |

## `SELECT` examples

Description for Retrieves all Service Bus Hybrid Connections used by this Web App.


```sql
SELECT
id,
name,
kind,
properties,
type
FROM azure.app_service.hybrid_connections
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hybrid_connections</code> resource.

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
INSERT INTO azure.app_service.hybrid_connections (
name,
namespaceName,
relayName,
resourceGroupName,
subscriptionId,
kind,
properties
)
SELECT 
'{{ name }}',
'{{ namespaceName }}',
'{{ relayName }}',
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
        - name: serviceBusNamespace
          value: string
        - name: relayName
          value: string
        - name: relayArmUri
          value: string
        - name: hostname
          value: string
        - name: port
          value: integer
        - name: sendKeyName
          value: string
        - name: sendKeyValue
          value: string
        - name: serviceBusSuffix
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>hybrid_connections</code> resource.

```sql
/*+ update */
UPDATE azure.app_service.hybrid_connections
SET 
kind = '{{ kind }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}'
AND namespaceName = '{{ namespaceName }}'
AND relayName = '{{ relayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>hybrid_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_service.hybrid_connections
WHERE name = '{{ name }}'
AND namespaceName = '{{ namespaceName }}'
AND relayName = '{{ relayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
