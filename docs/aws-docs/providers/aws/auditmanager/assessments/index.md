---
title: assessments
hide_title: false
hide_table_of_contents: false
keywords:
  - assessments
  - auditmanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>assessments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assessments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.auditmanager.assessments</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>FrameworkId</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>AssessmentId</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>AwsAccount</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Arn</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>The tags associated with the assessment.</td></tr><tr><td><code>Delegations</code></td><td><code>array</code></td><td>The list of delegations.</td></tr><tr><td><code>Roles</code></td><td><code>array</code></td><td>The list of roles for the specified assessment.</td></tr><tr><td><code>Scope</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>AssessmentReportsDestination</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Status</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>CreationTime</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Name</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>Description</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.auditmanager.assessments
WHERE region = 'us-east-1'
</pre>
