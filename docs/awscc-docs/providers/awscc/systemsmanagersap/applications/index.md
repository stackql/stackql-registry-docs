---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
  - systemsmanagersap
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>applications</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>applications</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.systemsmanagersap.applications</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the Helix application</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>applications</code> resource, the following permissions are required:

### Create
<pre>
ssm-sap:RegisterApplication,
ssm-sap:GetApplication,
ssm-sap:TagResource,
ssm-sap:ListTagsForResource</pre>

### List
<pre>
ssm-sap:ListApplications</pre>


## Example
```sql
SELECT
region,
arn
FROM awscc.systemsmanagersap.applications
WHERE region = 'us-east-1'
```
