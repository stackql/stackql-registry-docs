---
title: assignments_vm_sse
hide_title: false
hide_table_of_contents: false
keywords:
  - assignments_vm_sse
  - guest_configuration
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

Creates, updates, deletes, gets or lists a <code>assignments_vm_sse</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignments_vm_sse</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.guest_configuration.assignments_vm_sse" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_assignments_vm_sse', value: 'view', },
        { label: 'assignments_vm_sse', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="assignment_hash" /> | `text` | field from the `properties` object |
| <CopyableCode code="compliance_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="context" /> | `text` | field from the `properties` object |
| <CopyableCode code="guest_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_compliance_status_checked" /> | `text` | field from the `properties` object |
| <CopyableCode code="latest_assignment_report" /> | `text` | field from the `properties` object |
| <CopyableCode code="latest_report_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameter_hash" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmssName" /> | `text` | field from the `properties` object |
| <CopyableCode code="vmss_vm_list" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Guest configuration assignment properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId, vmssName" /> | Get information about a guest configuration assignment for VMSS |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vmssName" /> | List all guest configuration assignments for VMSS. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId, vmssName" /> | Creates an association between a VMSS and guest configuration |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId, vmssName" /> | Delete a guest configuration assignment for VMSS |

## `SELECT` examples

List all guest configuration assignments for VMSS.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_assignments_vm_sse', value: 'view', },
        { label: 'assignments_vm_sse', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
assignment_hash,
compliance_status,
context,
guest_configuration,
last_compliance_status_checked,
latest_assignment_report,
latest_report_id,
parameter_hash,
provisioning_state,
resourceGroupName,
resource_type,
subscriptionId,
system_data,
target_resource_id,
vmssName,
vmss_vm_list
FROM azure.guest_configuration.vw_assignments_vm_sse
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmssName = '{{ vmssName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.guest_configuration.assignments_vm_sse
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmssName = '{{ vmssName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>assignments_vm_sse</code> resource.

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
INSERT INTO azure.guest_configuration.assignments_vm_sse (
name,
resourceGroupName,
subscriptionId,
vmssName,
properties
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vmssName }}',
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
        - name: targetResourceId
          value: string
        - name: guestConfiguration
          value:
            - name: kind
              value: string
            - name: name
              value: string
            - name: version
              value: string
            - name: contentUri
              value: string
            - name: contentHash
              value: string
            - name: contentManagedIdentity
              value: string
            - name: assignmentType
              value: string
            - name: assignmentSource
              value: string
            - name: contentType
              value: string
            - name: configurationParameter
              value:
                - - name: name
                    value: string
                  - name: value
                    value: string
            - name: configurationProtectedParameter
              value:
                - - name: name
                    value: string
                  - name: value
                    value: string
            - name: configurationSetting
              value:
                - name: configurationMode
                  value: string
                - name: allowModuleOverwrite
                  value: boolean
                - name: actionAfterReboot
                  value: string
                - name: refreshFrequencyMins
                  value: number
                - name: rebootIfNeeded
                  value: boolean
                - name: configurationModeFrequencyMins
                  value: number
        - name: complianceStatus
          value: string
        - name: lastComplianceStatusChecked
          value: string
        - name: latestReportId
          value: string
        - name: parameterHash
          value: string
        - name: latestAssignmentReport
          value:
            - name: id
              value: string
            - name: reportId
              value: string
            - name: assignment
              value:
                - name: name
                  value: string
                - name: configuration
                  value:
                    - name: name
                      value: string
                    - name: version
                      value: string
            - name: vm
              value:
                - name: id
                  value: string
                - name: uuid
                  value: string
            - name: startTime
              value: string
            - name: endTime
              value: string
            - name: complianceStatus
              value: string
            - name: operationType
              value: string
            - name: resources
              value:
                - - name: complianceStatus
                    value: string
                  - name: resourceId
                    value: string
                  - name: reasons
                    value:
                      - - name: phrase
                          value: string
                        - name: code
                          value: string
                  - name: properties
                    value: object
        - name: context
          value: string
        - name: assignmentHash
          value: string
        - name: provisioningState
          value: string
        - name: resourceType
          value: string
        - name: vmssVMList
          value:
            - - name: vmId
                value: string
              - name: vmResourceId
                value: string
              - name: complianceStatus
                value: string
              - name: latestReportId
                value: string
              - name: lastComplianceChecked
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

Deletes the specified <code>assignments_vm_sse</code> resource.

```sql
/*+ delete */
DELETE FROM azure.guest_configuration.assignments_vm_sse
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmssName = '{{ vmssName }}';
```
