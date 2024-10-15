---
title: availability_group_listeners
hide_title: false
hide_table_of_contents: false
keywords:
  - availability_group_listeners
  - sql_vm
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

Creates, updates, deletes, gets or lists a <code>availability_group_listeners</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>availability_group_listeners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql_vm.availability_group_listeners" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_availability_group_listeners', value: 'view', },
        { label: 'availability_group_listeners', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="availabilityGroupListenerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_group_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="availability_group_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="create_default_availability_group_if_not_exist" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_balancer_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="multi_subnet_ip_configurations" /> | `text` | field from the `properties` object |
| <CopyableCode code="port" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlVirtualMachineGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The properties of an availability group listener. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="availabilityGroupListenerName, resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Gets an availability group listener. |
| <CopyableCode code="list_by_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Lists all availability group listeners in a SQL virtual machine group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="availabilityGroupListenerName, resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Creates or updates an availability group listener. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="availabilityGroupListenerName, resourceGroupName, sqlVirtualMachineGroupName, subscriptionId" /> | Deletes an availability group listener. |

## `SELECT` examples

Lists all availability group listeners in a SQL virtual machine group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_availability_group_listeners', value: 'view', },
        { label: 'availability_group_listeners', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
availabilityGroupListenerName,
availability_group_configuration,
availability_group_name,
create_default_availability_group_if_not_exist,
load_balancer_configurations,
multi_subnet_ip_configurations,
port,
provisioning_state,
resourceGroupName,
sqlVirtualMachineGroupName,
subscriptionId,
system_data
FROM azure.sql_vm.vw_availability_group_listeners
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlVirtualMachineGroupName = '{{ sqlVirtualMachineGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.sql_vm.availability_group_listeners
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sqlVirtualMachineGroupName = '{{ sqlVirtualMachineGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>availability_group_listeners</code> resource.

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
INSERT INTO azure.sql_vm.availability_group_listeners (
availabilityGroupListenerName,
resourceGroupName,
sqlVirtualMachineGroupName,
subscriptionId,
properties
)
SELECT 
'{{ availabilityGroupListenerName }}',
'{{ resourceGroupName }}',
'{{ sqlVirtualMachineGroupName }}',
'{{ subscriptionId }}',
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
          value: string
        - name: availabilityGroupName
          value: string
        - name: loadBalancerConfigurations
          value:
            - - name: privateIpAddress
                value:
                  - name: ipAddress
                    value: string
                  - name: subnetResourceId
                    value: string
              - name: publicIpAddressResourceId
                value: string
              - name: loadBalancerResourceId
                value: string
              - name: probePort
                value: integer
              - name: sqlVirtualMachineInstances
                value:
                  - string
        - name: multiSubnetIpConfigurations
          value:
            - - name: sqlVirtualMachineInstance
                value: string
        - name: createDefaultAvailabilityGroupIfNotExist
          value: boolean
        - name: port
          value: integer
        - name: availabilityGroupConfiguration
          value:
            - name: replicas
              value:
                - - name: sqlVirtualMachineInstanceId
                    value: string
                  - name: role
                    value: string
                  - name: commit
                    value: string
                  - name: failover
                    value: string
                  - name: readableSecondary
                    value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>availability_group_listeners</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql_vm.availability_group_listeners
WHERE availabilityGroupListenerName = '{{ availabilityGroupListenerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlVirtualMachineGroupName = '{{ sqlVirtualMachineGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
