---
title: hubs
hide_title: false
hide_table_of_contents: false
keywords:
  - hubs
  - customer_insights
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

Creates, updates, deletes, gets or lists a <code>hubs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hubs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.customer_insights.hubs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hubs', value: 'view', },
        { label: 'hubs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="api_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="hubName" /> | `text` | field from the `properties` object |
| <CopyableCode code="hub_billing_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="tenant_features" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
| <CopyableCode code="web_endpoint" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Properties of hub. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Gets information about the specified hub. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all hubs in the specified subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the hubs in a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Creates a hub, or updates an existing hub. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Deletes the specified hub. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="hubName, resourceGroupName, subscriptionId" /> | Updates a Hub. |

## `SELECT` examples

Gets all hubs in the specified subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_hubs', value: 'view', },
        { label: 'hubs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
api_endpoint,
hubName,
hub_billing_info,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
tenant_features,
type,
web_endpoint
FROM azure_extras.customer_insights.vw_hubs
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
tags,
type
FROM azure_extras.customer_insights.hubs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>hubs</code> resource.

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
INSERT INTO azure_extras.customer_insights.hubs (
hubName,
resourceGroupName,
subscriptionId,
properties,
location,
tags
)
SELECT 
'{{ hubName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: apiEndpoint
          value: string
        - name: webEndpoint
          value: string
        - name: provisioningState
          value: string
        - name: tenantFeatures
          value: integer
        - name: hubBillingInfo
          value:
            - name: skuName
              value: string
            - name: minUnits
              value: integer
            - name: maxUnits
              value: integer
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>hubs</code> resource.

```sql
/*+ update */
UPDATE azure_extras.customer_insights.hubs
SET 
properties = '{{ properties }}',
location = '{{ location }}',
tags = '{{ tags }}'
WHERE 
hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>hubs</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.customer_insights.hubs
WHERE hubName = '{{ hubName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
