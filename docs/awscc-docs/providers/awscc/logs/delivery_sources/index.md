---
title: delivery_sources
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery_sources
  - logs
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>delivery_sources</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_sources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>delivery_sources</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.logs.delivery_sources</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The unique name of the Log source.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>delivery_sources</code> resource, the following permissions are required:

### Create
<pre>
logs:PutDeliverySource,
logs:GetDeliverySource,
logs:ListTagsForResource,
logs:TagResource,
logs:AllowVendedLogDeliveryForResource,
codewhisperer:AllowVendedLogDeliveryForResource,
autoloop:AllowVendedLogDeliveryForResource,
workmail:AllowVendedLogDeliveryForResource</pre>

### List
<pre>
logs:DescribeDeliverySources</pre>


## Example
```sql
SELECT
region,
name
FROM awscc.logs.delivery_sources
WHERE region = 'us-east-1'
```
