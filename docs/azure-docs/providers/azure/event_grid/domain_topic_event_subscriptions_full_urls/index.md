---
title: domain_topic_event_subscriptions_full_urls
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_topic_event_subscriptions_full_urls
  - event_grid
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

Creates, updates, deletes, gets or lists a <code>domain_topic_event_subscriptions_full_urls</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_topic_event_subscriptions_full_urls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.domain_topic_event_subscriptions_full_urls" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="endpointUrl" /> | `string` | The URL that represents the endpoint of the destination of an event subscription. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, eventSubscriptionName, resourceGroupName, subscriptionId, topicName" /> | Get the full endpoint URL for a nested event subscription for domain topic. |

## `SELECT` examples

Get the full endpoint URL for a nested event subscription for domain topic.


```sql
SELECT
endpointUrl
FROM azure.event_grid.domain_topic_event_subscriptions_full_urls
WHERE domainName = '{{ domainName }}'
AND eventSubscriptionName = '{{ eventSubscriptionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND topicName = '{{ topicName }}';
```