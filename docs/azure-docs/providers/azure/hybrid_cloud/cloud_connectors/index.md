---
title: cloud_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_connectors
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

Creates, updates, deletes, gets or lists a <code>cloud_connectors</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_cloud.cloud_connectors" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_connectors', value: 'view', },
        { label: 'cloud_connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloudConnectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="cloud_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Cloud connector resource properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cloudConnectorName, resourceGroupName, subscriptionId" /> | Gets the specified cloud connector in a specified resource group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Return list of cloud connectors in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Return list of cloud connectors in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cloudConnectorName, resourceGroupName, subscriptionId" /> | Creates or updates a cloud connector resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cloudConnectorName, resourceGroupName, subscriptionId" /> | Deletes a specified cloud connector resource. |
| <CopyableCode code="discover_resources" /> | `EXEC` | <CopyableCode code="cloudConnectorName, resourceGroupName, subscriptionId" /> | Returns a list of discovered remote cloud resources via this cloud connector resource. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="cloudConnectorName, resourceGroupName, subscriptionId" /> | Updates the specified cloud connector tags. |

## `SELECT` examples

Return list of cloud connectors in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_cloud_connectors', value: 'view', },
        { label: 'cloud_connectors', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
account_id,
cloudConnectorName,
cloud_type,
etag,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.hybrid_cloud.vw_cloud_connectors
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
FROM azure.hybrid_cloud.cloud_connectors
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cloud_connectors</code> resource.

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
INSERT INTO azure.hybrid_cloud.cloud_connectors (
cloudConnectorName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ cloudConnectorName }}',
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
        - name: accountId
          value: string
        - name: cloudType
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

Deletes the specified <code>cloud_connectors</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_cloud.cloud_connectors
WHERE cloudConnectorName = '{{ cloudConnectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
