---
title: subscriber_usage_aggregates
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriber_usage_aggregates
  - commerce_admin
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

Creates, updates, deletes, gets or lists a <code>subscriber_usage_aggregates</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriber_usage_aggregates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.commerce_admin.subscriber_usage_aggregates" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | URI of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location where resource is location. |
| <CopyableCode code="properties" /> | `object` | Properties for aggregate usage. |
| <CopyableCode code="tags" /> | `object` | List of key-value pairs. |
| <CopyableCode code="type" /> | `string` | Type of resource. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="reportedEndTime, reportedStartTime, subscriptionId" /> | Gets a collection of SubscriberUsageAggregates, which are UsageAggregates from users. |

## `SELECT` examples

Gets a collection of SubscriberUsageAggregates, which are UsageAggregates from users.


```sql
SELECT
id,
name,
location,
properties,
tags,
type
FROM azure_stack.commerce_admin.subscriber_usage_aggregates
WHERE reportedEndTime = '{{ reportedEndTime }}'
AND reportedStartTime = '{{ reportedStartTime }}'
AND subscriptionId = '{{ subscriptionId }}';
```