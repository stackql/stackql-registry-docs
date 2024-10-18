---
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
  - resources
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resources.resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="kind" /> | `string` | The kind of the resource. |
| <CopyableCode code="managedBy" /> | `string` | ID of the resource that manages this resource. |
| <CopyableCode code="plan" /> | `object` | Plan for the resource. |
| <CopyableCode code="properties" /> | `object` | The resource properties. |
| <CopyableCode code="sku" /> | `object` | The resource model definition representing SKU |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId" /> | Gets a resource. |
| <CopyableCode code="get_by_id" /> | `SELECT` | <CopyableCode code="api-version, resourceId" /> | Gets a resource by ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all the resources in a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all the resources for a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId" /> | Creates a resource. |
| <CopyableCode code="create_or_update_by_id" /> | `INSERT` | <CopyableCode code="api-version, resourceId" /> | Create a resource by ID. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId" /> | Deletes a resource. |
| <CopyableCode code="delete_by_id" /> | `DELETE` | <CopyableCode code="api-version, resourceId" /> | Deletes a resource by ID. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId" /> | Updates a resource. |
| <CopyableCode code="move_resources" /> | `EXEC` | <CopyableCode code="sourceResourceGroupName, subscriptionId" /> | The resources to be moved must be in the same source resource group in the source subscription being used. The target resource group may be in a different subscription. When moving resources, both the source group and the target group are locked for the duration of the operation. Write and delete operations are blocked on the groups until the move completes. |
| <CopyableCode code="update_by_id" /> | `EXEC` | <CopyableCode code="api-version, resourceId" /> | Updates a resource by ID. |
| <CopyableCode code="validate_move_resources" /> | `EXEC` | <CopyableCode code="sourceResourceGroupName, subscriptionId" /> | This operation checks whether the specified resources can be moved to the target. The resources to be moved must be in the same source resource group in the source subscription being used. The target resource group may be in a different subscription. If validation succeeds, it returns HTTP response code 204 (no content). If validation fails, it returns HTTP response code 409 (Conflict) with an error message. Retrieve the URL in the Location header value to check the result of the long-running operation. |

## `SELECT` examples

Get all the resources in a subscription.


```sql
SELECT
id,
name,
identity,
kind,
managedBy,
plan,
properties,
sku,
type
FROM azure.resources.resources
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resources</code> resource.

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
INSERT INTO azure.resources.resources (
api-version,
resourceId,
plan,
properties,
kind,
managedBy,
sku,
identity
)
SELECT 
'{{ api-version }}',
'{{ resourceId }}',
'{{ plan }}',
'{{ properties }}',
'{{ kind }}',
'{{ managedBy }}',
'{{ sku }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: plan
      value:
        - name: name
          value: string
        - name: publisher
          value: string
        - name: product
          value: string
        - name: promotionCode
          value: string
        - name: version
          value: string
    - name: properties
      value: object
    - name: kind
      value: string
    - name: managedBy
      value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
        - name: size
          value: string
        - name: family
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
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>resources</code> resource.

```sql
/*+ update */
UPDATE azure.resources.resources
SET 
plan = '{{ plan }}',
properties = '{{ properties }}',
kind = '{{ kind }}',
managedBy = '{{ managedBy }}',
sku = '{{ sku }}',
identity = '{{ identity }}'
WHERE 
api-version = '{{ api-version }}'
AND parentResourcePath = '{{ parentResourcePath }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND resourceProviderNamespace = '{{ resourceProviderNamespace }}'
AND resourceType = '{{ resourceType }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>resources</code> resource.

```sql
/*+ delete */
DELETE FROM azure.resources.resources
WHERE api-version = '{{ api-version }}'
AND resourceId = '{{ resourceId }}';
```
