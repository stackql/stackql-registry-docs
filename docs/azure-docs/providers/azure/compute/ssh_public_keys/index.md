---
title: ssh_public_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - ssh_public_keys
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

Creates, updates, deletes, gets or lists a <code>ssh_public_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ssh_public_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.ssh_public_keys" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ssh_public_keys', value: 'view', },
        { label: 'ssh_public_keys', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="location" /> | `text` | Resource location |
| <CopyableCode code="public_key" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sshPublicKeyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags |
| <CopyableCode code="type" /> | `text` | Resource type |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Properties of the SSH public key. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, sshPublicKeyName, subscriptionId" /> | Retrieves information about an SSH public key. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all of the SSH public keys in the specified resource group. Use the nextLink property in the response to get the next page of SSH public keys. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all of the SSH public keys in the subscription. Use the nextLink property in the response to get the next page of SSH public keys. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="resourceGroupName, sshPublicKeyName, subscriptionId" /> | Creates a new SSH public key resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, sshPublicKeyName, subscriptionId" /> | Delete an SSH public key. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceGroupName, sshPublicKeyName, subscriptionId" /> | Updates a new SSH public key resource. |
| <CopyableCode code="generate_key_pair" /> | `EXEC` | <CopyableCode code="resourceGroupName, sshPublicKeyName, subscriptionId" /> | Generates and returns a public/private key pair and populates the SSH public key resource with the public key. The length of the key will be 3072 bits. This operation can only be performed once per SSH public key resource. |

## `SELECT` examples

Lists all of the SSH public keys in the subscription. Use the nextLink property in the response to get the next page of SSH public keys.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_ssh_public_keys', value: 'view', },
        { label: 'ssh_public_keys', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
location,
public_key,
resourceGroupName,
sshPublicKeyName,
subscriptionId,
tags,
type
FROM azure.compute.vw_ssh_public_keys
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
FROM azure.compute.ssh_public_keys
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>ssh_public_keys</code> resource.

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
INSERT INTO azure.compute.ssh_public_keys (
resourceGroupName,
sshPublicKeyName,
subscriptionId,
properties,
location,
tags
)
SELECT 
'{{ resourceGroupName }}',
'{{ sshPublicKeyName }}',
'{{ subscriptionId }}',
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
        - name: publicKey
          value: string
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

Updates a <code>ssh_public_keys</code> resource.

```sql
/*+ update */
UPDATE azure.compute.ssh_public_keys
SET 
properties = '{{ properties }}',
tags = '{{ tags }}'
WHERE 
resourceGroupName = '{{ resourceGroupName }}'
AND sshPublicKeyName = '{{ sshPublicKeyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>ssh_public_keys</code> resource.

```sql
/*+ delete */
DELETE FROM azure.compute.ssh_public_keys
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND sshPublicKeyName = '{{ sshPublicKeyName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
