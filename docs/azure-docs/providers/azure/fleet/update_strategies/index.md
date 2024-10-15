---
title: update_strategies
hide_title: false
hide_table_of_contents: false
keywords:
  - update_strategies
  - fleet
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

Creates, updates, deletes, gets or lists a <code>update_strategies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>update_strategies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.fleet.update_strategies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_update_strategies', value: 'view', },
        { label: 'update_strategies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="fleetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="strategy" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="updateStrategyName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="eTag" /> | `string` | If eTag is provided in the response body, it may also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. |
| <CopyableCode code="properties" /> | `object` | The properties of the UpdateStrategy. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId, updateStrategyName" /> | Get a FleetUpdateStrategy |
| <CopyableCode code="list_by_fleet" /> | `SELECT` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId" /> | List FleetUpdateStrategy resources by Fleet |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId, updateStrategyName" /> | Create a FleetUpdateStrategy |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="fleetName, resourceGroupName, subscriptionId, updateStrategyName" /> | Delete a FleetUpdateStrategy |

## `SELECT` examples

List FleetUpdateStrategy resources by Fleet

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_update_strategies', value: 'view', },
        { label: 'update_strategies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
e_tag,
fleetName,
provisioning_state,
resourceGroupName,
strategy,
subscriptionId,
updateStrategyName
FROM azure.fleet.vw_update_strategies
WHERE fleetName = '{{ fleetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
eTag,
properties
FROM azure.fleet.update_strategies
WHERE fleetName = '{{ fleetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>update_strategies</code> resource.

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
INSERT INTO azure.fleet.update_strategies (
fleetName,
resourceGroupName,
subscriptionId,
updateStrategyName,
properties
)
SELECT 
'{{ fleetName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ updateStrategyName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: provisioningState
          value: []
        - name: strategy
          value:
            - name: stages
              value:
                - - name: name
                    value: string
                  - name: groups
                    value:
                      - - name: name
                          value: string
                  - name: afterStageWaitInSeconds
                    value: integer
    - name: eTag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>update_strategies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.fleet.update_strategies
WHERE fleetName = '{{ fleetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND updateStrategyName = '{{ updateStrategyName }}';
```
