---
title: destinations
hide_title: false
hide_table_of_contents: false
keywords:
  - destinations
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
Retrieves a list of <code>destinations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>destinations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>destinations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.logs.destinations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>destination_name</code></td><td><code>string</code></td><td>The name of the destination resource</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>destinations</code> resource, the following permissions are required:

### Create
```json
logs:PutDestination,
logs:PutDestinationPolicy,
logs:DescribeDestinations,
iam:PassRole
```

### List
```json
logs:DescribeDestinations
```


## Example
```sql
SELECT
region,
destination_name
FROM awscc.logs.destinations
WHERE region = 'us-east-1'
```
