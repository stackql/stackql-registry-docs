---
title: repository
hide_title: false
hide_table_of_contents: false
keywords:
  - repository
  - codecommit
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>repository</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repository</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>repository</td></tr>
<tr><td><b>Id</b></td><td><code>aws.codecommit.repository</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>clone_url_http</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>clone_url_ssh</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>repository_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>triggers</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>code</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>repository_description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
clone_url_http,
clone_url_ssh,
repository_name,
triggers,
id,
arn,
code,
repository_description,
tags,
name
FROM aws.codecommit.repository
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Id&gt;'
```
