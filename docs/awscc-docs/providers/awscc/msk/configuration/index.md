---
title: configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration
  - msk
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>configuration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.msk.configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>server_properties</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>kafka_versions_list</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>latest_revision</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>configuration</code> resource, the following permissions are required:

### Delete
<pre>
kafka:DeleteConfiguration,
kafka:DescribeConfiguration</pre>

### Read
<pre>
kafka:DescribeConfiguration</pre>

### Update
<pre>
kafka:UpdateConfiguration,
kafka:DescribeConfiguration</pre>


## Example
```sql
SELECT
region,
name,
description,
server_properties,
kafka_versions_list,
arn,
latest_revision
FROM awscc.msk.configuration
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
