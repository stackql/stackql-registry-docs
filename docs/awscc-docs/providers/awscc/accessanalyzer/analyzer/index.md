---
title: analyzer
hide_title: false
hide_table_of_contents: false
keywords:
  - analyzer
  - accessanalyzer
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>analyzer</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analyzer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>analyzer</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.accessanalyzer.analyzer</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>analyzer_name</code></td><td><code>string</code></td><td>Analyzer name</td></tr>
<tr><td><code>archive_rules</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the analyzer</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>type</code></td><td><code>string</code></td><td>The type of the analyzer, must be one of ACCOUNT, ORGANIZATION, ACCOUNT_UNUSED_ACCESS or ORGANIZATION_UNUSED_ACCESS</td></tr>
<tr><td><code>analyzer_configuration</code></td><td><code>object</code></td><td>The configuration for the analyzer</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>analyzer</code> resource, the following permissions are required:

### Read
<pre>
access-analyzer:ListAnalyzers,
access-analyzer:GetAnalyzer,
access-analyzer:ListArchiveRules</pre>

### Update
<pre>
access-analyzer:CreateArchiveRule,
access-analyzer:DeleteArchiveRule,
access-analyzer:ListAnalyzers,
access-analyzer:TagResource,
access-analyzer:UntagResource,
access-analyzer:UpdateArchiveRule</pre>

### Delete
<pre>
access-analyzer:DeleteAnalyzer</pre>


## Example
```sql
SELECT
region,
analyzer_name,
archive_rules,
arn,
tags,
type,
analyzer_configuration
FROM awscc.accessanalyzer.analyzer
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
