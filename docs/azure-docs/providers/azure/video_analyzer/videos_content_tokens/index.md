---
title: videos_content_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - videos_content_tokens
  - video_analyzer
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

Creates, updates, deletes, gets or lists a <code>videos_content_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>videos_content_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.video_analyzer.videos_content_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="expirationDate" /> | `string` | The content token expiration date in ISO8601 format (eg. 2021-01-01T00:00:00Z). |
| <CopyableCode code="token" /> | `string` | The content token value to be added to the video content URL as the value for the "token" query string parameter. The token is specific to a single video. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId, videoName" /> | Generates a streaming token which can be used for accessing content from video content URLs, for a video resource with the given name. |

## `SELECT` examples

Generates a streaming token which can be used for accessing content from video content URLs, for a video resource with the given name.


```sql
SELECT
expirationDate,
token
FROM azure.video_analyzer.videos_content_tokens
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND videoName = '{{ videoName }}';
```