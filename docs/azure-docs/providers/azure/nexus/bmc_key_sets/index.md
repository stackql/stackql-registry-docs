---
title: bmc_key_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - bmc_key_sets
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

Creates, updates, deletes, gets or lists a <code>bmc_key_sets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bmc_key_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.bmc_key_sets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bmc_key_sets', value: 'view', },
        { label: 'bmc_key_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="azure_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="bmcKeySetName" /> | `text` | field from the `properties` object |
| <CopyableCode code="clusterName" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_validation" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bmcKeySetName, clusterName, resourceGroupName, subscriptionId" /> | Get baseboard management controller key set of the provided cluster. |
| <CopyableCode code="list_by_cluster" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get a list of baseboard management controller key sets for the provided cluster. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="bmcKeySetName, clusterName, resourceGroupName, subscriptionId, data__extendedLocation, data__properties" /> | Create a new baseboard management controller key set or update the existing one for the provided cluster. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bmcKeySetName, clusterName, resourceGroupName, subscriptionId" /> | Delete the baseboard management controller key set of the provided cluster. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="bmcKeySetName, clusterName, resourceGroupName, subscriptionId" /> | Patch properties of baseboard management controller key set for the provided cluster, or update the tags associated with it. Properties and tag updates can be done independently. |

## `SELECT` examples

Get a list of baseboard management controller key sets for the provided cluster.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_bmc_key_sets', value: 'view', },
        { label: 'bmc_key_sets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
azure_group_id,
bmcKeySetName,
clusterName,
detailed_status,
detailed_status_message,
expiration,
extended_location,
last_validation,
location,
privilege_level,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
user_list,
user_list_status
FROM azure.nexus.vw_bmc_key_sets
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
FROM azure.nexus.bmc_key_sets
WHERE clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>bmc_key_sets</code> resource.

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
INSERT INTO azure.nexus.bmc_key_sets (
bmcKeySetName,
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
'{{ bmcKeySetName }}',
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
        - name: lastValidation
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

Updates a <code>bmc_key_sets</code> resource.

```sql
/*+ update */
UPDATE azure.nexus.bmc_key_sets
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
bmcKeySetName = '{{ bmcKeySetName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>bmc_key_sets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.nexus.bmc_key_sets
WHERE bmcKeySetName = '{{ bmcKeySetName }}'
AND clusterName = '{{ clusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
