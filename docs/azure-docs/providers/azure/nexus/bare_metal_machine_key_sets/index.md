---
title: bare_metal_machine_key_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - bare_metal_machine_key_sets
  - nexus
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

Creates, updates, deletes, gets or lists a <code>bare_metal_machine_key_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bare_metal_machine_key_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.bare_metal_machine_key_sets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bare_metal_machine_key_sets', value: 'view', },
        { label: 'bare_metal_machine_key_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azure_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="bareMetalMachineKeySetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="jump_hosts_allowed" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_validation" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="os_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="privilege_level" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="user_list" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_list_status" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bareMetalMachineKeySetName, clusterName, resourceGroupName, subscriptionId" /> | Get bare metal machine key set of the provided cluster. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get a list of bare metal machine key sets for the provided cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="bareMetalMachineKeySetName, clusterName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties" /> | Create a new bare metal machine key set or update the existing one for the provided cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bareMetalMachineKeySetName, clusterName, resourceGroupName, subscriptionId" /> | Delete the bare metal machine key set of the provided cluster. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="bareMetalMachineKeySetName, clusterName, resourceGroupName, subscriptionId" /> | Patch properties of bare metal machine key set for the provided cluster, or update the tags associated with it. Properties and tag updates can be done independently. |

## `SELECT` examples

Get a list of bare metal machine key sets for the provided cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bare_metal_machine_key_sets', value: 'view', },
        { label: 'bare_metal_machine_key_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
azure_group_id,
bareMetalMachineKeySetName,
clusterName,
detailed_status,
detailed_status_message,
expiration,
extended_location,
jump_hosts_allowed,
last_validation,
location,
os_group_name,
privilege_level,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
user_list,
user_list_status
FROM azure.nexus.vw_bare_metal_machine_key_sets
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.nexus.bare_metal_machine_key_sets
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bare_metal_machine_key_sets</code> resource.

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
INSERT INTO azure.nexus.bare_metal_machine_key_sets (
bareMetalMachineKeySetName,
clusterName,
resourceGroupName,
subscriptionId,
data__extendedLocation,
data__properties,
extendedLocation,
properties,
tags,
location
)
SELECT 
'{{ bareMetalMachineKeySetName }}',
'{{ clusterName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__extendedLocation }}',
'{{ data__properties }}',
'{{ extendedLocation }}',
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
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: string
    - name: properties
      value:
        - name: azureGroupId
          value: string
        - name: detailedStatus
          value: string
        - name: detailedStatusMessage
          value: string
        - name: expiration
          value: string
        - name: jumpHostsAllowed
          value:
            - string
        - name: lastValidation
          value: string
        - name: osGroupName
          value: string
        - name: privilegeLevel
          value: string
        - name: provisioningState
          value: string
        - name: userList
          value:
            - - name: azureUserName
                value: string
              - name: description
                value: string
              - name: sshPublicKey
                value:
                  - name: keyData
                    value: string
              - name: userPrincipalName
                value: string
        - name: userListStatus
          value:
            - - name: azureUserName
                value: string
              - name: status
                value: string
              - name: statusMessage
                value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>bare_metal_machine_key_sets</code> resource.

```sql
/*+ update */
UPDATE azure.nexus.bare_metal_machine_key_sets
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
bareMetalMachineKeySetName = '{{ bareMetalMachineKeySetName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>bare_metal_machine_key_sets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.nexus.bare_metal_machine_key_sets
WHERE bareMetalMachineKeySetName = '{{ bareMetalMachineKeySetName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
