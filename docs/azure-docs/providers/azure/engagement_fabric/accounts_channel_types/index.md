---
title: accounts_channel_types
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts_channel_types
  - engagement_fabric
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

Creates, updates, deletes, gets or lists a <code>accounts_channel_types</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>accounts_channel_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.engagement_fabric.accounts_channel_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="channelDescription" /> | `string` | Text description for the channel |
| <CopyableCode code="channelFunctions" /> | `array` | All the available functions for the channel |
| <CopyableCode code="channelType" /> | `string` | Channel type |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
channelDescription,
channelFunctions,
channelType
FROM azure.engagement_fabric.accounts_channel_types
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```