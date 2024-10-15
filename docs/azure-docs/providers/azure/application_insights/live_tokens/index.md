---
title: live_tokens
hide_title: false
hide_table_of_contents: false
keywords:
  - live_tokens
  - application_insights
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

Creates, updates, deletes, gets or lists a <code>live_tokens</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>live_tokens</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.application_insights.live_tokens" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="liveToken" /> | `string` | JWT token for accessing live metrics stream data. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceUri" /> | **Gets an access token for live metrics stream data.** |

## `SELECT` examples

**Gets an access token for live metrics stream data.**


```sql
SELECT
liveToken
FROM azure.application_insights.live_tokens
WHERE resourceUri = '{{ resourceUri }}';
```