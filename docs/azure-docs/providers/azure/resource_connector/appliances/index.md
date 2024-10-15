---
title: appliances
hide_title: false
hide_table_of_contents: false
keywords:
  - appliances
  - resource_connector
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

Creates, updates, deletes, gets or lists a <code>appliances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>appliances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.resource_connector.appliances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_appliances', value: 'view', },
        { label: 'appliances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="distro" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the resource. |
| <CopyableCode code="infrastructure_config" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties for an appliance. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Gets the details of an Appliance with a specified resource group and name. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets a list of Appliances in the specified subscription and resource group. The operation returns properties of each Appliance. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets a list of Appliances in the specified subscription. The operation returns properties of each Appliance |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Creates or updates an Appliance in the specified Subscription and Resource Group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Deletes an Appliance with the specified Resource Name, Resource Group, and Subscription Id. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Updates an Appliance with the specified Resource Name in the specified Resource Group and Subscription. |

## `SELECT` examples

Gets a list of Appliances in the specified subscription. The operation returns properties of each Appliance

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_appliances', value: 'view', },
        { label: 'appliances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
distro,
identity,
infrastructure_config,
location,
provisioning_state,
public_key,
resourceGroupName,
resourceName,
status,
subscriptionId,
tags,
version
FROM azure.resource_connector.vw_appliances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.resource_connector.appliances
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>appliances</code> resource.

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
INSERT INTO azure.resource_connector.appliances (
resourceGroupName,
resourceName,
subscriptionId,
identity,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ identity }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: string
    - name: properties
      value:
        - name: distro
          value: string
        - name: infrastructureConfig
          value:
            - name: provider
              value: string
        - name: provisioningState
          value: string
        - name: publicKey
          value: string
        - name: status
          value: string
        - name: version
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>appliances</code> resource.

```sql
/*+ update */
UPDATE azure.resource_connector.appliances
SET 
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>appliances</code> resource.

```sql
/*+ delete */
DELETE FROM azure.resource_connector.appliances
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
