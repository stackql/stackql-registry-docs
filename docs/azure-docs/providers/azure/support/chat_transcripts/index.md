---
title: chat_transcripts
hide_title: false
hide_table_of_contents: false
keywords:
  - chat_transcripts
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

Creates, updates, deletes, gets or lists a <code>chat_transcripts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>chat_transcripts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.support.chat_transcripts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_chat_transcripts', value: 'view', },
        { label: 'chat_transcripts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="chatTranscriptName" /> | `text` | field from the `properties` object |
| <CopyableCode code="messages" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="chatTranscriptName, subscriptionId, supportTicketName" /> | Returns chatTranscript details for a support ticket under a subscription. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId, supportTicketName" /> | Lists all chat transcripts for a support ticket under subscription |

## `SELECT` examples

Lists all chat transcripts for a support ticket under subscription

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_chat_transcripts', value: 'view', },
        { label: 'chat_transcripts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
chatTranscriptName,
messages,
start_time,
subscriptionId,
supportTicketName
FROM azure.support.vw_chat_transcripts
WHERE subscriptionId = '{{ subscriptionId }}'
AND supportTicketName = '{{ supportTicketName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.support.chat_transcripts
WHERE subscriptionId = '{{ subscriptionId }}'
AND supportTicketName = '{{ supportTicketName }}';
```
</TabItem></Tabs>

