---
title: machines
hide_title: false
hide_table_of_contents: false
keywords:
  - machines
  - hybrid_compute
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

Creates, updates, deletes, gets or lists a <code>machines</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_compute.machines" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_machines', value: 'view', },
        { label: 'machines', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="agent_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_public_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_status_change" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="machine_fqdn" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="os_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="physical_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="vm_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="identity" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a hybrid machine. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Retrieves information about the model view or the instance view of a hybrid machine. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all the hybrid machines in the specified resource group. Use the nextLink property in the response to get the next page of hybrid machines. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the hybrid machines in the specified subscription. Use the nextLink property in the response to get the next page of hybrid machines. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | The operation to create or update a hybrid machine resource identity in Azure. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | The operation to remove a hybrid machine identity in Azure. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | The operation to update a hybrid machine. |
| <CopyableCode code="reconnect" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | The operation to reconnect a hybrid machine resource to its identity in Azure. |

## `SELECT` examples

Lists all the hybrid machines in the specified subscription. Use the nextLink property in the response to get the next page of hybrid machines.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_machines', value: 'view', },
        { label: 'machines', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
agent_version,
client_public_key,
display_name,
error_details,
identity,
last_status_change,
location,
machine_fqdn,
os_name,
os_profile,
os_version,
physical_location,
provisioning_state,
resourceGroupName,
status,
subscriptionId,
tags,
type,
vm_id
FROM azure.hybrid_compute.vw_machines
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
identity,
location,
properties,
tags,
type
FROM azure.hybrid_compute.machines
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>machines</code> resource.

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
INSERT INTO azure.hybrid_compute.machines (
name,
resourceGroupName,
subscriptionId,
properties,
location,
tags,
identity
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: osProfile
          value:
            - name: computerName
              value: string
        - name: provisioningState
          value: string
        - name: status
          value: string
        - name: lastStatusChange
          value: string
        - name: errorDetails
          value:
            - - name: code
                value: string
              - name: message
                value: string
              - name: target
                value: string
              - name: details
                value:
                  - - name: code
                      value: string
                    - name: message
                      value: string
                    - name: target
                      value: string
                    - name: details
                      value:
                        - - name: code
                            value: string
                          - name: message
                            value: string
                          - name: target
                            value: string
                          - name: details
                            value:
                              - - name: code
                                  value: string
                                - name: message
                                  value: string
                                - name: target
                                  value: string
                                - name: details
                                  value:
                                    - - name: code
                                        value: string
                                      - name: message
                                        value: string
                                      - name: target
                                        value: string
                                      - name: details
                                        value:
                                          - - name: code
                                              value: string
                                            - name: message
                                              value: string
                                            - name: target
                                              value: string
                                            - name: details
                                              value:
                                                - - name: code
                                                    value: string
                                                  - name: message
                                                    value: string
                                                  - name: target
                                                    value: string
                                                  - name: details
                                                    value:
                                                      - - name: code
                                                          value: string
                                                        - name: message
                                                          value: string
                                                        - name: target
                                                          value: string
                                                        - name: details
                                                          value:
                                                            - - name: code
                                                                value: string
                                                              - name: message
                                                                value: string
                                                              - name: target
                                                                value: string
                                                              - name: details
                                                                value:
                                                                  - []
        - name: agentVersion
          value: string
        - name: vmId
          value: string
        - name: displayName
          value: string
        - name: machineFqdn
          value: string
        - name: physicalLocation
          value: string
        - name: clientPublicKey
          value: string
        - name: osName
          value: string
        - name: osVersion
          value: string
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
    - name: identity
      value:
        - name: type
          value: string
        - name: principalId
          value: string
        - name: tenantId
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>machines</code> resource.

```sql
/*+ update */
UPDATE azure.hybrid_compute.machines
SET 
identity = '{{ identity }}',
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>machines</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_compute.machines
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
