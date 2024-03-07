---
title: discoverers
hide_title: false
hide_table_of_contents: false
keywords:
  - discoverers
  - eventschemas
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>discoverers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>discoverers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>discoverers</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.eventschemas.discoverers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>discoverer_arn</code></td><td><code>string</code></td><td>The ARN of the discoverer.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>discoverers</code> resource, the following permissions are required:

### Create
<pre>
schemas:CreateDiscoverer,
schemas:DescribeDiscoverer,
schemas:TagResource,
events:PutRule,
events:PutTargets,
events:EnableRule,
events:ListTargetsByRule,
iam:CreateServiceLinkedRole</pre>

### List
<pre>
schemas:ListDiscoverers</pre>


## Example
```sql
SELECT
region,
discoverer_arn
FROM awscc.eventschemas.discoverers
WHERE region = 'us-east-1'
```