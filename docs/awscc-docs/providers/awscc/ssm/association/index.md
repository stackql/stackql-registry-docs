---
title: association
hide_title: false
hide_table_of_contents: false
keywords:
  - association
  - ssm
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>association</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>association</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.ssm.association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>association_id</code></td><td><code>string</code></td><td>Unique identifier of the association.</td></tr>
<tr><td><code>association_name</code></td><td><code>string</code></td><td>The name of the association.</td></tr>
<tr><td><code>document_version</code></td><td><code>string</code></td><td>The version of the SSM document to associate with the target.</td></tr>
<tr><td><code>instance_id</code></td><td><code>string</code></td><td>The ID of the instance that the SSM document is associated with.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the SSM document.</td></tr>
<tr><td><code>parameters</code></td><td><code>object</code></td><td>Parameter values that the SSM document uses at runtime.</td></tr>
<tr><td><code>schedule_expression</code></td><td><code>string</code></td><td>A Cron or Rate expression that specifies when the association is applied to the target.</td></tr>
<tr><td><code>targets</code></td><td><code>array</code></td><td>The targets that the SSM document sends commands to.</td></tr>
<tr><td><code>output_location</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>automation_target_parameter_name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>max_errors</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>max_concurrency</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>compliance_severity</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>sync_compliance</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>wait_for_success_timeout_seconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>apply_only_at_cron_interval</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>calendar_names</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>schedule_offset</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>association</code> resource, the following permissions are required:

### Delete
<pre>
ssm:DeleteAssociation</pre>

### Update
<pre>
iam:PassRole,
ssm:UpdateAssociation,
ssm:GetCalendarState</pre>

### Read
<pre>
ssm:DescribeAssociation,
resource-groups:GetGroupQuery,
resource-groups:ListGroups,
resource-groups:ListGroupResources</pre>


## Example
```sql
SELECT
region,
association_id,
association_name,
document_version,
instance_id,
name,
parameters,
schedule_expression,
targets,
output_location,
automation_target_parameter_name,
max_errors,
max_concurrency,
compliance_severity,
sync_compliance,
wait_for_success_timeout_seconds,
apply_only_at_cron_interval,
calendar_names,
schedule_offset
FROM awscc.ssm.association
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;AssociationId&gt;'
```
