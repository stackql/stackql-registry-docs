---
title: configuration_profile_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profile_assignments
  - automanage
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

Creates, updates, deletes, gets or lists a <code>configuration_profile_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_profile_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automanage.configuration_profile_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_profile_assignments', value: 'view', },
        { label: 'configuration_profile_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="configurationProfileAssignmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="managedBy" /> | `string` | Azure resource id. Indicates if this resource is managed by another Azure resource. |
| <CopyableCode code="properties" /> | `object` | Automanage configuration profile assignment properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationProfileAssignmentName, resourceGroupName, subscriptionId, vmName" /> | Get information about a configuration profile assignment |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get list of configuration profile assignments |
| <CopyableCode code="list_by_cluster_name" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get list of configuration profile assignments |
| <CopyableCode code="list_by_machine_name" /> | `SELECT` | <CopyableCode code="machineName, resourceGroupName, subscriptionId" /> | Get list of configuration profile assignments |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get list of configuration profile assignments under a given subscription |
| <CopyableCode code="list_by_virtual_machines" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmName" /> | Get list of configuration profile assignments |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationProfileAssignmentName, resourceGroupName, subscriptionId, vmName" /> | Creates an association between a VM and Automanage configuration profile |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationProfileAssignmentName, resourceGroupName, subscriptionId, vmName" /> | Delete a configuration profile assignment |

## `SELECT` examples

Get list of configuration profile assignments under a given subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_profile_assignments', value: 'view', },
        { label: 'configuration_profile_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
configurationProfileAssignmentName,
configuration_profile,
managed_by,
resourceGroupName,
status,
subscriptionId,
system_data,
target_id,
vmName
FROM azure.automanage.vw_configuration_profile_assignments
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
managedBy,
properties,
systemData
FROM azure.automanage.configuration_profile_assignments
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration_profile_assignments</code> resource.

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
INSERT INTO azure.automanage.configuration_profile_assignments (
configurationProfileAssignmentName,
resourceGroupName,
subscriptionId,
vmName,
properties
)
SELECT 
'{{ configurationProfileAssignmentName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vmName }}',
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
        - name: configurationProfile
          value: string
        - name: targetId
          value: string
        - name: status
          value: string
    - name: managedBy
      value: []
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

Deletes the specified <code>configuration_profile_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automanage.configuration_profile_assignments
WHERE configurationProfileAssignmentName = '{{ configurationProfileAssignmentName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmName = '{{ vmName }}';
```
