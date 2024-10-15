---
title: labs
hide_title: false
hide_table_of_contents: false
keywords:
  - labs
  - dev_test_labs
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

Creates, updates, deletes, gets or lists a <code>labs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>labs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.labs" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_labs', value: 'view', },
        { label: 'labs', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="announcement" /> | `text` | field from the `properties` object |
| <CopyableCode code="artifacts_storage_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_premium_storage_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_storage_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="environment_permission" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="lab_storage_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="load_balancer_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource. |
| <CopyableCode code="mandatory_artifacts_resource_ids_linux" /> | `text` | field from the `properties` object |
| <CopyableCode code="mandatory_artifacts_resource_ids_windows" /> | `text` | field from the `properties` object |
| <CopyableCode code="network_security_group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="premium_data_disk_storage_account" /> | `text` | field from the `properties` object |
| <CopyableCode code="premium_data_disks" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="public_ip_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="support" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="unique_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="vault_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="vm_creation_resource_group" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a lab. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Get lab. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List labs in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List labs in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Create or replace an existing lab. This operation can take a while to complete. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Delete lab. This operation can take a while to complete. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Allows modifying tags of labs. All other properties will be ignored. |
| <CopyableCode code="claim_any_vm" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Claim a random claimable virtual machine in the lab. This operation can take a while to complete. |
| <CopyableCode code="export_resource_usage" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Exports the lab resource usage into a storage account This operation can take a while to complete. |
| <CopyableCode code="generate_upload_uri" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Generate a URI for uploading custom disk images to a Lab. |
| <CopyableCode code="import_virtual_machine" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Import a virtual machine into a different lab. This operation can take a while to complete. |

## `SELECT` examples

List labs in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_labs', value: 'view', },
        { label: 'labs', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
announcement,
artifacts_storage_account,
created_date,
default_premium_storage_account,
default_storage_account,
environment_permission,
extended_properties,
lab_storage_type,
load_balancer_id,
location,
mandatory_artifacts_resource_ids_linux,
mandatory_artifacts_resource_ids_windows,
network_security_group_id,
premium_data_disk_storage_account,
premium_data_disks,
provisioning_state,
public_ip_id,
resourceGroupName,
subscriptionId,
support,
tags,
type,
unique_identifier,
vault_name,
vm_creation_resource_group
FROM azure.dev_test_labs.vw_labs
WHERE subscriptionId = '{{ subscriptionId }}';
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
FROM azure.dev_test_labs.labs
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>labs</code> resource.

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
INSERT INTO azure.dev_test_labs.labs (
name,
resourceGroupName,
subscriptionId,
location,
tags,
properties
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ location }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
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
    - name: properties
      value:
        - name: defaultStorageAccount
          value: string
        - name: defaultPremiumStorageAccount
          value: string
        - name: artifactsStorageAccount
          value: string
        - name: premiumDataDiskStorageAccount
          value: string
        - name: vaultName
          value: string
        - name: labStorageType
          value: string
        - name: mandatoryArtifactsResourceIdsLinux
          value:
            - string
        - name: mandatoryArtifactsResourceIdsWindows
          value:
            - string
        - name: createdDate
          value: string
        - name: premiumDataDisks
          value: string
        - name: environmentPermission
          value: string
        - name: announcement
          value:
            - name: title
              value: string
            - name: markdown
              value: string
            - name: enabled
              value: string
            - name: expirationDate
              value: string
            - name: expired
              value: boolean
            - name: provisioningState
              value: string
            - name: uniqueIdentifier
              value: string
        - name: support
          value:
            - name: enabled
              value: string
            - name: markdown
              value: string
        - name: vmCreationResourceGroup
          value: string
        - name: publicIpId
          value: string
        - name: loadBalancerId
          value: string
        - name: networkSecurityGroupId
          value: string
        - name: extendedProperties
          value: object
        - name: provisioningState
          value: string
        - name: uniqueIdentifier
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>labs</code> resource.

```sql
/*+ update */
UPDATE azure.dev_test_labs.labs
SET 
tags = '{{ tags }}'
WHERE 
name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>labs</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_test_labs.labs
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
