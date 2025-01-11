---
title: event_data_stores_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - event_data_stores_list_only
  - cloudtrail
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>event_data_stores</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/event_data_stores/"><code>event_data_stores</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_data_stores_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A storage lake of event data against which you can run complex SQL-based queries. An event data store can include events that you have logged on your account from the last 7 to 2557 or 3653 days (about seven or ten years) depending on the selected BillingMode.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudtrail.event_data_stores_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="event_data_store_arn" /></td><td><code>string</code></td><td>The ARN of the event data store.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>event_data_stores</code> in a region.
```sql
SELECT
region,
event_data_store_arn
FROM aws.cloudtrail.event_data_stores_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>event_data_stores_list_only</code> resource, see <a href="/providers/aws/cloudtrail/event_data_stores/#permissions"><code>event_data_stores</code></a>

