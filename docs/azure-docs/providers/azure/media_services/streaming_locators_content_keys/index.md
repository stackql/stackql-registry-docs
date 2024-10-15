---
title: streaming_locators_content_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_locators_content_keys
  - media_services
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

Creates, updates, deletes, gets or lists a <code>streaming_locators_content_keys</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streaming_locators_content_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.streaming_locators_content_keys" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="contentKeys" /> | `array` | ContentKeys used by current Streaming Locator |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, streamingLocatorName, subscriptionId" /> | List Content Keys used by this Streaming Locator |

## `SELECT` examples

List Content Keys used by this Streaming Locator


```sql
SELECT
contentKeys
FROM azure.media_services.streaming_locators_content_keys
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND streamingLocatorName = '{{ streamingLocatorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```