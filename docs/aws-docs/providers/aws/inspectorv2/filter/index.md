---
title: filter
hide_title: false
hide_table_of_contents: false
keywords:
  - filter
  - inspectorv2
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>filter</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>filter</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>filter</td></tr>
<tr><td><b>Id</b></td><td><code>aws.inspectorv2.filter</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>Findings filter name.</td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>Findings filter description.</td></tr>
<tr><td><code>filter_criteria</code></td><td><code>object</code></td><td>Findings filter criteria.</td></tr>
<tr><td><code>filter_action</code></td><td><code>string</code></td><td>Findings filter action.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Findings filter ARN.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
name,
description,
filter_criteria,
filter_action,
arn
FROM aws.inspectorv2.filter
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
