---
title: flow_entitlement
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_entitlement
  - mediaconnect
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>flow_entitlement</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow_entitlement</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>flow_entitlement</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.mediaconnect.flow_entitlement</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>flow_arn</code></td><td><code>string</code></td><td>The ARN of the flow.</td></tr>
<tr><td><code>entitlement_arn</code></td><td><code>string</code></td><td>The ARN of the entitlement.</td></tr>
<tr><td><code>data_transfer_subscriber_fee_percent</code></td><td><code>integer</code></td><td>Percentage from 0-100 of the data transfer cost to be billed to the subscriber.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>A description of the entitlement.</td></tr>
<tr><td><code>encryption</code></td><td><code>object</code></td><td>The type of encryption that will be used on the output that is associated with this entitlement.</td></tr>
<tr><td><code>entitlement_status</code></td><td><code>string</code></td><td> An indication of whether the entitlement is enabled.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the entitlement.</td></tr>
<tr><td><code>subscribers</code></td><td><code>array</code></td><td>The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>flow_entitlement</code> resource, the following permissions are required:

### Read
<pre>
mediaconnect:DescribeFlow</pre>

### Update
<pre>
mediaconnect:DescribeFlow,
mediaconnect:UpdateFlowEntitlement</pre>

### Delete
<pre>
mediaconnect:DescribeFlow,
mediaconnect:RevokeFlowEntitlement</pre>


## Example
```sql
SELECT
region,
flow_arn,
entitlement_arn,
data_transfer_subscriber_fee_percent,
description,
encryption,
entitlement_status,
name,
subscribers
FROM awscc.mediaconnect.flow_entitlement
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;EntitlementArn&gt;'
```
