---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - api_management
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.api_management.users" /></td></tr>
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
| <CopyableCode code="email" /> | `text` | field from the `properties` object |
| <CopyableCode code="first_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="identities" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="note" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serviceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="userId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | User profile. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, userId" /> | Gets the details of the user specified by its identifier. |
| <CopyableCode code="list_by_service" /> | `SELECT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId" /> | Lists a collection of registered users in the specified service instance. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, userId" /> | Creates or Updates a user. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="If-Match, resourceGroupName, serviceName, subscriptionId, userId" /> | Deletes specific user. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="If-Match, resourceGroupName, serviceName, subscriptionId, userId" /> | Updates the details of the user specified by its identifier. |
| <CopyableCode code="generate_sso_url" /> | `EXEC` | <CopyableCode code="resourceGroupName, serviceName, subscriptionId, userId" /> | Retrieves a redirection URL containing an authentication token for signing a given user into the developer portal. |

## `SELECT` examples

Lists a collection of registered users in the specified service instance.

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
email,
first_name,
groups,
identities,
last_name,
note,
registration_date,
resourceGroupName,
serviceName,
state,
subscriptionId,
userId
FROM azure.api_management.vw_users
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.api_management.users
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
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
INSERT INTO azure.api_management.users (
resourceGroupName,
serviceName,
subscriptionId,
userId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ serviceName }}',
'{{ subscriptionId }}',
'{{ userId }}',
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
        - name: email
          value: string
        - name: firstName
          value: string
        - name: lastName
          value: string
        - name: password
          value: string
        - name: appType
          value: string
        - name: confirmation
          value: string
        - name: state
          value: string
        - name: note
          value: string
        - name: identities
          value:
            - - name: provider
                value: string
              - name: id
                value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>users</code> resource.

```sql
/*+ update */
UPDATE azure.api_management.users
SET 
properties = '{{ properties }}'
WHERE 
If-Match = '{{ If-Match }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userId = '{{ userId }}';
```

## `DELETE` example

Deletes the specified <code>users</code> resource.

```sql
/*+ delete */
DELETE FROM azure.api_management.users
WHERE If-Match = '{{ If-Match }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serviceName = '{{ serviceName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userId = '{{ userId }}';
```
