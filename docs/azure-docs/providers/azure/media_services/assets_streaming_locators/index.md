---
title: assets_streaming_locators
hide_title: false
hide_table_of_contents: false
keywords:
  - assets_streaming_locators
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

Creates, updates, deletes, gets or lists a <code>assets_streaming_locators</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets_streaming_locators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.media_services.assets_streaming_locators" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="streamingLocators" /> | `array` | The list of Streaming Locators. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, assetName, resourceGroupName, subscriptionId" /> | Lists Streaming Locators which are associated with this asset. |

## `SELECT` examples

Lists Streaming Locators which are associated with this asset.


```sql
SELECT
streamingLocators
FROM azure.media_services.assets_streaming_locators
WHERE accountName = '{{ accountName }}'
AND assetName = '{{ assetName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```