---
title: streaming_locators_paths
hide_title: false
hide_table_of_contents: false
keywords:
  - streaming_locators_paths
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

Creates, updates, deletes, gets or lists a <code>streaming_locators_paths</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>streaming_locators_paths</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.streaming_locators_paths" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="downloadPaths" /> | `array` | Download Paths supported by current Streaming Locator |
| <CopyableCode code="streamingPaths" /> | `array` | Streaming Paths supported by current Streaming Locator |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, streamingLocatorName, subscriptionId" /> | List Paths supported by this Streaming Locator |

## `SELECT` examples

List Paths supported by this Streaming Locator


```sql
SELECT
downloadPaths,
streamingPaths
FROM azure.media_services.streaming_locators_paths
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND streamingLocatorName = '{{ streamingLocatorName }}'
AND subscriptionId = '{{ subscriptionId }}';
```