---
title: database
hide_title: false
hide_table_of_contents: false
keywords:
  - database
  - timestream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>database</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>database</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>database</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.timestream.database</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>database_name</code></td><td><code>string</code></td><td>The name for the database. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the database name.</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>The KMS key for the database. If the KMS key is not specified, the database will be encrypted with a Timestream managed KMS key located in your account.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>database</code> resource, the following permissions are required:

### Read
<pre>
timestream:DescribeDatabase,
timestream:DescribeEndpoints,
timestream:ListTagsForResource</pre>

### Update
<pre>
timestream:UpdateDatabase,
timestream:DescribeDatabase,
timestream:DescribeEndpoints,
timestream:TagResource,
timestream:UntagResource</pre>

### Delete
<pre>
timestream:DeleteDatabase,
timestream:DescribeEndpoints</pre>


## Example
```sql
SELECT
region,
arn,
database_name,
kms_key_id,
tags
FROM awscc.timestream.database
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DatabaseName&gt;'
```
