---
title: invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - invitations
  - data_share
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

Creates, updates, deletes, gets or lists a <code>invitations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_share.invitations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_invitations', value: 'view', },
        { label: 'invitations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `text` | Name of the azure resource |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="invitationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="invitation_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="invitation_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="responded_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="sent_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="shareName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_active_directory_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_email" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_object_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of the azure resource |
| <CopyableCode code="user_email" /> | `text` | field from the `properties` object |
| <CopyableCode code="user_name" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource id of the azure resource |
| <CopyableCode code="name" /> | `string` | Name of the azure resource |
| <CopyableCode code="properties" /> | `object` | Invitation property bag. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the azure resource |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, invitationName, resourceGroupName, shareName, subscriptionId" /> | Get an invitation in a share |
| <CopyableCode code="list_by_share" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, shareName, subscriptionId" /> | List invitations in a share |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, invitationName, resourceGroupName, shareName, subscriptionId" /> | Create an invitation |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, invitationName, resourceGroupName, shareName, subscriptionId" /> | Delete an invitation in a share |

## `SELECT` examples

List invitations in a share

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_invitations', value: 'view', },
        { label: 'invitations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
expiration_date,
invitationName,
invitation_id,
invitation_status,
resourceGroupName,
responded_at,
sent_at,
shareName,
subscriptionId,
system_data,
target_active_directory_id,
target_email,
target_object_id,
type,
user_email,
user_name
FROM azure.data_share.vw_invitations
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareName = '{{ shareName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.data_share.invitations
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareName = '{{ shareName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>invitations</code> resource.

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
INSERT INTO azure.data_share.invitations (
accountName,
invitationName,
resourceGroupName,
shareName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ invitationName }}',
'{{ resourceGroupName }}',
'{{ shareName }}',
'{{ subscriptionId }}',
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
    - name: systemData
      value:
        - name: createdAt
          value: string
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: lastModifiedAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: expirationDate
          value: string
        - name: invitationId
          value: string
        - name: invitationStatus
          value: string
        - name: respondedAt
          value: string
        - name: sentAt
          value: string
        - name: targetActiveDirectoryId
          value: string
        - name: targetEmail
          value: string
        - name: targetObjectId
          value: string
        - name: userEmail
          value: string
        - name: userName
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>invitations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_share.invitations
WHERE accountName = '{{ accountName }}'
AND invitationName = '{{ invitationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND shareName = '{{ shareName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
