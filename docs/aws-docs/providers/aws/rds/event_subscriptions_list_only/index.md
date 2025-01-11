---
title: event_subscriptions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - event_subscriptions_list_only
  - rds
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

Lists <code>event_subscriptions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/event_subscriptions/"><code>event_subscriptions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_subscriptions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::RDS::EventSubscription</code> resource allows you to receive notifications for Amazon Relational Database Service events through the Amazon Simple Notification Service (Amazon SNS). For more information, see &#91;Using Amazon RDS Event Notification&#93;(https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Events.html) in the *Amazon RDS User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.event_subscriptions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="subscription_name" /></td><td><code>string</code></td><td>The name of the subscription.<br />Constraints: The name must be less than 255 characters.</td></tr>
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
Lists all <code>event_subscriptions</code> in a region.
```sql
SELECT
region,
subscription_name
FROM aws.rds.event_subscriptions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>event_subscriptions_list_only</code> resource, see <a href="/providers/aws/rds/event_subscriptions/#permissions"><code>event_subscriptions</code></a>

