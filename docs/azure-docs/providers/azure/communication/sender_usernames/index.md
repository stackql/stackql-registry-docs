---
title: sender_usernames
hide_title: false
hide_table_of_contents: false
keywords:
  - sender_usernames
  - communication
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

Creates, updates, deletes, gets or lists a <code>sender_usernames</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sender_usernames</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.communication.sender_usernames" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sender_usernames', value: 'view', },
        { label: 'sender_usernames', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="domainName" /> | `text` | field from the `properties` object |
| <CopyableCode code="emailServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="senderUsername" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="username" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A class that describes the properties of a SenderUsername resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, senderUsername, subscriptionId" /> | Get a valid sender username for a domains resource. |
| <CopyableCode code="list_by_domains" /> | `SELECT` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, subscriptionId" /> | List all valid sender usernames for a domains resource. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, senderUsername, subscriptionId" /> | Add a new SenderUsername resource under the parent Domains resource or update an existing SenderUsername resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="domainName, emailServiceName, resourceGroupName, senderUsername, subscriptionId" /> | Operation to delete a SenderUsernames resource. |

## `SELECT` examples

List all valid sender usernames for a domains resource.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_sender_usernames', value: 'view', },
        { label: 'sender_usernames', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
data_location,
display_name,
domainName,
emailServiceName,
provisioning_state,
resourceGroupName,
senderUsername,
subscriptionId,
username
FROM azure.communication.vw_sender_usernames
WHERE domainName = '{{ domainName }}'
AND emailServiceName = '{{ emailServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.communication.sender_usernames
WHERE domainName = '{{ domainName }}'
AND emailServiceName = '{{ emailServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>sender_usernames</code> resource.

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
INSERT INTO azure.communication.sender_usernames (
domainName,
emailServiceName,
resourceGroupName,
senderUsername,
subscriptionId,
properties
)
SELECT 
'{{ domainName }}',
'{{ emailServiceName }}',
'{{ resourceGroupName }}',
'{{ senderUsername }}',
'{{ subscriptionId }}',
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
        - name: dataLocation
          value: string
        - name: username
          value: string
        - name: displayName
          value: string
        - name: provisioningState
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>sender_usernames</code> resource.

```sql
/*+ delete */
DELETE FROM azure.communication.sender_usernames
WHERE domainName = '{{ domainName }}'
AND emailServiceName = '{{ emailServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND senderUsername = '{{ senderUsername }}'
AND subscriptionId = '{{ subscriptionId }}';
```
