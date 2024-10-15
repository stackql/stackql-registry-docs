---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - event_hubs
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

Creates, updates, deletes, gets or lists a <code>namespaces</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_hubs.namespaces" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Properties to configure Identity for Bring your Own Keys |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `` | Namespace properties supplied for create namespace operation. |
| <CopyableCode code="sku" /> | `object` | SKU parameters supplied to the create namespace operation |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Gets the description of the specified namespace. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the available Namespaces within a subscription, irrespective of the resource groups. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists the available Namespaces within a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Creates or updates a namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Deletes an existing namespace. This operation also removes all associated resources under the namespace. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId" /> | Creates or updates a namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name" /> | Check the give Namespace name availability. |
| <CopyableCode code="regenerate_keys" /> | `EXEC` | <CopyableCode code="authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, data__keyType" /> | Regenerates the primary or secondary connection strings for the specified Namespace. |

## `SELECT` examples

Lists all the available Namespaces within a subscription, irrespective of the resource groups.


```sql
SELECT
identity,
location,
properties,
sku,
systemData,
tags
FROM azure.event_hubs.namespaces
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>namespaces</code> resource.

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
INSERT INTO azure.event_hubs.namespaces (
namespaceName,
resourceGroupName,
subscriptionId,
sku,
identity,
properties,
location,
tags
)
SELECT 
'{{ namespaceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ sku }}',
'{{ identity }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: capacity
          value: integer
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
        - name: userAssignedIdentities
          value: object
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
    - name: properties
      value: string
    - name: location
      value: string
    - name: tags
      value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>namespaces</code> resource.

```sql
/*+ update */
UPDATE azure.event_hubs.namespaces
SET 
sku = '{{ sku }}',
identity = '{{ identity }}',
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>namespaces</code> resource.

```sql
/*+ delete */
DELETE FROM azure.event_hubs.namespaces
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
