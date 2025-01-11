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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>product_subscription</code> resource or lists <code>product_subscriptions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>product_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::ProductSubscription resource represents a subscription to a service that is allowed to generate findings for your Security Hub account. One product subscription resource is created for each product enabled.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.product_subscriptions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="product_arn" /></td><td><code>string</code></td><td>The generic ARN of the product being subscribed to</td></tr>
<tr><td><CopyableCode code="product_subscription_arn" /></td><td><code>string</code></td><td>The ARN of the product subscription for the account</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-productsubscription.html"><code>AWS::SecurityHub::ProductSubscription</code></a>.

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
    <td><CopyableCode code="ProductArn, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>product_subscriptions</code> in a region.
```sql
SELECT
region,
product_arn,
product_subscription_arn
FROM aws.securityhub.product_subscriptions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>product_subscription</code>.
```sql
SELECT
region,
product_arn,
product_subscription_arn
FROM aws.securityhub.product_subscriptions
WHERE region = 'us-east-1' AND data__Identifier = '<ProductSubscriptionArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>product_subscription</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.securityhub.product_subscriptions (
 ProductArn,
 region
)
SELECT 
'{{ ProductArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.securityhub.product_subscriptions (
 ProductArn,
 region
)
SELECT 
 '{{ ProductArn }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: product_subscription
    props:
      - name: ProductArn
        value: '{{ ProductArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.securityhub.product_subscriptions
WHERE data__Identifier = '<ProductSubscriptionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>product_subscriptions</code> resource, the following permissions are required:

### Create
```json
securityhub:EnableImportFindingsForProduct
```

### Read
```json
securityhub:ListEnabledProductsForImport
```

### Delete
```json
securityhub:ListEnabledProductsForImport,
securityhub:DisableImportFindingsForProduct
```

### List
```json
securityhub:ListEnabledProductsForImport
```
