---
title: findings_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - findings_filters
  - macie
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>findings_filters</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>findings_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>findings_filters</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.macie.findings_filters</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>Findings filter ID.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>findings_filters</code> resource, the following permissions are required:

### Create
<pre>
macie2:GetFindingsFilter,
macie2:CreateFindingsFilter,
macie2:TagResource</pre>

### List
<pre>
macie2:ListFindingsFilters</pre>


## Example
```sql
SELECT
region,
id
FROM awscc.macie.findings_filters
WHERE region = 'us-east-1'
```
