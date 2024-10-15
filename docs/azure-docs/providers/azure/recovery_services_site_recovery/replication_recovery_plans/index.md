---
title: replication_recovery_plans
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_recovery_plans
  - recovery_services_site_recovery
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

Creates, updates, deletes, gets or lists a <code>replication_recovery_plans</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_recovery_plans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.recovery_services_site_recovery.replication_recovery_plans" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_recovery_plans', value: 'view', },
        { label: 'replication_recovery_plans', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource Name |
| <CopyableCode code="allowed_operations" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_scenario" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_scenario_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_scenario_status_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="failover_deployment_model" /> | `text` | field from the `properties` object |
| <CopyableCode code="friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_planned_failover_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_test_failover_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_unplanned_failover_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource Location |
| <CopyableCode code="primary_fabric_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_fabric_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provider_specific_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="recoveryPlanName" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_fabric_friendly_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="recovery_fabric_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_providers" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource Type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource Name |
| <CopyableCode code="location" /> | `string` | Resource Location |
| <CopyableCode code="properties" /> | `object` | Recovery plan properties. |
| <CopyableCode code="type" /> | `string` | Resource Type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="recoveryPlanName, resourceGroupName, resourceName, subscriptionId" /> | Gets the details of the recovery plan. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | Lists the recovery plans in the vault. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to create a recovery plan. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="recoveryPlanName, resourceGroupName, resourceName, subscriptionId" /> | Delete a recovery plan. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="recoveryPlanName, resourceGroupName, resourceName, subscriptionId" /> | The operation to update a recovery plan. |
| <CopyableCode code="failover_cancel" /> | `EXEC` | <CopyableCode code="recoveryPlanName, resourceGroupName, resourceName, subscriptionId" /> | The operation to cancel the failover of a recovery plan. |
| <CopyableCode code="failover_commit" /> | `EXEC` | <CopyableCode code="recoveryPlanName, resourceGroupName, resourceName, subscriptionId" /> | The operation to commit the failover of a recovery plan. |
| <CopyableCode code="planned_failover" /> | `EXEC` | <CopyableCode code="recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to start the planned failover of a recovery plan. |
| <CopyableCode code="reprotect" /> | `EXEC` | <CopyableCode code="recoveryPlanName, resourceGroupName, resourceName, subscriptionId" /> | The operation to reprotect(reverse replicate) a recovery plan. |
| <CopyableCode code="test_failover" /> | `EXEC` | <CopyableCode code="recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to start the test failover of a recovery plan. |
| <CopyableCode code="test_failover_cleanup" /> | `EXEC` | <CopyableCode code="recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to cleanup test failover of a recovery plan. |
| <CopyableCode code="unplanned_failover" /> | `EXEC` | <CopyableCode code="recoveryPlanName, resourceGroupName, resourceName, subscriptionId, data__properties" /> | The operation to start the unplanned failover of a recovery plan. |

## `SELECT` examples

Lists the recovery plans in the vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_recovery_plans', value: 'view', },
        { label: 'replication_recovery_plans', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allowed_operations,
current_scenario,
current_scenario_status,
current_scenario_status_description,
failover_deployment_model,
friendly_name,
groups,
last_planned_failover_time,
last_test_failover_time,
last_unplanned_failover_time,
location,
primary_fabric_friendly_name,
primary_fabric_id,
provider_specific_details,
recoveryPlanName,
recovery_fabric_friendly_name,
recovery_fabric_id,
replication_providers,
resourceGroupName,
resourceName,
subscriptionId,
type
FROM azure.recovery_services_site_recovery.vw_replication_recovery_plans
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
type
FROM azure.recovery_services_site_recovery.replication_recovery_plans
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_recovery_plans</code> resource.

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
INSERT INTO azure.recovery_services_site_recovery.replication_recovery_plans (
recoveryPlanName,
resourceGroupName,
resourceName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ recoveryPlanName }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
        - name: primaryFabricId
          value: string
        - name: recoveryFabricId
          value: string
        - name: failoverDeploymentModel
          value: string
        - name: groups
          value:
            - - name: groupType
                value: string
              - name: replicationProtectedItems
                value:
                  - - name: id
                      value: string
                    - name: virtualMachineId
                      value: string
              - name: startGroupActions
                value:
                  - - name: actionName
                      value: string
                    - name: failoverTypes
                      value:
                        - string
                    - name: failoverDirections
                      value:
                        - string
                    - name: customDetails
                      value:
                        - name: instanceType
                          value: string
              - name: endGroupActions
                value:
                  - - name: actionName
                      value: string
                    - name: failoverTypes
                      value:
                        - string
                    - name: failoverDirections
                      value:
                        - string
        - name: providerSpecificInput
          value:
            - - name: instanceType
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>replication_recovery_plans</code> resource.

```sql
/*+ update */
UPDATE azure.recovery_services_site_recovery.replication_recovery_plans
SET 
properties = '{{ properties }}'
WHERE 
recoveryPlanName = '{{ recoveryPlanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>replication_recovery_plans</code> resource.

```sql
/*+ delete */
DELETE FROM azure.recovery_services_site_recovery.replication_recovery_plans
WHERE recoveryPlanName = '{{ recoveryPlanName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
