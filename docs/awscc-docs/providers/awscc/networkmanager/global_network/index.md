---
title: global_network
hide_title: false
hide_table_of_contents: false
keywords:
  - global_network
  - networkmanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>global_network</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>global_network</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>global_network</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.networkmanager.global_network</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the global network.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The ID of the global network.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>The description of the global network.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags for the global network.</td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td>The date and time that the global network was created.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td>The state of the global network.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>global_network</code> resource, the following permissions are required:

### Read
<pre>
networkmanager:DescribeGlobalNetworks</pre>

### Update
<pre>
networkmanager:UpdateGlobalNetwork,
networkmanager:DescribeGlobalNetworks,
networkmanager:TagResource,
networkmanager:UntagResource,
networkmanager:ListTagsForResource</pre>

### Delete
<pre>
networkmanager:DeleteGlobalNetwork,
networkmanager:DescribeGlobalNetworks</pre>


## Example
```sql
SELECT
region,
arn,
id,
description,
tags,
created_at,
state
FROM awscc.networkmanager.global_network
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
