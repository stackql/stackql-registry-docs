---
title: data_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - data_pools
  - autonomous_dev_platform
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

Creates, updates, deletes, gets or lists a <code>data_pools</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.autonomous_dev_platform.data_pools" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_pools', value: 'view', },
        { label: 'data_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_pool_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="locations" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Data Pool properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, dataPoolName, resourceGroupName, subscriptionId" /> | Gets the properties of a Data Pool |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the data pools under the ADP account |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, dataPoolName, resourceGroupName, subscriptionId" /> | Creates or updates a Data Pool |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, dataPoolName, resourceGroupName, subscriptionId" /> | Deletes a Data Pool |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="accountName, dataPoolName, resourceGroupName, subscriptionId" /> | Updates the properties of an existing Data Pool |

## `SELECT` examples

Lists the data pools under the ADP account

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_pools', value: 'view', },
        { label: 'data_pools', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
dataPoolName,
data_pool_id,
locations,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
tags,
type
FROM azure.autonomous_dev_platform.vw_data_pools
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
FROM azure.autonomous_dev_platform.data_pools
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_pools</code> resource.

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
INSERT INTO azure.autonomous_dev_platform.data_pools (
accountName,
dataPoolName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ dataPoolName }}',
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
        - name: dataPoolId
          value: string
        - name: provisioningState
          value: string
        - name: locations
          value:
            - - name: name
                value: string
              - name: encryption
                value:
                  - name: keyVaultUri
                    value: string
                  - name: keyName
                    value: string
                  - name: keyVersion
                    value: string
                  - name: userAssignedIdentity
                    value: string
              - name: storageSku
                value:
                  - name: name
                    value: string
              - name: storageAccountCount
                value: integer
        - name: tags
          value: []
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

## `UPDATE` example

Updates a <code>data_pools</code> resource.

```sql
/*+ update */
UPDATE azure.autonomous_dev_platform.data_pools
SET 
properties = '{{ properties }}'
WHERE 
accountName = '{{ accountName }}'
AND dataPoolName = '{{ dataPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>data_pools</code> resource.

```sql
/*+ delete */
DELETE FROM azure.autonomous_dev_platform.data_pools
WHERE accountName = '{{ accountName }}'
AND dataPoolName = '{{ dataPoolName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
