---
title: inputs
hide_title: false
hide_table_of_contents: false
keywords:
  - inputs
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
Retrieves a list of <code>inputs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>inputs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>inputs</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotevents.inputs</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>input_name</code></td><td><code>string</code></td><td>The name of the input.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>inputs</code> resource, the following permissions are required:

### Create
<pre>
iotevents:CreateInput,
iotevents:TagResource,
iotevents:DescribeInput,
iotevents:ListTagsForResource</pre>

### List
<pre>
iotevents:ListInputs</pre>


## Example
```sql
SELECT
region,
input_name
FROM awscc.iotevents.inputs
WHERE region = 'us-east-1'
```
