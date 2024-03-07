---
title: input
hide_title: false
hide_table_of_contents: false
keywords:
  - input
  - iotevents
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>input</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>input</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>input</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotevents.input</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>input_definition</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>input_description</code></td><td><code>string</code></td><td>A brief description of the input.</td></tr>
<tr><td><code>input_name</code></td><td><code>string</code></td><td>The name of the input.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;For more information, see &#91;Tag&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;AWSCloudFormation&#x2F;latest&#x2F;UserGuide&#x2F;aws-properties-resource-tags.html).</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>input</code> resource, the following permissions are required:

### Read
<pre>
iotevents:DescribeInput,
iotevents:ListTagsForResource</pre>

### Update
<pre>
iotevents:UpdateInput,
iotevents:DescribeInput,
iotevents:ListTagsForResource,
iotevents:UntagResource,
iotevents:TagResource</pre>

### Delete
<pre>
iotevents:DeleteInput,
iotevents:DescribeInput</pre>


## Example
```sql
SELECT
region,
input_definition,
input_description,
input_name,
tags
FROM awscc.iotevents.input
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;InputName&gt;'
```
