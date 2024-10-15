---
title: sim_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - sim_groups
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

Creates, updates, deletes, gets or lists a <code>sim_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sim_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.mobile_network.sim_groups" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sim_groups', value: 'view', },
        { label: 'sim_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="encryption_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (User assigned identity) |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="mobile_network" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="simGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (User assigned identity) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | SIM group properties. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, simGroupName, subscriptionId" /> | Gets information about the specified SIM group. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the SIM groups in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all the SIM groups in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, simGroupName, subscriptionId, data__properties" /> | Creates or updates a SIM group. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, simGroupName, subscriptionId" /> | Deletes the specified SIM group. |
| <CopyableCode code="update_tags" /> | `EXEC` | <CopyableCode code="resourceGroupName, simGroupName, subscriptionId" /> | Patch SIM group resource. |

## `SELECT` examples

Gets all the SIM groups in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sim_groups', value: 'view', },
        { label: 'sim_groups', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
encryption_key,
identity,
location,
mobile_network,
provisioning_state,
resourceGroupName,
simGroupName,
subscriptionId,
tags
FROM azure.mobile_network.vw_sim_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.mobile_network.sim_groups
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sim_groups</code> resource.

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
INSERT INTO azure.mobile_network.sim_groups (
resourceGroupName,
simGroupName,
subscriptionId,
data__properties,
properties,
identity,
tags,
location
)
SELECT 
'{{ resourceGroupName }}',
'{{ simGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}',
'{{ identity }}',
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
        - name: encryptionKey
          value:
            - name: keyUrl
              value: string
        - name: mobileNetwork
          value:
            - name: id
              value: string
    - name: identity
      value:
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sim_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.mobile_network.sim_groups
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND simGroupName = '{{ simGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
