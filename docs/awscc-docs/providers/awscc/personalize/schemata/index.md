---
title: schemata
hide_title: false
hide_table_of_contents: false
keywords:
  - schemata
  - personalize
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>schemata</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schemata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>schemata</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.personalize.schemata</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>schema_arn</code></td><td><code>string</code></td><td>Arn for the schema.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>schemata</code> resource, the following permissions are required:

### Create
<pre>
personalize:CreateSchema,
personalize:DescribeSchema</pre>

### List
<pre>
personalize:ListSchemas</pre>


## Example
```sql
SELECT
region,
schema_arn
FROM awscc.personalize.schemata
WHERE region = 'us-east-1'
```
