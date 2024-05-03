---
title: access_grants
hide_title: false
hide_table_of_contents: false
keywords:
  - access_grants
  - s3
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

Used to retrieve a list of <code>access_grants</code> in a region or create a <code>access_grants</code> resource, use <code>access_grant</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_grants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::S3::AccessGrant resource is an Amazon S3 resource type representing permissions to a specific S3 bucket or prefix hosted in an S3 Access Grants instance.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.access_grants" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="access_grant_id" /></td><td><code>string</code></td><td>The ID assigned to this access grant.</td></tr>
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
access_grant_id
FROM aws.s3.access_grants
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>access_grants</code> resource, the following permissions are required:

### Create
```json
s3:CreateAccessGrant,
s3:TagResource
```

### List
```json
s3:ListAccessGrants
```

