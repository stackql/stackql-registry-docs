---
title: dashboards
hide_title: false
hide_table_of_contents: false
keywords:
  - dashboards
  - portal
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

Creates, updates, deletes, gets or lists a <code>dashboards</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dashboards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.portal.dashboards" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dashboards', value: 'view', },
        { label: 'dashboards', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dashboardName" /> | `text` | field from the `properties` object |
| <CopyableCode code="lenses" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="metadata" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Dashboard Properties with Provisioning state |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dashboardName, resourceGroupName, subscriptionId" /> | Gets the Dashboard. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the Dashboards within a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the dashboards within a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dashboardName, resourceGroupName, subscriptionId" /> | Creates or updates a Dashboard. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dashboardName, resourceGroupName, subscriptionId" /> | Deletes the Dashboard. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dashboardName, resourceGroupName, subscriptionId" /> | Updates an existing Dashboard. |

## `SELECT` examples

Gets all the dashboards within a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_dashboards', value: 'view', },
        { label: 'dashboards', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dashboardName,
lenses,
location,
metadata,
provisioning_state,
resourceGroupName,
subscriptionId,
tags
FROM azure.portal.vw_dashboards
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.portal.dashboards
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>dashboards</code> resource.

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
INSERT INTO azure.portal.dashboards (
dashboardName,
resourceGroupName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ dashboardName }}',
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
        - name: lenses
          value:
            - - name: order
                value: integer
              - name: parts
                value:
                  - - name: position
                      value:
                        - name: x
                          value: integer
                        - name: 'y'
                          value: integer
                        - name: rowSpan
                          value: integer
                        - name: colSpan
                          value: integer
                        - name: metadata
                          value: object
                    - name: metadata
                      value:
                        - name: type
                          value: []
              - name: metadata
                value: object
        - name: metadata
          value: object
        - name: provisioningState
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>dashboards</code> resource.

```sql
/*+ update */
UPDATE azure.portal.dashboards
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
dashboardName = '{{ dashboardName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>dashboards</code> resource.

```sql
/*+ delete */
DELETE FROM azure.portal.dashboards
WHERE dashboardName = '{{ dashboardName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
