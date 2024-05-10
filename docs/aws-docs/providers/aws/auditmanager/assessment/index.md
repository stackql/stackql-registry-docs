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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>assessment</code> resource, use <code>assessments</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assessment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An entity that defines the scope of audit evidence collected by AWS Audit Manager.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.auditmanager.assessment" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="framework_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="assessment_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="aws_account" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags associated with the assessment.</td></tr>
<tr><td><CopyableCode code="delegations" /></td><td><code>array</code></td><td>The list of delegations.</td></tr>
<tr><td><CopyableCode code="roles" /></td><td><code>array</code></td><td>The list of roles for the specified assessment.</td></tr>
<tr><td><CopyableCode code="scope" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="assessment_reports_destination" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
WHERE region = 'us-east-1' AND data__Identifier = '<AssessmentId>';
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

