---
title: product_subscription
hide_title: false
hide_table_of_contents: false
keywords:
  - product_subscription
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


Gets or updates an individual <code>product_subscription</code> resource, use <code>product_subscriptions</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product_subscription</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::ProductSubscription resource represents a subscription to a service that is allowed to generate findings for your Security Hub account. One product subscription resource is created for each product enabled.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.product_subscription" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="product_arn" /></td><td><code>string</code></td><td>The generic ARN of the product being subscribed to</td></tr>
<tr><td><CopyableCode code="product_subscription_arn" /></td><td><code>string</code></td><td>The ARN of the product subscription for the account</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
product_arn,
product_subscription_arn
FROM aws.securityhub.product_subscription
WHERE region = 'us-east-1' AND data__Identifier = '<ProductSubscriptionArn>';
```


## Permissions

To operate on the <code>product_subscription</code> resource, the following permissions are required:

### Read
```json
securityhub:ListEnabledProductsForImport
```

