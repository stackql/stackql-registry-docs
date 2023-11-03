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
null
<tr><td><b>Id</b></td><td><code>aws.ssm.association</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AssociationId</code></td><td><code>string</code></td><td>Unique identifier of the association.</td></tr><tr><td><code>AssociationName</code></td><td><code>string</code></td><td>The name of the association.</td></tr><tr><td><code>DocumentVersion</code></td><td><code>string</code></td><td>The version of the SSM document to associate with the target.</td></tr><tr><td><code>InstanceId</code></td><td><code>string</code></td><td>The ID of the instance that the SSM document is associated with.</td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td>The name of the SSM document.</td></tr><tr><td><code>Parameters</code></td><td><code>object</code></td><td>Parameter values that the SSM document uses at runtime.</td></tr><tr><td><code>ScheduleExpression</code></td><td><code>string</code></td><td>A Cron or Rate expression that specifies when the association is applied to the target.</td></tr><tr><td><code>Targets</code></td><td><code>array</code></td><td>The targets that the SSM document sends commands to.</td></tr><tr><td><code>OutputLocation</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>AutomationTargetParameterName</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MaxErrors</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MaxConcurrency</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ComplianceSeverity</code></td><td><code>string</code></td><td></td></tr><tr><td><code>SyncCompliance</code></td><td><code>string</code></td><td></td></tr><tr><td><code>WaitForSuccessTimeoutSeconds</code></td><td><code>integer</code></td><td></td></tr><tr><td><code>ApplyOnlyAtCronInterval</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>CalendarNames</code></td><td><code>array</code></td><td></td></tr><tr><td><code>ScheduleOffset</code></td><td><code>integer</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.ssm.association
WHERE region = 'us-east-1' AND data__Identifier = '<AssociationId>'
</pre>
