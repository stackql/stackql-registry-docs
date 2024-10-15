---
title: cloud_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_connections
  - hybrid_cloud
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

Creates, updates, deletes, gets or lists a <code>cloud_connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_cloud.cloud_connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_connections', value: 'view', },
        { label: 'cloud_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cloudConnectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_connector" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="shared_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="virtual_hub" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Cloud connection resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudConnectionName, resourceGroupName, subscriptionId" /> | Gets the specified cloud connection in a specified resource group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Return list of cloud connections in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Return list of cloud connections in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cloudConnectionName, resourceGroupName, subscriptionId" /> | Creates or updates a cloud connection resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudConnectionName, resourceGroupName, subscriptionId" /> | Deletes a specified cloud connection resource. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="cloudConnectionName, resourceGroupName, subscriptionId" /> | Updates the specified cloud connection tags. |

## `SELECT` examples

Return list of cloud connections in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_connections', value: 'view', },
        { label: 'cloud_connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
cloudConnectionName,
cloud_connector,
etag,
location,
provisioning_state,
remote_resource_id,
resourceGroupName,
shared_key,
subscriptionId,
tags,
virtual_hub
FROM azure.hybrid_cloud.vw_cloud_connections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
etag,
location,
properties,
tags
FROM azure.hybrid_cloud.cloud_connections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cloud_connections</code> resource.

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
INSERT INTO azure.hybrid_cloud.cloud_connections (
cloudConnectionName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ cloudConnectionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
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
    - name: properties
      value:
        - name: cloudConnector
          value:
            - name: id
              value: string
        - name: remoteResourceId
          value: string
        - name: sharedKey
          value: string
        - name: provisioningState
          value: []
    - name: etag
      value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>cloud_connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_cloud.cloud_connections
WHERE cloudConnectionName = '{{ cloudConnectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
