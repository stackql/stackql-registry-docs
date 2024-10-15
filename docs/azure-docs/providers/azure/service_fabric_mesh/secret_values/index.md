---
title: secret_values
hide_title: false
hide_table_of_contents: false
keywords:
  - secret_values
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

Creates, updates, deletes, gets or lists a <code>secret_values</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secret_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_fabric_mesh.secret_values" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_secret_values', value: 'view', },
        { label: 'secret_values', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secretResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secretValueResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="value" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | This type describes properties of a secret value resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, secretResourceName, secretValueResourceName, subscriptionId" /> | Get the information about the specified named secret value resources. The information does not include the actual value of the secret. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, secretResourceName, subscriptionId" /> | Gets information about all secret value resources of the specified secret resource. The information includes the names of the secret value resources, but not the actual values. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, secretResourceName, secretValueResourceName, subscriptionId, data__properties" /> | Creates a new value of the specified secret resource. The name of the value is typically the version identifier. Once created the value cannot be changed. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, secretResourceName, secretValueResourceName, subscriptionId" /> | Deletes the secret value resource identified by the name. The name of the resource is typically the version associated with that value. Deletion will fail if the specified value is in use. |

## `SELECT` examples

Gets information about all secret value resources of the specified secret resource. The information includes the names of the secret value resources, but not the actual values.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_secret_values', value: 'view', },
        { label: 'secret_values', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
location,
provisioning_state,
resourceGroupName,
secretResourceName,
secretValueResourceName,
subscriptionId,
tags,
value
FROM azure.service_fabric_mesh.vw_secret_values
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND secretResourceName = '{{ secretResourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.service_fabric_mesh.secret_values
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND secretResourceName = '{{ secretResourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>secret_values</code> resource.

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
INSERT INTO azure.service_fabric_mesh.secret_values (
resourceGroupName,
secretResourceName,
secretValueResourceName,
subscriptionId,
data__properties,
tags,
location,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ secretResourceName }}',
'{{ secretValueResourceName }}',
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
        - name: provisioningState
          value: string
        - name: value
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>secret_values</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_fabric_mesh.secret_values
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND secretResourceName = '{{ secretResourceName }}'
AND secretValueResourceName = '{{ secretValueResourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
