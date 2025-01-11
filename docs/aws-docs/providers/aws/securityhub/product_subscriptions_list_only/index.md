---
title: product_subscriptions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - product_subscriptions_list_only
  - securityhub
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

Lists <code>product_subscriptions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/product_subscriptions/"><code>product_subscriptions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product_subscriptions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::ProductSubscription resource represents a subscription to a service that is allowed to generate findings for your Security Hub account. One product subscription resource is created for each product enabled.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.product_subscriptions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="product_subscription_arn" /></td><td><code>string</code></td><td>The ARN of the product subscription for the account</td></tr>
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
Lists all <code>product_subscriptions</code> in a region.
```sql
SELECT
region,
product_subscription_arn
FROM aws.securityhub.product_subscriptions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>product_subscriptions_list_only</code> resource, see <a href="/providers/aws/securityhub/product_subscriptions/#permissions"><code>product_subscriptions</code></a>

