---
title: settings
hide_title: false
hide_table_of_contents: false
keywords:
  - settings
  - contactcenterinsights
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

Creates, updates, deletes, gets or lists a <code>settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contactcenterinsights.settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the settings resource. Format: projects/{project}/locations/{location}/settings |
| <CopyableCode code="analysisConfig" /> | `object` | Default configuration when creating Analyses in Insights. |
| <CopyableCode code="conversationTtl" /> | `string` | The default TTL for newly-created conversations. If a conversation has a specified expiration, that value will be used instead. Changing this value will not change the expiration of existing conversations. Conversations with no expire time persist until they are deleted. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which the settings was created. |
| <CopyableCode code="languageCode" /> | `string` | A language code to be applied to each transcript segment unless the segment already specifies a language code. Language code defaults to "en-US" if it is neither specified on the segment nor here. |
| <CopyableCode code="pubsubNotificationSettings" /> | `object` | A map that maps a notification trigger to a Pub/Sub topic. Each time a specified trigger occurs, Insights will notify the corresponding Pub/Sub topic. Keys are notification triggers. Supported keys are: * "all-triggers": Notify each time any of the supported triggers occurs. * "create-analysis": Notify each time an analysis is created. * "create-conversation": Notify each time a conversation is created. * "export-insights-data": Notify each time an export is complete. * "ingest-conversations": Notify each time an IngestConversations LRO is complete. * "update-conversation": Notify each time a conversation is updated via UpdateConversation. * "upload-conversation": Notify when an UploadConversation LRO is complete. Values are Pub/Sub topics. The format of each Pub/Sub topic is: projects/{project}/topics/{topic} |
| <CopyableCode code="redactionConfig" /> | `object` | DLP resources used for redaction while ingesting conversations. DLP settings are applied to conversations ingested from the `UploadConversation` and `IngestConversations` endpoints, including conversation coming from CCAI Platform. They are not applied to conversations ingested from the `CreateConversation` endpoint or the Dialogflow / Agent Assist runtime integrations. When using Dialogflow / Agent Assist runtime integrations, redaction should be performed in Dialogflow / Agent Assist. |
| <CopyableCode code="speechConfig" /> | `object` | Speech-to-Text configuration. Speech-to-Text settings are applied to conversations ingested from the `UploadConversation` and `IngestConversations` endpoints, including conversation coming from CCAI Platform. They are not applied to conversations ingested from the `CreateConversation` endpoint. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time at which the settings were last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_settings" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Gets project-level settings. |
| <CopyableCode code="update_settings" /> | `UPDATE` | <CopyableCode code="locationsId, projectsId" /> | Updates project-level settings. |

## `SELECT` examples

Gets project-level settings.

```sql
SELECT
name,
analysisConfig,
conversationTtl,
createTime,
languageCode,
pubsubNotificationSettings,
redactionConfig,
speechConfig,
updateTime
FROM google.contactcenterinsights.settings
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a <code>settings</code> resource.

```sql
/*+ update */
UPDATE google.contactcenterinsights.settings
SET 
name = '{{ name }}',
analysisConfig = '{{ analysisConfig }}',
languageCode = '{{ languageCode }}',
redactionConfig = '{{ redactionConfig }}',
speechConfig = '{{ speechConfig }}',
conversationTtl = '{{ conversationTtl }}',
pubsubNotificationSettings = '{{ pubsubNotificationSettings }}'
WHERE 
locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
