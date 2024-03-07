---
title: multiplex
hide_title: false
hide_table_of_contents: false
keywords:
  - multiplex
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
Gets an individual <code>multiplex</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>multiplex</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>multiplex</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.medialive.multiplex</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The unique arn of the multiplex.</td></tr>
<tr><td><code>availability_zones</code></td><td><code>array</code></td><td>A list of availability zones for the multiplex.</td></tr>
<tr><td><code>destinations</code></td><td><code>array</code></td><td>A list of the multiplex output destinations.</td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The unique id of the multiplex.</td></tr>
<tr><td><code>multiplex_settings</code></td><td><code>object</code></td><td>Configuration for a multiplex event.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Name of multiplex.</td></tr>
<tr><td><code>pipelines_running_count</code></td><td><code>integer</code></td><td>The number of currently healthy pipelines.</td></tr>
<tr><td><code>program_count</code></td><td><code>integer</code></td><td>The number of programs in the multiplex.</td></tr>
<tr><td><code>state</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>A collection of key-value pairs.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>multiplex</code> resource, the following permissions are required:

### Read
<pre>
medialive:DescribeMultiplex</pre>

### Update
<pre>
medialive:UpdateMultiplex,
medialive:DescribeMultiplex,
medialive:CreateTags,
medialive:DeleteTags</pre>

### Delete
<pre>
medialive:DeleteMultiplex,
medialive:DescribeMultiplex</pre>


## Example
```sql
SELECT
region,
arn,
availability_zones,
destinations,
id,
multiplex_settings,
name,
pipelines_running_count,
program_count,
state,
tags
FROM awscc.medialive.multiplex
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
