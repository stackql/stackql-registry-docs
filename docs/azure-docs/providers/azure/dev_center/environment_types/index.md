---
title: environment_types
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_types
  - dev_center
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

Creates, updates, deletes, gets or lists a <code>environment_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.environment_types" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_environment_types', value: 'view', },
        { label: 'environment_types', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="devCenterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="environmentTypeName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of an environment type. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="devCenterName, environmentTypeName, resourceGroupName, subscriptionId" /> | Gets an environment type. |
| <CopyableCode code="list_by_dev_center" /> | `SELECT` | <CopyableCode code="devCenterName, resourceGroupName, subscriptionId" /> | Lists environment types for the devcenter. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="devCenterName, environmentTypeName, resourceGroupName, subscriptionId" /> | Creates or updates an environment type. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="devCenterName, environmentTypeName, resourceGroupName, subscriptionId" /> | Deletes an environment type. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="devCenterName, environmentTypeName, resourceGroupName, subscriptionId" /> | Partially updates an environment type. |

## `SELECT` examples

Lists environment types for the devcenter.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_environment_types', value: 'view', },
        { label: 'environment_types', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
devCenterName,
display_name,
environmentTypeName,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
tags,
type
FROM azure.dev_center.vw_environment_types
WHERE devCenterName = '{{ devCenterName }}'
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
tags,
type
FROM azure.dev_center.environment_types
WHERE devCenterName = '{{ devCenterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environment_types</code> resource.

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
INSERT INTO azure.dev_center.environment_types (
devCenterName,
environmentTypeName,
resourceGroupName,
subscriptionId,
properties,
tags
)
SELECT 
'{{ devCenterName }}',
'{{ environmentTypeName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ tags }}'
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
    - name: type
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
    - name: properties
      value:
        - name: displayName
          value: string
        - name: provisioningState
          value: []
    - name: tags
      value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>environment_types</code> resource.

```sql
/*+ update */
UPDATE azure.dev_center.environment_types
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
devCenterName = '{{ devCenterName }}'
AND environmentTypeName = '{{ environmentTypeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>environment_types</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_center.environment_types
WHERE devCenterName = '{{ devCenterName }}'
AND environmentTypeName = '{{ environmentTypeName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
