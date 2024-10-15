---
title: data_collection_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - data_collection_endpoints
  - monitor
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

Creates, updates, deletes, gets or lists a <code>data_collection_endpoints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_collection_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.monitor.data_collection_endpoints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified ID of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="etag" /> | `string` | Resource entity tag (ETag). |
| <CopyableCode code="identity" /> | `object` | Managed service identity of the resource. |
| <CopyableCode code="kind" /> | `string` | The kind of the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives. |
| <CopyableCode code="properties" /> | `object` | Resource properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataCollectionEndpointName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> |  |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="dataCollectionEndpointName, resourceGroupName, subscriptionId, data__location" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataCollectionEndpointName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dataCollectionEndpointName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="reconcile_nsp" /> | `EXEC` | <CopyableCode code="dataCollectionEndpointName, networkSecurityPerimeterConfigurationName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
id,
name,
etag,
identity,
kind,
location,
properties,
systemData,
tags,
type
FROM azure.monitor.data_collection_endpoints
WHERE subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_collection_endpoints</code> resource.

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
INSERT INTO azure.monitor.data_collection_endpoints (
dataCollectionEndpointName,
resourceGroupName,
subscriptionId,
data__location,
properties,
location,
tags,
kind,
identity
)
SELECT 
'{{ dataCollectionEndpointName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}',
'{{ kind }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value: string
    - name: location
      value: string
    - name: tags
      value: object
    - name: kind
      value: string
    - name: identity
      value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: etag
      value: string
    - name: systemData
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>data_collection_endpoints</code> resource.

```sql
/*+ update */
UPDATE azure.monitor.data_collection_endpoints
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
dataCollectionEndpointName = '{{ dataCollectionEndpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>data_collection_endpoints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.monitor.data_collection_endpoints
WHERE dataCollectionEndpointName = '{{ dataCollectionEndpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
