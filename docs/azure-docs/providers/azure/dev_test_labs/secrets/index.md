---
title: secrets
hide_title: false
hide_table_of_contents: false
keywords:
  - secrets
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

Creates, updates, deletes, gets or lists a <code>secrets</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>secrets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_test_labs.secrets" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_secrets', value: 'view', },
        { label: 'secrets', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The identifier of the resource. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="labName" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The location of the resource. |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | The tags of the resource. |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="unique_identifier" /> | `text` | field from the `properties` object |
| <CopyableCode code="userName" /> | `text` | field from the `properties` object |
| <CopyableCode code="value" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The identifier of the resource. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of a secret. |
| <CopyableCode code="tags" /> | `object` | The tags of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, userName" /> | Get secret. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="labName, resourceGroupName, subscriptionId, userName" /> | List secrets in a given user profile. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, userName, data__properties" /> | Create or replace an existing secret. This operation can take a while to complete. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, userName" /> | Delete secret. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="labName, name, resourceGroupName, subscriptionId, userName" /> | Allows modifying tags of secrets. All other properties will be ignored. |

## `SELECT` examples

List secrets in a given user profile.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_secrets', value: 'view', },
        { label: 'secrets', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
labName,
location,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
type,
unique_identifier,
userName,
value
FROM azure.dev_test_labs.vw_secrets
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
FROM azure.dev_test_labs.secrets
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userName = '{{ userName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>secrets</code> resource.

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
INSERT INTO azure.dev_test_labs.secrets (
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
        - name: value
          value: string
        - name: provisioningState
          value: string
        - name: uniqueIdentifier
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>secrets</code> resource.

```sql
/*+ update */
UPDATE azure.dev_test_labs.secrets
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

Deletes the specified <code>secrets</code> resource.

```sql
/*+ delete */
DELETE FROM azure.dev_test_labs.secrets
WHERE labName = '{{ labName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userName = '{{ userName }}';
```
