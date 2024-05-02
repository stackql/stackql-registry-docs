---
title: assessment
hide_title: false
hide_table_of_contents: false
keywords:
  - assessment
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
Gets an individual <code>assessment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assessment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An entity that defines the scope of audit evidence collected by AWS Audit Manager.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.auditmanager.assessment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>framework_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>assessment_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>aws_account</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags associated with the assessment.</td></tr>
<tr><td><code>delegations</code></td><td><code>array</code></td><td>The list of delegations.</td></tr>
<tr><td><code>roles</code></td><td><code>array</code></td><td>The list of roles for the specified assessment.</td></tr>
<tr><td><code>scope</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>assessment_reports_destination</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>creation_time</code></td><td><code>number</code></td><td></td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td></td></tr>
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
framework_id,
assessment_id,
aws_account,
arn,
tags,
delegations,
roles,
scope,
assessment_reports_destination,
status,
creation_time,
name,
description
FROM aws.auditmanager.assessment
WHERE data__Identifier = '<AssessmentId>';
```

## Permissions

To operate on the <code>assessment</code> resource, the following permissions are required:

### Read
```json
auditmanager:GetAssessment
```

### Update
```json
auditmanager:UpdateAssessment,
auditmanager:UpdateAssessmentStatus,
auditmanager:BatchCreateDelegationByAssessment,
auditmanager:BatchDeleteDelegationByAssessment
```

### Delete
```json
auditmanager:DeleteAssessment
```

