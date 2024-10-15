---
title: protected_items
hide_title: false
hide_table_of_contents: false
keywords:
  - protected_items
  - data_replication
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

Creates, updates, deletes, gets or lists a <code>protected_items</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>protected_items</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_replication.protected_items" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_protected_items', value: 'view', },
        { label: 'protected_items', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `text` | Gets or sets the name of the resource. |
| <CopyableCode code="allowed_jobs" /> | `text` | field from the `properties` object |
| <CopyableCode code="correlation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="current_job" /> | `text` | field from the `properties` object |
| <CopyableCode code="custom_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="dra_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabric_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabric_object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="fabric_object_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="health_errors" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_failed_enable_protection_job" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_failed_planned_failover_job" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_successful_planned_failover_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_successful_test_failover_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_successful_unplanned_failover_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_test_failover_job" /> | `text` | field from the `properties` object |
| <CopyableCode code="policy_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="protectedItemName" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="protection_state_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_extension_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="replication_health" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resync_required" /> | `text` | field from the `properties` object |
| <CopyableCode code="resynchronization_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="source_fabric_provider_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_dra_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_fabric_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_fabric_provider_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_failover_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="test_failover_state_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets or sets the type of the resource. |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name of the resource. |
| <CopyableCode code="properties" /> | `object` | Protected item model properties. |
| <CopyableCode code="systemData" /> | `object` | System data required to be defined for Azure resources. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="protectedItemName, resourceGroupName, subscriptionId, vaultName" /> | Gets the details of the protected item. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Gets the list of protected items in the given vault. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="protectedItemName, resourceGroupName, subscriptionId, vaultName, data__properties" /> | Creates the protected item. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="protectedItemName, resourceGroupName, subscriptionId, vaultName" /> | Removes the protected item. |
| <CopyableCode code="planned_failover" /> | `EXEC` | <CopyableCode code="protectedItemName, resourceGroupName, subscriptionId, vaultName, data__properties" /> | Performs the planned failover on the protected item. |

## `SELECT` examples

Gets the list of protected items in the given vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_protected_items', value: 'view', },
        { label: 'protected_items', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
allowed_jobs,
correlation_id,
current_job,
custom_properties,
dra_id,
fabric_id,
fabric_object_id,
fabric_object_name,
health_errors,
last_failed_enable_protection_job,
last_failed_planned_failover_job,
last_successful_planned_failover_time,
last_successful_test_failover_time,
last_successful_unplanned_failover_time,
last_test_failover_job,
policy_name,
protectedItemName,
protection_state,
protection_state_description,
provisioning_state,
replication_extension_name,
replication_health,
resourceGroupName,
resync_required,
resynchronization_state,
source_fabric_provider_id,
subscriptionId,
system_data,
target_dra_id,
target_fabric_id,
target_fabric_provider_id,
test_failover_state,
test_failover_state_description,
type,
vaultName
FROM azure.data_replication.vw_protected_items
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_replication.protected_items
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>protected_items</code> resource.

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
INSERT INTO azure.data_replication.protected_items (
protectedItemName,
resourceGroupName,
subscriptionId,
vaultName,
data__properties,
properties
)
SELECT 
'{{ protectedItemName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vaultName }}',
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
        - name: policyName
          value: string
        - name: replicationExtensionName
          value: string
        - name: correlationId
          value: string
        - name: provisioningState
          value: string
        - name: protectionState
          value: string
        - name: protectionStateDescription
          value: string
        - name: testFailoverState
          value: string
        - name: testFailoverStateDescription
          value: string
        - name: resynchronizationState
          value: string
        - name: fabricObjectId
          value: string
        - name: fabricObjectName
          value: string
        - name: sourceFabricProviderId
          value: string
        - name: targetFabricProviderId
          value: string
        - name: fabricId
          value: string
        - name: targetFabricId
          value: string
        - name: draId
          value: string
        - name: targetDraId
          value: string
        - name: resyncRequired
          value: boolean
        - name: lastSuccessfulPlannedFailoverTime
          value: string
        - name: lastSuccessfulUnplannedFailoverTime
          value: string
        - name: lastSuccessfulTestFailoverTime
          value: string
        - name: currentJob
          value: string
        - name: allowedJobs
          value:
            - string
        - name: lastFailedEnableProtectionJob
          value: string
        - name: lastFailedPlannedFailoverJob
          value: string
        - name: lastTestFailoverJob
          value: string
        - name: replicationHealth
          value: string
        - name: healthErrors
          value:
            - - name: affectedResourceType
                value: string
              - name: affectedResourceCorrelationIds
                value:
                  - string
              - name: childErrors
                value:
                  - - name: code
                      value: string
                    - name: healthCategory
                      value: string
                    - name: category
                      value: string
                    - name: severity
                      value: string
                    - name: source
                      value: string
                    - name: creationTime
                      value: string
                    - name: isCustomerResolvable
                      value: boolean
                    - name: summary
                      value: string
                    - name: message
                      value: string
                    - name: causes
                      value: string
                    - name: recommendation
                      value: string
              - name: code
                value: string
              - name: healthCategory
                value: string
              - name: category
                value: string
              - name: severity
                value: string
              - name: source
                value: string
              - name: creationTime
                value: string
              - name: isCustomerResolvable
                value: boolean
              - name: summary
                value: string
              - name: message
                value: string
              - name: causes
                value: string
              - name: recommendation
                value: string
        - name: customProperties
          value:
            - name: instanceType
              value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: systemData
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>protected_items</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_replication.protected_items
WHERE protectedItemName = '{{ protectedItemName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
