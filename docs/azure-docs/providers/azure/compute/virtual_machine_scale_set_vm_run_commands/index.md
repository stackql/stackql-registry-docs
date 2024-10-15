---
title: virtual_machine_scale_set_vm_run_commands
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_scale_set_vm_run_commands
  - compute
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_scale_set_vm_run_commands</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_scale_set_vm_run_commands</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.virtual_machine_scale_set_vm_run_commands" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_scale_set_vm_run_commands', value: 'view', },
        { label: 'virtual_machine_scale_set_vm_run_commands', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="async_execution" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_blob_managed_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_blob_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="instanceId" /> | `text` | field from the `properties` object |
| <CopyableCode code="instance_view" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="output_blob_managed_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="output_blob_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="protected_parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="runCommandName" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_as_password" /> | `text` | field from the `properties` object |
| <CopyableCode code="run_as_user" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="timeout_in_seconds" /> | `text` | field from the `properties` object |
| <CopyableCode code="treat_failure_as_deployment_failure" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="vmScaleSetName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Virtual Machine run command. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="instanceId, resourceGroupName, runCommandName, subscriptionId, vmScaleSetName" /> | The operation to get the VMSS VM run command. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="instanceId, resourceGroupName, subscriptionId, vmScaleSetName" /> | The operation to get all run commands of an instance in Virtual Machine Scaleset. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="instanceId, resourceGroupName, runCommandName, subscriptionId, vmScaleSetName" /> | The operation to create or update the VMSS VM run command. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="instanceId, resourceGroupName, runCommandName, subscriptionId, vmScaleSetName" /> | The operation to delete the VMSS VM run command. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="instanceId, resourceGroupName, runCommandName, subscriptionId, vmScaleSetName" /> | The operation to update the VMSS VM run command. |

## `SELECT` examples

The operation to get all run commands of an instance in Virtual Machine Scaleset.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_scale_set_vm_run_commands', value: 'view', },
        { label: 'virtual_machine_scale_set_vm_run_commands', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
async_execution,
error_blob_managed_identity,
error_blob_uri,
instanceId,
instance_view,
location,
output_blob_managed_identity,
output_blob_uri,
parameters,
protected_parameters,
provisioning_state,
resourceGroupName,
runCommandName,
run_as_password,
run_as_user,
source,
subscriptionId,
tags,
timeout_in_seconds,
treat_failure_as_deployment_failure,
type,
vmScaleSetName
FROM azure.compute.vw_virtual_machine_scale_set_vm_run_commands
WHERE instanceId = '{{ instanceId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmScaleSetName = '{{ vmScaleSetName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure.compute.virtual_machine_scale_set_vm_run_commands
WHERE instanceId = '{{ instanceId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmScaleSetName = '{{ vmScaleSetName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_machine_scale_set_vm_run_commands</code> resource.

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
INSERT INTO azure.compute.virtual_machine_scale_set_vm_run_commands (
instanceId,
resourceGroupName,
runCommandName,
subscriptionId,
vmScaleSetName,
properties,
location,
tags
)
SELECT 
'{{ instanceId }}',
'{{ resourceGroupName }}',
'{{ runCommandName }}',
'{{ subscriptionId }}',
'{{ vmScaleSetName }}',
'{{ properties }}',
'{{ location }}',
'{{ tags }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: source
          value:
            - name: script
              value: string
            - name: scriptUri
              value: string
            - name: commandId
              value: string
            - name: scriptUriManagedIdentity
              value:
                - name: clientId
                  value: string
                - name: objectId
                  value: string
        - name: parameters
          value:
            - - name: name
                value: string
              - name: value
                value: string
        - name: protectedParameters
          value:
            - - name: name
                value: string
              - name: value
                value: string
        - name: asyncExecution
          value: boolean
        - name: runAsUser
          value: string
        - name: runAsPassword
          value: string
        - name: timeoutInSeconds
          value: integer
        - name: outputBlobUri
          value: string
        - name: errorBlobUri
          value: string
        - name: provisioningState
          value: string
        - name: instanceView
          value:
            - name: executionState
              value: string
            - name: executionMessage
              value: string
            - name: exitCode
              value: integer
            - name: output
              value: string
            - name: error
              value: string
            - name: startTime
              value: string
            - name: endTime
              value: string
            - name: statuses
              value:
                - - name: code
                    value: string
                  - name: level
                    value: string
                  - name: displayStatus
                    value: string
                  - name: message
                    value: string
                  - name: time
                    value: string
        - name: treatFailureAsDeploymentFailure
          value: boolean
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_machine_scale_set_vm_run_commands</code> resource.

```sql
/*+ update */
UPDATE azure.compute.virtual_machine_scale_set_vm_run_commands
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
instanceId = '{{ instanceId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runCommandName = '{{ runCommandName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmScaleSetName = '{{ vmScaleSetName }}';
```

## `DELETE` example

Deletes the specified <code>virtual_machine_scale_set_vm_run_commands</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.virtual_machine_scale_set_vm_run_commands
WHERE instanceId = '{{ instanceId }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND runCommandName = '{{ runCommandName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vmScaleSetName = '{{ vmScaleSetName }}';
```
