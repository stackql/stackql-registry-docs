---
title: management_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - management_policies
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

Creates, updates, deletes, gets or lists a <code>management_policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>management_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.management_policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_management_policies', value: 'view', },
        { label: 'management_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="managementPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | The Storage Account ManagementPolicy properties. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, managementPolicyName, resourceGroupName, subscriptionId" /> | Gets the managementpolicy associated with the specified storage account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, managementPolicyName, resourceGroupName, subscriptionId" /> | Sets the managementpolicy to the specified storage account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, managementPolicyName, resourceGroupName, subscriptionId" /> | Deletes the managementpolicy associated with the specified storage account. |

## `SELECT` examples

Gets the managementpolicy associated with the specified storage account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_management_policies', value: 'view', },
        { label: 'management_policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
last_modified_time,
managementPolicyName,
policy,
resourceGroupName,
subscriptionId,
type
FROM azure.storage.vw_management_policies
WHERE accountName = '{{ accountName }}'
AND managementPolicyName = '{{ managementPolicyName }}'
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
type
FROM azure.storage.management_policies
WHERE accountName = '{{ accountName }}'
AND managementPolicyName = '{{ managementPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>management_policies</code> resource.

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
INSERT INTO azure.storage.management_policies (
accountName,
managementPolicyName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ managementPolicyName }}',
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
      value:
        - name: lastModifiedTime
          value: string
        - name: policy
          value:
            - name: rules
              value:
                - - name: enabled
                    value: boolean
                  - name: name
                    value: string
                  - name: type
                    value: string
                  - name: definition
                    value:
                      - name: actions
                        value:
                          - name: baseBlob
                            value:
                              - name: tierToCool
                                value:
                                  - name: daysAfterModificationGreaterThan
                                    value: number
                                  - name: daysAfterLastAccessTimeGreaterThan
                                    value: number
                                  - name: daysAfterLastTierChangeGreaterThan
                                    value: number
                                  - name: daysAfterCreationGreaterThan
                                    value: number
                              - name: enableAutoTierToHotFromCool
                                value: boolean
                          - name: snapshot
                            value:
                              - name: tierToCool
                                value:
                                  - name: daysAfterCreationGreaterThan
                                    value: number
                                  - name: daysAfterLastTierChangeGreaterThan
                                    value: number
                          - name: version
                            value: []
                      - name: filters
                        value:
                          - name: prefixMatch
                            value:
                              - string
                          - name: blobTypes
                            value:
                              - string
                          - name: blobIndexMatch
                            value:
                              - - name: name
                                  value: string
                                - name: op
                                  value: string
                                - name: value
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

Deletes the specified <code>management_policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage.management_policies
WHERE accountName = '{{ accountName }}'
AND managementPolicyName = '{{ managementPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
