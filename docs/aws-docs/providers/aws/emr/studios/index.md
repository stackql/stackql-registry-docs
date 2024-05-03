---
title: studios
hide_title: false
hide_table_of_contents: false
keywords:
  - studios
  - emr
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

Used to retrieve a list of <code>studios</code> in a region or create a <code>studios</code> resource, use <code>studio</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studios</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::EMR::Studio</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emr.studios" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td>The ID of the EMR Studio.</td></tr>
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
studio_id
FROM aws.emr.studios
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>studios</code> resource, the following permissions are required:

### Create
```json
elasticmapreduce:CreateStudio,
elasticmapreduce:DescribeStudio,
elasticmapreduce:AddTags,
sso:CreateManagedApplicationInstance,
sso:DeleteManagedApplicationInstance,
iam:PassRole
```

### List
```json
elasticmapreduce:ListStudios
```

