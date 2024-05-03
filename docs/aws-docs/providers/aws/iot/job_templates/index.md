---
title: job_templates
hide_title: false
hide_table_of_contents: false
keywords:
  - job_templates
  - iot
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

Used to retrieve a list of <code>job_templates</code> in a region or create a <code>job_templates</code> resource, use <code>job_template</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_templates</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Job templates enable you to preconfigure jobs so that you can deploy them to multiple sets of target devices.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.job_templates" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="job_template_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
job_template_id
FROM aws.iot.job_templates
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>job_templates</code> resource, the following permissions are required:

### Create
```json
iot:CreateJobTemplate,
iam:PassRole,
s3:GetObject,
iot:TagResource
```

### List
```json
iot:ListJobTemplates
```

