---
title: configuration_profile_hcrp_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_profile_hcrp_assignments
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

Creates, updates, deletes, gets or lists a <code>configuration_profile_hcrp_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_profile_hcrp_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.automanage.configuration_profile_hcrp_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_profile_hcrp_assignments', value: 'view', },
        { label: 'configuration_profile_hcrp_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="configurationProfileAssignmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="configuration_profile" /> | `text` | field from the `properties` object |
| <CopyableCode code="machineName" /> | `text` | field from the `properties` object |
| <CopyableCode code="managed_by" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_id" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationProfileAssignmentName, machineName, resourceGroupName, subscriptionId" /> | Get information about a configuration profile assignment |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationProfileAssignmentName, machineName, resourceGroupName, subscriptionId" /> | Creates an association between a ARC machine and Automanage configuration profile |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationProfileAssignmentName, machineName, resourceGroupName, subscriptionId" /> | Delete a configuration profile assignment |

## `SELECT` examples

Get information about a configuration profile assignment

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_configuration_profile_hcrp_assignments', value: 'view', },
        { label: 'configuration_profile_hcrp_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
configurationProfileAssignmentName,
configuration_profile,
machineName,
managed_by,
resourceGroupName,
status,
subscriptionId,
system_data,
target_id
FROM azure.automanage.vw_configuration_profile_hcrp_assignments
WHERE configurationProfileAssignmentName = '{{ configurationProfileAssignmentName }}'
AND machineName = '{{ machineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
managedBy,
properties,
systemData
FROM azure.automanage.configuration_profile_hcrp_assignments
WHERE configurationProfileAssignmentName = '{{ configurationProfileAssignmentName }}'
AND machineName = '{{ machineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>configuration_profile_hcrp_assignments</code> resource.

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
INSERT INTO azure.automanage.configuration_profile_hcrp_assignments (
configurationProfileAssignmentName,
machineName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ configurationProfileAssignmentName }}',
'{{ machineName }}',
'{{ resourceGroupName }}',
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

Deletes the specified <code>configuration_profile_hcrp_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.automanage.configuration_profile_hcrp_assignments
WHERE configurationProfileAssignmentName = '{{ configurationProfileAssignmentName }}'
AND machineName = '{{ machineName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
