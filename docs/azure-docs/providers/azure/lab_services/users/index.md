---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - lab_services
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.lab_services.users" /></td></tr>
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
| <CopyableCode code="additional_usage_quota" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="email" /> | `text` | field from the `properties` object |
| <CopyableCode code="invitation_sent" /> | `text` | field from the `properties` object |
| <CopyableCode code="invitation_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="labName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registration_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_operation_error" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="total_usage" /> | `text` | field from the `properties` object |
| <CopyableCode code="userName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | User resource properties |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="labName, resourceGroupName, subscriptionId, userName" /> | Returns the properties of a lab user. |
| <CopyableCode code="list_by_lab" /> | `SELECT` | <CopyableCode code="labName, resourceGroupName, subscriptionId" /> | Returns a list of all users for a lab. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="labName, resourceGroupName, subscriptionId, userName, data__properties" /> | Operation to create or update a lab user. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="labName, resourceGroupName, subscriptionId, userName" /> | Operation to delete a user resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="labName, resourceGroupName, subscriptionId, userName" /> | Operation to update a lab user. |
| <CopyableCode code="invite" /> | `EXEC` | <CopyableCode code="labName, resourceGroupName, subscriptionId, userName" /> | Operation to invite a user to a lab. |

## `SELECT` examples

Returns a list of all users for a lab.

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
additional_usage_quota,
display_name,
email,
invitation_sent,
invitation_state,
labName,
provisioning_state,
registration_state,
resourceGroupName,
resource_operation_error,
subscriptionId,
system_data,
total_usage,
userName
FROM azure.lab_services.vw_users
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.lab_services.users
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
INSERT INTO azure.lab_services.users (
labName,
resourceGroupName,
subscriptionId,
userName,
data__properties,
properties
)
SELECT 
'{{ labName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ userName }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
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
    - name: properties
      value:
        - name: additionalUsageQuota
          value: string
        - name: provisioningState
          value: []
        - name: resourceOperationError
          value:
            - name: timestamp
              value: string
            - name: code
              value: string
            - name: message
              value: string
            - name: action
              value: string
        - name: displayName
          value: string
        - name: email
          value: []
        - name: registrationState
          value: []
        - name: invitationState
          value: []
        - name: invitationSent
          value: string
        - name: totalUsage
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>users</code> resource.

```sql
/*+ update */
UPDATE azure.lab_services.users
SET 
properties = '{{ properties }}'
WHERE 
labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userName = '{{ userName }}';
```

## `DELETE` example

Deletes the specified <code>users</code> resource.

```sql
/*+ delete */
DELETE FROM azure.lab_services.users
WHERE labName = '{{ labName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND userName = '{{ userName }}';
```
