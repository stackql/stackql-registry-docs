---
title: hybrid_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_connections
  - relay
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.relay.hybrid_connections" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `` | Properties of the HybridConnection. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hybridConnectionName, namespaceName, resourceGroupName, subscriptionId" /> | Returns the description for the specified hybrid connection. |
| <CopyableCode code="list_by_namespace" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Lists the hybrid connection within the namespace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hybridConnectionName, namespaceName, resourceGroupName, subscriptionId" /> | Creates or updates a service hybrid connection. This operation is idempotent. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hybridConnectionName, namespaceName, resourceGroupName, subscriptionId" /> | Deletes a hybrid connection. |
| <CopyableCode code="regenerate_keys" /> | `EXEC` | <CopyableCode code="authorizationRuleName, hybridConnectionName, namespaceName, resourceGroupName, subscriptionId, data__keyType" /> | Regenerates the primary or secondary connection strings to the hybrid connection. |

## `SELECT` examples

Lists the hybrid connection within the namespace.


```sql
SELECT
id,
name,
location,
properties,
systemData,
type
FROM azure.relay.hybrid_connections
WHERE namespaceName = '{{ namespaceName }}'
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
INSERT INTO azure.relay.hybrid_connections (
hybridConnectionName,
namespaceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ hybridConnectionName }}',
'{{ namespaceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>hybrid_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.relay.hybrid_connections
WHERE hybridConnectionName = '{{ hybridConnectionName }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
