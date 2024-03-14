---
title: billing_group
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_group
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>billing_group</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>billing_group</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.billing_group</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>billing_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>billing_group_properties</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
id,
arn,
billing_group_name,
tags,
billing_group_properties
FROM awscc.iot.billing_group
WHERE data__Identifier = '<BillingGroupName>';
```

## Permissions

To operate on the <code>billing_group</code> resource, the following permissions are required:

### Delete
```json
iot:DescribeBillingGroup,
iot:DeleteBillingGroup
```

### Read
```json
iot:DescribeBillingGroup,
iot:ListTagsForResource
```

### Update
```json
iot:DescribeBillingGroup,
iot:UpdateBillingGroup,
iot:ListTagsForResource,
iot:TagResource,
iot:UntagResource
```

