---
title: shared_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_private_link_resources
  - signalr
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

Creates, updates, deletes, gets or lists a <code>shared_private_link_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>shared_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.signalr.shared_private_link_resources" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_shared_private_link_resources', value: 'view', },
        { label: 'shared_private_link_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="fqdns" /> | `text` | field from the `properties` object |
| <CopyableCode code="group_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="private_link_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="request_message" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="sharedPrivateLinkResourceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Describes the properties of an existing Shared Private Link Resource |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, sharedPrivateLinkResourceName, subscriptionId" /> | Get the specified shared private link resource |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, resourceName, subscriptionId" /> | List shared private link resources |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, resourceName, sharedPrivateLinkResourceName, subscriptionId" /> | Create or update a shared private link resource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, resourceName, sharedPrivateLinkResourceName, subscriptionId" /> | Delete the specified shared private link resource |

## `SELECT` examples

List shared private link resources

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_shared_private_link_resources', value: 'view', },
        { label: 'shared_private_link_resources', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
fqdns,
group_id,
private_link_resource_id,
provisioning_state,
request_message,
resourceGroupName,
resourceName,
sharedPrivateLinkResourceName,
status,
subscriptionId
FROM azure.signalr.vw_shared_private_link_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.signalr.shared_private_link_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>shared_private_link_resources</code> resource.

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
INSERT INTO azure.signalr.shared_private_link_resources (
resourceGroupName,
resourceName,
sharedPrivateLinkResourceName,
subscriptionId,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ sharedPrivateLinkResourceName }}',
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
        - name: groupId
          value: string
        - name: privateLinkResourceId
          value: string
        - name: provisioningState
          value: []
        - name: requestMessage
          value: string
        - name: fqdns
          value:
            - string
        - name: status
          value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>shared_private_link_resources</code> resource.

```sql
/*+ delete */
DELETE FROM azure.signalr.shared_private_link_resources
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND sharedPrivateLinkResourceName = '{{ sharedPrivateLinkResourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
