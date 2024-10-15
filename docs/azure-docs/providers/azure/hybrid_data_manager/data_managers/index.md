---
title: data_managers
hide_title: false
hide_table_of_contents: false
keywords:
  - data_managers
  - hybrid_data_manager
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

Creates, updates, deletes, gets or lists a <code>data_managers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_managers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_data_manager.data_managers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Resource Id. |
| <CopyableCode code="name" /> | `string` | The Resource Name. |
| <CopyableCode code="etag" /> | `string` | Etag of the Resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. This will be one of the supported and registered Azure Geo Regions (e.g. West US, East
US, Southeast Asia, etc.). The geo region of a resource cannot be changed once it is created, but if an identical geo
region is specified on update the request will succeed. |
| <CopyableCode code="sku" /> | `object` | The sku type. |
| <CopyableCode code="tags" /> | `object` | The list of key value pairs that describe the resource. These tags can be used in viewing and grouping this resource
(across resource groups). |
| <CopyableCode code="type" /> | `string` | The Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | Gets information about the specified data manager resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the data manager resources available under the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the data manager resources available under the given resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | Creates a new data manager resource with the specified parameters. Existing resources cannot be updated with this API
and should instead be updated with the Update data manager resource API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | Deletes a data manager resource in Microsoft Azure. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dataManagerName, resourceGroupName, subscriptionId" /> | Updates the properties of an existing data manager resource. |

## `SELECT` examples

Lists all the data manager resources available under the subscription.


```sql
SELECT
id,
name,
etag,
location,
sku,
tags,
type
FROM azure.hybrid_data_manager.data_managers
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_managers</code> resource.

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
INSERT INTO azure.hybrid_data_manager.data_managers (
dataManagerName,
resourceGroupName,
subscriptionId,
location,
tags,
sku,
etag
)
SELECT 
'{{ dataManagerName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ sku }}',
'{{ etag }}'
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
    - name: tags
      value: object
    - name: sku
      value:
        - name: name
          value: string
        - name: tier
          value: string
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>data_managers</code> resource.

```sql
/*+ update */
UPDATE azure.hybrid_data_manager.data_managers
SET 
sku = '{{ sku }}',
tags = '{{ tags }}'
WHERE 
dataManagerName = '{{ dataManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>data_managers</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_data_manager.data_managers
WHERE dataManagerName = '{{ dataManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
