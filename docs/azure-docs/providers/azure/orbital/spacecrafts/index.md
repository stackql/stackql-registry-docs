---
title: spacecrafts
hide_title: false
hide_table_of_contents: false
keywords:
  - spacecrafts
  - orbital
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

Creates, updates, deletes, gets or lists a <code>spacecrafts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>spacecrafts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.orbital.spacecrafts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_spacecrafts', value: 'view', },
        { label: 'spacecrafts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="links" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="norad_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="spacecraftName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="title_line" /> | `text` | field from the `properties` object |
| <CopyableCode code="tle_line1" /> | `text` | field from the `properties` object |
| <CopyableCode code="tle_line2" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | List of Spacecraft Resource Properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, spacecraftName, subscriptionId" /> | Gets the specified spacecraft in a specified resource group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns list of spacecrafts by resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns list of spacecrafts by subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, spacecraftName, subscriptionId, data__properties" /> | Creates or updates a spacecraft resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, spacecraftName, subscriptionId" /> | Deletes a specified spacecraft resource. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, spacecraftName, subscriptionId" /> | Updates the specified spacecraft tags. |

## `SELECT` examples

Returns list of spacecrafts by subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_spacecrafts', value: 'view', },
        { label: 'spacecrafts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
links,
location,
norad_id,
provisioning_state,
resourceGroupName,
spacecraftName,
subscriptionId,
tags,
title_line,
tle_line1,
tle_line2
FROM azure.orbital.vw_spacecrafts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.orbital.spacecrafts
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>spacecrafts</code> resource.

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
INSERT INTO azure.orbital.spacecrafts (
resourceGroupName,
spacecraftName,
subscriptionId,
data__properties,
properties,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ spacecraftName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: provisioningState
          value: string
        - name: noradId
          value: string
        - name: titleLine
          value: string
        - name: tleLine1
          value: string
        - name: tleLine2
          value: string
        - name: links
          value:
            - - name: name
                value: string
              - name: centerFrequencyMHz
                value: number
              - name: bandwidthMHz
                value: number
              - name: direction
                value: string
              - name: polarization
                value: string
              - name: authorizations
                value:
                  - - name: groundStation
                      value: string
                    - name: expirationDate
                      value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>spacecrafts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.orbital.spacecrafts
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND spacecraftName = '{{ spacecraftName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
