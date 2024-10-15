---
title: chat_sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - chat_sessions
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

Creates, updates, deletes, gets or lists a <code>chat_sessions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>chat_sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.test_base.chat_sessions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_chat_sessions', value: 'view', },
        { label: 'chat_sessions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="chatSessionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="testBaseAccountName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | The chat session properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="chatSessionName, resourceGroupName, subscriptionId, testBaseAccountName" /> | Get a chat session |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, testBaseAccountName" /> | List all chat sessions |
| <CopyableCode code="chat" /> | `EXEC` | <CopyableCode code="chatSessionName, resourceGroupName, subscriptionId, testBaseAccountName, data__question" /> | Start a new chat turn. Ask a question and see the answer in response. |

## `SELECT` examples

List all chat sessions

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_chat_sessions', value: 'view', },
        { label: 'chat_sessions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
chatSessionName,
provisioning_state,
resourceGroupName,
subscriptionId,
testBaseAccountName
FROM azure_extras.test_base.vw_chat_sessions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure_extras.test_base.chat_sessions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND testBaseAccountName = '{{ testBaseAccountName }}';
```
</TabItem></Tabs>

