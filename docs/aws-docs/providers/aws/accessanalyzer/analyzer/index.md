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
Gets or operates on an individual <code>analyzer</code> resource, use <code>analyzers</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analyzer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AccessAnalyzer::Analyzer type specifies an analyzer of the user's account</td></tr>
<tr><td><b>Id</b></td><td><code>aws.accessanalyzer.analyzer</code></td></tr>
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

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
analyzer_name,
archive_rules,
arn,
tags,
type,
analyzer_configuration
FROM aws.accessanalyzer.analyzer
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>analyzer</code> resource, the following permissions are required:

### Read
```json
access-analyzer:ListAnalyzers,
access-analyzer:GetAnalyzer,
access-analyzer:ListArchiveRules
```

### Update
```json
access-analyzer:CreateArchiveRule,
access-analyzer:DeleteArchiveRule,
access-analyzer:ListAnalyzers,
access-analyzer:TagResource,
access-analyzer:UntagResource,
access-analyzer:UpdateArchiveRule
```

### Delete
```json
access-analyzer:DeleteAnalyzer
```

