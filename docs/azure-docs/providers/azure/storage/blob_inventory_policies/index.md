---
title: blob_inventory_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - blob_inventory_policies
  - storage
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

Creates, updates, deletes, gets or lists a <code>blob_inventory_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>blob_inventory_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.blob_inventory_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_blob_inventory_policies', value: 'view', },
        { label: 'blob_inventory_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="blobInventoryPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | The storage account blob inventory policy properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, blobInventoryPolicyName, resourceGroupName, subscriptionId" /> | Gets the blob inventory policy associated with the specified storage account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Gets the blob inventory policy associated with the specified storage account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, blobInventoryPolicyName, resourceGroupName, subscriptionId" /> | Sets the blob inventory policy to the specified storage account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, blobInventoryPolicyName, resourceGroupName, subscriptionId" /> | Deletes the blob inventory policy associated with the specified storage account. |

## `SELECT` examples

Gets the blob inventory policy associated with the specified storage account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_blob_inventory_policies', value: 'view', },
        { label: 'blob_inventory_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
blobInventoryPolicyName,
last_modified_time,
policy,
resourceGroupName,
subscriptionId,
system_data,
type
FROM azure.storage.vw_blob_inventory_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.storage.blob_inventory_policies
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>blob_inventory_policies</code> resource.

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
INSERT INTO azure.storage.blob_inventory_policies (
accountName,
blobInventoryPolicyName,
resourceGroupName,
subscriptionId,
properties,
systemData
)
SELECT 
'{{ accountName }}',
'{{ blobInventoryPolicyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ systemData }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: lastModifiedTime
          value: string
        - name: policy
          value:
            - name: enabled
              value: boolean
            - name: destination
              value: string
            - name: type
              value: string
            - name: rules
              value:
                - - name: enabled
                    value: boolean
                  - name: name
                    value: string
                  - name: destination
                    value: string
                  - name: definition
                    value:
                      - name: filters
                        value:
                          - name: prefixMatch
                            value:
                              - string
                          - name: excludePrefix
                            value:
                              - string
                          - name: blobTypes
                            value:
                              - string
                          - name: includeBlobVersions
                            value: boolean
                          - name: includeSnapshots
                            value: boolean
                          - name: includeDeleted
                            value: boolean
                          - name: creationTime
                            value:
                              - name: lastNDays
                                value: integer
                      - name: format
                        value: string
                      - name: schedule
                        value: string
                      - name: objectType
                        value: string
                      - name: schemaFields
                        value:
                          - string
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

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>blob_inventory_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage.blob_inventory_policies
WHERE accountName = '{{ accountName }}'
AND blobInventoryPolicyName = '{{ blobInventoryPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
