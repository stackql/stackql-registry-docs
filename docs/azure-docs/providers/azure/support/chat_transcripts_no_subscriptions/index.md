---
title: chat_transcripts_no_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - chat_transcripts_no_subscriptions
  - support
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

Creates, updates, deletes, gets or lists a <code>chat_transcripts_no_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>chat_transcripts_no_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.support.chat_transcripts_no_subscriptions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_chat_transcripts_no_subscriptions', value: 'view', },
        { label: 'chat_transcripts_no_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="chatTranscriptName" /> | `text` | field from the `properties` object |
| <CopyableCode code="messages" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="supportTicketName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Describes the properties of a Chat Transcript Details resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="chatTranscriptName, supportTicketName" /> | Returns chatTranscript details for a no subscription support ticket. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="supportTicketName" /> | Lists all chat transcripts for a support ticket |

## `SELECT` examples

Lists all chat transcripts for a support ticket

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_chat_transcripts_no_subscriptions', value: 'view', },
        { label: 'chat_transcripts_no_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
chatTranscriptName,
messages,
start_time,
supportTicketName
FROM azure.support.vw_chat_transcripts_no_subscriptions
WHERE supportTicketName = '{{ supportTicketName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.support.chat_transcripts_no_subscriptions
WHERE supportTicketName = '{{ supportTicketName }}';
```
</TabItem></Tabs>

