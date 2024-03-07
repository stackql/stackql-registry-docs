---
title: ip_sets
hide_title: false
hide_table_of_contents: false
keywords:
  - ip_sets
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
Retrieves a list of <code>ip_sets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>ip_sets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>ip_sets</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.guardduty.ip_sets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>detector_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>ip_sets</code> resource, the following permissions are required:

### Create
<pre>
guardduty:CreateIPSet,
guardduty:GetIPSet,
guardduty:TagResource,
iam:PutRolePolicy</pre>

### List
<pre>
guardduty:ListIPSets</pre>


## Example
```sql
SELECT
region,
id,
detector_id
FROM awscc.guardduty.ip_sets
WHERE region = 'us-east-1'
```
