---
title: billing_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - billing_groups
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
Retrieves a list of <code>billing_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>billing_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>billing_groups</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.billing_groups</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>billing_group_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>billing_groups</code> resource, the following permissions are required:

### Create
<pre>
iot:DescribeBillingGroup,
iot:ListTagsForResource,
iot:CreateBillingGroup,
iot:TagResource</pre>

### List
<pre>
iot:ListBillingGroups,
iot:ListTagsForResource</pre>


## Example
```sql
SELECT
region,
billing_group_name
FROM awscc.iot.billing_groups
WHERE region = 'us-east-1'
```