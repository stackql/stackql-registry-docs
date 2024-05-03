---
title: product_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - product_subscriptions
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

Used to retrieve a list of <code>product_subscriptions</code> in a region or create a <code>product_subscriptions</code> resource, use <code>product_subscription</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::ProductSubscription resource represents a subscription to a service that is allowed to generate findings for your Security Hub account. One product subscription resource is created for each product enabled.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.product_subscriptions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
product_subscription_arn
FROM aws.securityhub.product_subscriptions
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>product_subscriptions</code> resource, the following permissions are required:

### Create
```json
securityhub:EnableImportFindingsForProduct
```

### List
```json
securityhub:ListEnabledProductsForImport
```

