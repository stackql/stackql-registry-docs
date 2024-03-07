---
title: filter
hide_title: false
hide_table_of_contents: false
keywords:
  - filter
  - guardduty
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
<tr><td><b>Id</b></td><td><code>awscc.guardduty.filter</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>action</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>detector_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>finding_criteria</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>rank</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>filter</code> resource, the following permissions are required:

### Read
<pre>
guardduty:GetFilter</pre>

### Delete
<pre>
guardduty:ListDetectors,
guardduty:ListFilters,
guardduty:GetFilter,
guardduty:DeleteFilter</pre>

### Update
<pre>
guardduty:UpdateFilter,
guardduty:GetFilter,
guardduty:ListFilters</pre>


## Example
```sql
SELECT
region,
action,
description,
detector_id,
finding_criteria,
rank,
name,
tags
FROM awscc.guardduty.filter
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DetectorId&gt;'
AND data__Identifier = '&lt;Name&gt;'
```
