---
title: fuota_tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - fuota_tasks
  - iotwireless
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>fuota_tasks</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fuota_tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>fuota_tasks</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iotwireless.fuota_tasks</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>FUOTA task id. Returned after successful create.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>fuota_tasks</code> resource, the following permissions are required:

### Create
<pre>
iotwireless:CreateFuotaTask,
iotwireless:TagResource,
iotwireless:ListTagsForResource,
iam:GetRole,
iam:PassRole</pre>

### List
<pre>
iotwireless:ListFuotaTasks,
iotwireless:ListTagsForResource</pre>


## Example
```sql
SELECT
region,
id
FROM awscc.iotwireless.fuota_tasks
WHERE region = 'us-east-1'
```
