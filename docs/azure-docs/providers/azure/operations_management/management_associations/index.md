---
title: management_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - management_associations
  - operations_management
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

Creates, updates, deletes, gets or lists a <code>management_associations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>management_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.operations_management.management_associations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_management_associations', value: 'view', },
        { label: 'management_associations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="application_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="managementAssociationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="providerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceType" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | ManagementAssociation properties supported by the OperationsManagement resource provider. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="managementAssociationName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId" /> | Retrieves the user ManagementAssociation. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Retrieves the ManagementAssociations list. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="managementAssociationName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId" /> | Creates or updates the ManagementAssociation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="managementAssociationName, providerName, resourceGroupName, resourceName, resourceType, subscriptionId" /> | Deletes the ManagementAssociation in the subscription. |

## `SELECT` examples

Retrieves the ManagementAssociations list.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_management_associations', value: 'view', },
        { label: 'management_associations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
application_id,
location,
managementAssociationName,
providerName,
resourceGroupName,
resourceName,
resourceType,
subscriptionId,
type
FROM azure.operations_management.vw_management_associations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure.operations_management.management_associations
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>management_associations</code> resource.

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
INSERT INTO azure.operations_management.management_associations (
managementAssociationName,
providerName,
resourceGroupName,
resourceName,
resourceType,
subscriptionId,
location,
properties
)
SELECT 
'{{ managementAssociationName }}',
'{{ providerName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ resourceType }}',
'{{ subscriptionId }}',
'{{ location }}',
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
    - name: type
      value: string
    - name: location
      value: string
    - name: properties
      value:
        - name: applicationId
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>management_associations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.operations_management.management_associations
WHERE managementAssociationName = '{{ managementAssociationName }}'
AND providerName = '{{ providerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND resourceType = '{{ resourceType }}'
AND subscriptionId = '{{ subscriptionId }}';
```
