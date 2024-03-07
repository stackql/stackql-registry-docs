---
title: multiplexes
hide_title: false
hide_table_of_contents: false
keywords:
  - multiplexes
  - medialive
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>multiplexes</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multiplexes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>multiplexes</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.medialive.multiplexes</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The unique id of the multiplex.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>multiplexes</code> resource, the following permissions are required:

### Create
<pre>
medialive:CreateMultiplex,
medialive:DescribeMultiplex,
medialive:CreateTags</pre>

### List
<pre>
medialive:ListMultiplexes</pre>


## Example
```sql
SELECT
region,
id
FROM awscc.medialive.multiplexes
WHERE region = 'us-east-1'
```
