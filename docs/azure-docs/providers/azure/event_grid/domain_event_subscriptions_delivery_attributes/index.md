---
title: domain_event_subscriptions_delivery_attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - domain_event_subscriptions_delivery_attributes
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

Creates, updates, deletes, gets or lists a <code>domain_event_subscriptions_delivery_attributes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domain_event_subscriptions_delivery_attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.domain_event_subscriptions_delivery_attributes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of the delivery attribute or header. |
| <CopyableCode code="type" /> | `string` | Type of the delivery attribute or header name. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="domainName, eventSubscriptionName, resourceGroupName, subscriptionId" /> | Get all delivery attributes for an event subscription for domain. |

## `SELECT` examples

Get all delivery attributes for an event subscription for domain.


```sql
SELECT
name,
type
FROM azure.event_grid.domain_event_subscriptions_delivery_attributes
WHERE domainName = '{{ domainName }}'
AND eventSubscriptionName = '{{ eventSubscriptionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```