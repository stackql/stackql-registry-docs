---
title: disks
hide_title: false
hide_table_of_contents: false
keywords:
  - disks
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

Creates, updates, deletes, gets or lists a <code>disks</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>disks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.disks" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disks', value: 'view', },
        { label: 'disks', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_blob_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_size_gib" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="disk_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="host_caching" /> | `text` | field from the `properties` object |
| <CopyableCode code="labName" /> | `text` | field from the `properties` object |
| <CopyableCode code="leased_by_lab_vm_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource. |
| <CopyableCode code="managed_disk_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="unique_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="userName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a disk. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, userName" /> | Get disk. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="labName, resourceGroupName, subscriptionId, userName" /> | List disks in a given user profile. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, userName, data__properties" /> | Create or replace an existing disk. This operation can take a while to complete. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, userName" /> | Delete disk. This operation can take a while to complete. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, userName" /> | Allows modifying tags of disks. All other properties will be ignored. |
| <CopyableCode code="attach" /> | `EXEC` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, userName" /> | Attach and create the lease of the disk to the virtual machine. This operation can take a while to complete. |
| <CopyableCode code="detach" /> | `EXEC` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, userName" /> | Detach and break the lease of the disk attached to the virtual machine. This operation can take a while to complete. |

## `SELECT` examples

List disks in a given user profile.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_disks', value: 'view', },
        { label: 'disks', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
created_date,
disk_blob_name,
disk_size_gib,
disk_type,
disk_uri,
host_caching,
labName,
leased_by_lab_vm_id,
location,
managed_disk_id,
provisioning_state,
resourceGroupName,
storage_account_id,
subscriptionId,
tags,
type,
unique_identifier,
userName
FROM azure.dev_test_labs.vw_disks
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userName = '{{ userName }}';
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
FROM azure.dev_test_labs.disks
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userName = '{{ userName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>disks</code> resource.

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
INSERT INTO azure.dev_test_labs.disks (
labName,
name,
resourceGroupName,
subscriptionId,
userName,
data__properties,
location,
tags,
properties
)
SELECT 
'{{ labName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ userName }}',
'{{ data__properties }}',
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
        - name: diskType
          value: string
        - name: diskSizeGiB
          value: integer
        - name: leasedByLabVmId
          value: string
        - name: diskBlobName
          value: string
        - name: diskUri
          value: string
        - name: storageAccountId
          value: string
        - name: createdDate
          value: string
        - name: hostCaching
          value: string
        - name: managedDiskId
          value: string
        - name: provisioningState
          value: string
        - name: uniqueIdentifier
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>disks</code> resource.

```sql
/*+ update */
UPDATE azure.dev_test_labs.disks
SET 
tags = '{{ tags }}'
WHERE 
labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userName = '{{ userName }}';
```

## `DELETE` example

Deletes the specified <code>disks</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_test_labs.disks
WHERE labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userName = '{{ userName }}';
```
