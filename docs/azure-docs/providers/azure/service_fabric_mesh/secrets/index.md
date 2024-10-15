---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
  - service_fabric_mesh
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

Creates, updates, deletes, gets or lists a <code>secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_mesh.secrets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_secrets', value: 'view', },
        { label: 'secrets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secretResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a secret resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, secretResourceName, subscriptionId" /> | Gets the information about the secret resource with the given name. The information include the description and other properties of the secret. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets the information about all secret resources in a given resource group. The information include the description and other properties of the Secret. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets the information about all secret resources in a given resource group. The information include the description and other properties of the secret. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, secretResourceName, subscriptionId, data__properties" /> | Creates a secret resource with the specified name, description and properties. If a secret resource with the same name exists, then it is updated with the specified description and properties. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, secretResourceName, subscriptionId" /> | Deletes the secret resource identified by the name. |

## `SELECT` examples

Gets the information about all secret resources in a given resource group. The information include the description and other properties of the secret.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_secrets', value: 'view', },
        { label: 'secrets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
content_type,
kind,
location,
resourceGroupName,
secretResourceName,
status,
status_details,
subscriptionId,
tags
FROM azure.service_fabric_mesh.vw_secrets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.service_fabric_mesh.secrets
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>secrets</code> resource.

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
INSERT INTO azure.service_fabric_mesh.secrets (
resourceGroupName,
secretResourceName,
subscriptionId,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ secretResourceName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}'
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
        - name: kind
          value: []
        - name: description
          value: string
        - name: status
          value: []
        - name: statusDetails
          value: string
        - name: contentType
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>secrets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_fabric_mesh.secrets
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND secretResourceName = '{{ secretResourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
