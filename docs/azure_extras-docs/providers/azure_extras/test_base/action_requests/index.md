---
title: action_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - action_requests
  - test_base
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

Creates, updates, deletes, gets or lists a <code>action_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>action_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.action_requests" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_action_requests', value: 'view', },
        { label: 'action_requests', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="actionRequestName" /> | `text` | field from the `properties` object |
| <CopyableCode code="creation_date" /> | `text` | field from the `properties` object |
| <CopyableCode code="pre_release_access_request_spec" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="request_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` |  |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="actionRequestName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Get the action request under the specified test base account. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | List all action requests under the specified test base account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="actionRequestName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Delete (revoke) an action request. Only requests in review can be deleted. |
| <CopyableCode code="put" /> | `REPLACE` | <CopyableCode code="actionRequestName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Create (submit) an action request. |

## `SELECT` examples

List all action requests under the specified test base account.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_action_requests', value: 'view', },
        { label: 'action_requests', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
actionRequestName,
creation_date,
pre_release_access_request_spec,
provisioning_state,
request_type,
resourceGroupName,
status,
subscriptionId,
testBaseAccountName
FROM azure_extras.test_base.vw_action_requests
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.action_requests
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>


## `REPLACE` example

Replaces all fields in the specified <code>action_requests</code> resource.

```sql
/*+ update */
REPLACE azure_extras.test_base.action_requests
SET 
properties = '{{ properties }}'
WHERE 
actionRequestName = '{{ actionRequestName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```

## `DELETE` example

Deletes the specified <code>action_requests</code> resource.

```sql
/*+ delete */
DELETE FROM azure_extras.test_base.action_requests
WHERE actionRequestName = '{{ actionRequestName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
