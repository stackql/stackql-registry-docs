---
title: consoles
hide_title: false
hide_table_of_contents: false
keywords:
  - consoles
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

Creates, updates, deletes, gets or lists a <code>consoles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consoles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.nexus.consoles" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_consoles', value: 'view', },
        { label: 'consoles', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="consoleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="detailed_status_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="enabled" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="private_link_service_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ssh_public_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="virtualMachineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_machine_access_id" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="consoleName, resourceGroupName, subscriptionId, virtualMachineName" /> | Get properties of the provided virtual machine console. |
| <CopyableCode code="list_by_virtual_machine" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualMachineName" /> | Get a list of consoles for the provided virtual machine. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="consoleName, resourceGroupName, subscriptionId, virtualMachineName, data__extendedLocation, data__properties" /> | Create a new virtual machine console or update the properties of the existing virtual machine console. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="consoleName, resourceGroupName, subscriptionId, virtualMachineName" /> | Delete the provided virtual machine console. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="consoleName, resourceGroupName, subscriptionId, virtualMachineName" /> | Patch the properties of the provided virtual machine console, or update the tags associated with the virtual machine console. Properties and tag updates can be done independently. |

## `SELECT` examples

Get a list of consoles for the provided virtual machine.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_consoles', value: 'view', },
        { label: 'consoles', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
consoleName,
detailed_status,
detailed_status_message,
enabled,
expiration,
extended_location,
location,
private_link_service_id,
provisioning_state,
resourceGroupName,
ssh_public_key,
subscriptionId,
tags,
virtualMachineName,
virtual_machine_access_id
FROM azure.nexus.vw_consoles
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineName = '{{ virtualMachineName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.nexus.consoles
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineName = '{{ virtualMachineName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>consoles</code> resource.

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
INSERT INTO azure.nexus.consoles (
consoleName,
resourceGroupName,
subscriptionId,
virtualMachineName,
data__extendedLocation,
data__properties,
extendedLocation,
properties,
tags,
location
)
SELECT 
'{{ consoleName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ virtualMachineName }}',
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
        - name: detailedStatus
          value: string
        - name: detailedStatusMessage
          value: string
        - name: enabled
          value: string
        - name: expiration
          value: string
        - name: privateLinkServiceId
          value: string
        - name: provisioningState
          value: string
        - name: sshPublicKey
          value:
            - name: keyData
              value: string
        - name: virtualMachineAccessId
          value: string
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>consoles</code> resource.

```sql
/*+ update */
UPDATE azure.nexus.consoles
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
consoleName = '{{ consoleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineName = '{{ virtualMachineName }}';
```

## `DELETE` example

Deletes the specified <code>consoles</code> resource.

```sql
/*+ delete */
DELETE FROM azure.nexus.consoles
WHERE consoleName = '{{ consoleName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualMachineName = '{{ virtualMachineName }}';
```
