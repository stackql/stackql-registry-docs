---
title: virtual_machine_image_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machine_image_templates
  - image_builder
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

Creates, updates, deletes, gets or lists a <code>virtual_machine_image_templates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_machine_image_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.image_builder.virtual_machine_image_templates" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_image_templates', value: 'view', },
        { label: 'virtual_machine_image_templates', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="auto_run" /> | `text` | field from the `properties` object |
| <CopyableCode code="build_timeout_in_minutes" /> | `text` | field from the `properties` object |
| <CopyableCode code="customize" /> | `text` | field from the `properties` object |
| <CopyableCode code="distribute" /> | `text` | field from the `properties` object |
| <CopyableCode code="error_handling" /> | `text` | field from the `properties` object |
| <CopyableCode code="exact_staging_resource_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Identity for the image template. |
| <CopyableCode code="imageTemplateName" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_run_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="managed_resource_tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="optimize" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_error" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="staging_resource_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="validate" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_profile" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Identity for the image template. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Describes the properties of an image template |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId" /> | Get information about a virtual machine image template |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets information about the VM image templates associated with the subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets information about the VM image templates associated with the specified resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId, data__identity" /> | Create or update a virtual machine image template |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId" /> | Delete a virtual machine image template |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId" /> | Update the tags for this Virtual Machine Image Template |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId" /> | Cancel the long running image build based on the image template |
| <CopyableCode code="run" /> | `EXEC` | <CopyableCode code="imageTemplateName, resourceGroupName, subscriptionId" /> | Create artifacts from a existing image template |

## `SELECT` examples

Gets information about the VM image templates associated with the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_machine_image_templates', value: 'view', },
        { label: 'virtual_machine_image_templates', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
auto_run,
build_timeout_in_minutes,
customize,
distribute,
error_handling,
exact_staging_resource_group,
identity,
imageTemplateName,
last_run_status,
location,
managed_resource_tags,
optimize,
provisioning_error,
provisioning_state,
resourceGroupName,
source,
staging_resource_group,
subscriptionId,
tags,
validate,
vm_profile
FROM azure.image_builder.vw_virtual_machine_image_templates
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
tags
FROM azure.image_builder.virtual_machine_image_templates
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_machine_image_templates</code> resource.

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
INSERT INTO azure.image_builder.virtual_machine_image_templates (
imageTemplateName,
resourceGroupName,
subscriptionId,
data__identity,
properties,
identity,
tags,
location
)
SELECT 
'{{ imageTemplateName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__identity }}',
'{{ properties }}',
'{{ identity }}',
'{{ tags }}',
'{{ location }}'
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
            - name: type
              value: string
        - name: customize
          value:
            - - name: type
                value: string
              - name: name
                value: string
        - name: optimize
          value:
            - name: vmBoot
              value:
                - name: state
                  value: string
        - name: validate
          value:
            - name: continueDistributeOnFailure
              value: boolean
            - name: sourceValidationOnly
              value: boolean
            - name: inVMValidations
              value:
                - - name: type
                    value: string
                  - name: name
                    value: string
        - name: distribute
          value:
            - - name: type
                value: string
              - name: runOutputName
                value: string
              - name: artifactTags
                value: object
        - name: errorHandling
          value:
            - name: onCustomizerError
              value: []
        - name: provisioningState
          value: []
        - name: provisioningError
          value:
            - name: provisioningErrorCode
              value: string
            - name: message
              value: string
        - name: lastRunStatus
          value:
            - name: startTime
              value: string
            - name: endTime
              value: string
            - name: runState
              value: string
            - name: runSubState
              value: string
            - name: message
              value: string
        - name: buildTimeoutInMinutes
          value: integer
        - name: vmProfile
          value:
            - name: vmSize
              value: string
            - name: osDiskSizeGB
              value: integer
            - name: userAssignedIdentities
              value:
                - string
            - name: vnetConfig
              value:
                - name: subnetId
                  value: string
                - name: containerInstanceSubnetId
                  value: string
                - name: proxyVmSize
                  value: string
        - name: stagingResourceGroup
          value: string
        - name: exactStagingResourceGroup
          value: string
        - name: autoRun
          value:
            - name: state
              value: string
        - name: managedResourceTags
          value: object
    - name: identity
      value:
        - name: type
          value: string
        - name: userAssignedIdentities
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>virtual_machine_image_templates</code> resource.

```sql
/*+ update */
UPDATE azure.image_builder.virtual_machine_image_templates
SET 
identity = '{{ identity }}',
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
imageTemplateName = '{{ imageTemplateName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>virtual_machine_image_templates</code> resource.

```sql
/*+ delete */
DELETE FROM azure.image_builder.virtual_machine_image_templates
WHERE imageTemplateName = '{{ imageTemplateName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
