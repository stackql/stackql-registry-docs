---
title: assessment_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - assessment_tags
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

Expands all tag keys and values for <code>assessments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assessment_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An entity that defines the scope of audit evidence collected by AWS Audit Manager.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.auditmanager.assessment_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="framework_id" /></td><td><code>string</code></td><td>The identifier for the specified framework.</td></tr>
<tr><td><CopyableCode code="assessment_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="aws_account" /></td><td><code>object</code></td><td>The AWS account associated with the assessment.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the assessment.</td></tr>
<tr><td><CopyableCode code="delegations" /></td><td><code>array</code></td><td>The list of delegations.</td></tr>
<tr><td><CopyableCode code="roles" /></td><td><code>array</code></td><td>The list of roles for the specified assessment.</td></tr>
<tr><td><CopyableCode code="scope" /></td><td><code>object</code></td><td>The wrapper that contains the AWS accounts and AWS services in scope for the assessment.</td></tr>
<tr><td><CopyableCode code="assessment_reports_destination" /></td><td><code>object</code></td><td>The destination in which evidence reports are stored for the specified assessment.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the specified assessment.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>number</code></td><td>The sequence of characters that identifies when the event occurred.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the related assessment.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the specified assessment.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>assessments</code> in a region.
```sql
SELECT
region,
framework_id,
assessment_id,
aws_account,
arn,
delegations,
roles,
scope,
assessment_reports_destination,
status,
creation_time,
name,
description,
tag_key,
tag_value
FROM aws.auditmanager.assessment_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>assessment_tags</code> resource, see <a href="/providers/aws/auditmanager/assessments/#permissions"><code>assessments</code></a>


