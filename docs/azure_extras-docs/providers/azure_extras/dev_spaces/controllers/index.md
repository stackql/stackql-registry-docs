---
title: controllers
hide_title: false
hide_table_of_contents: false
keywords:
  - controllers
  - dev_spaces
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

Creates, updates, deletes, gets or lists a <code>controllers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>controllers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.dev_spaces.controllers" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_controllers', value: 'view', },
        { label: 'controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_plane_fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_suffix" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Region where the Azure resource is located. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sku" /> | `text` | Model representing SKU for Azure Dev Spaces Controller. |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Tags for the Azure resource. |
| <CopyableCode code="target_container_host_api_server_fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_container_host_credentials_base64" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_container_host_resource_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | Region where the Azure resource is located. |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="sku" /> | `object` | Model representing SKU for Azure Dev Spaces Controller. |
| <CopyableCode code="tags" /> | `object` | Tags for the Azure resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Gets the properties for an Azure Dev Spaces Controller. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the Azure Dev Spaces Controllers with their properties in the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the Azure Dev Spaces Controllers with their properties in the specified resource group and subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__location, data__properties, data__sku" /> | Creates an Azure Dev Spaces Controller with the specified create parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Deletes an existing Azure Dev Spaces Controller. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Updates the properties of an existing Azure Dev Spaces Controller with the specified update parameters. |

## `SELECT` examples

Lists all the Azure Dev Spaces Controllers with their properties in the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_controllers', value: 'view', },
        { label: 'controllers', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
data_plane_fqdn,
host_suffix,
location,
provisioning_state,
resourceGroupName,
sku,
subscriptionId,
tags,
target_container_host_api_server_fqdn,
target_container_host_credentials_base64,
target_container_host_resource_id
FROM azure_extras.dev_spaces.vw_controllers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
sku,
tags
FROM azure_extras.dev_spaces.controllers
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>controllers</code> resource.

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
INSERT INTO azure_extras.dev_spaces.controllers (
name,
resourceGroupName,
subscriptionId,
data__location,
data__properties,
data__sku,
tags,
location,
properties,
sku
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ data__properties }}',
'{{ data__sku }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ sku }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: hostSuffix
          value: string
        - name: dataPlaneFqdn
          value: string
        - name: targetContainerHostApiServerFqdn
          value: string
        - name: targetContainerHostResourceId
          value: string
        - name: targetContainerHostCredentialsBase64
          value: string
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>controllers</code> resource.

```sql
/*+ update */
UPDATE azure_extras.dev_spaces.controllers
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>controllers</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.dev_spaces.controllers
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
