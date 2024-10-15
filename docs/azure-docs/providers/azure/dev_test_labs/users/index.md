---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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

Creates, updates, deletes, gets or lists a <code>users</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.users" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_users', value: 'view', },
        { label: 'users', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="created_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="labName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="secret_store" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="unique_identifier" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a lab user profile. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Get user profile. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="labName, resourceGroupName, subscriptionId" /> | List user profiles in a given lab. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Create or replace an existing user profile. This operation can take a while to complete. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Delete user profile. This operation can take a while to complete. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId" /> | Allows modifying tags of user profiles. All other properties will be ignored. |

## `SELECT` examples

List user profiles in a given lab.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_users', value: 'view', },
        { label: 'users', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
created_date,
identity,
labName,
location,
provisioning_state,
resourceGroupName,
secret_store,
subscriptionId,
tags,
type,
unique_identifier
FROM azure.dev_test_labs.vw_users
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
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
tags,
type
FROM azure.dev_test_labs.users
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>users</code> resource.

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
INSERT INTO azure.dev_test_labs.users (
labName,
name,
resourceGroupName,
subscriptionId,
location,
tags,
properties
)
SELECT 
'{{ labName }}',
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
        - name: identity
          value:
            - name: principalName
              value: string
            - name: principalId
              value: string
            - name: tenantId
              value: string
            - name: objectId
              value: string
            - name: appId
              value: string
        - name: secretStore
          value:
            - name: keyVaultUri
              value: string
            - name: keyVaultId
              value: string
        - name: createdDate
          value: string
        - name: provisioningState
          value: string
        - name: uniqueIdentifier
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>users</code> resource.

```sql
/*+ update */
UPDATE azure.dev_test_labs.users
SET 
tags = '{{ tags }}'
WHERE 
labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>users</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_test_labs.users
WHERE labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
