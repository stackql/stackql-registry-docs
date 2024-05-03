---
title: application_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - application_instances
  - panorama
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

Used to retrieve a list of <code>application_instances</code> in a region or create a <code>application_instances</code> resource, use <code>application_instance</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Schema for ApplicationInstance CloudFormation Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.panorama.application_instances" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="application_instance_id" /></td><td><code>undefined</code></td><td></td></tr>
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
application_instance_id
FROM aws.panorama.application_instances
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>application_instances</code> resource, the following permissions are required:

### Create
```json
panorama:CreateApplicationInstance,
panorama:ListTagsForResource,
panorama:TagResource,
panorama:DescribeApplicationInstance,
panorama:DescribeApplicationInstanceDetails,
iam:PassRole,
s3:ListBucket,
s3:PutObject,
s3:GetObject,
s3:GetObjectVersion
```

### List
```json
panorama:ListApplicationInstances,
s3:ListBucket,
s3:GetObject,
s3:GetObjectVersion
```

