---
title: sites
hide_title: false
hide_table_of_contents: false
keywords:
  - sites
  - mobile_network
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

Creates, updates, deletes, gets or lists a <code>sites</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.sites" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sites', value: 'view', },
        { label: 'sites', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="mobileNetworkName" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_functions" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="siteName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Site properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="mobileNetworkName, resourceGroupName, siteName, subscriptionId" /> | Gets information about the specified mobile network site. |
| <CopyableCode code="list_by_mobile_network" /> | `SELECT` | <CopyableCode code="mobileNetworkName, resourceGroupName, subscriptionId" /> | Lists all sites in the mobile network. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="mobileNetworkName, resourceGroupName, siteName, subscriptionId" /> | Creates or updates a mobile network site. Must be created in the same location as its parent mobile network. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="mobileNetworkName, resourceGroupName, siteName, subscriptionId" /> | Deletes the specified mobile network site. This will also delete any network functions that are a part of this site. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="mobileNetworkName, resourceGroupName, siteName, subscriptionId" /> | Updates site tags. |

## `SELECT` examples

Lists all sites in the mobile network.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sites', value: 'view', },
        { label: 'sites', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
location,
mobileNetworkName,
network_functions,
provisioning_state,
resourceGroupName,
siteName,
subscriptionId,
tags
FROM azure.mobile_network.vw_sites
WHERE mobileNetworkName = '{{ mobileNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.mobile_network.sites
WHERE mobileNetworkName = '{{ mobileNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sites</code> resource.

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
INSERT INTO azure.mobile_network.sites (
mobileNetworkName,
resourceGroupName,
siteName,
subscriptionId,
properties,
tags,
location
)
SELECT 
'{{ mobileNetworkName }}',
'{{ resourceGroupName }}',
'{{ siteName }}',
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
        - name: provisioningState
          value: []
        - name: networkFunctions
          value:
            - - name: id
                value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sites</code> resource.

```sql
/*+ delete */
DELETE FROM azure.mobile_network.sites
WHERE mobileNetworkName = '{{ mobileNetworkName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND siteName = '{{ siteName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
