---
title: access_grants_locations
hide_title: false
hide_table_of_contents: false
keywords:
  - access_grants_locations
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

Used to retrieve a list of <code>access_grants_locations</code> in a region or create a <code>access_grants_locations</code> resource, use <code>access_grants_location</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_grants_locations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::S3::AccessGrantsLocation resource is an Amazon S3 resource type hosted in an access grants instance which can be the target of S3 access grants.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.s3.access_grants_locations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="access_grants_location_id" /></td><td><code>string</code></td><td>The unique identifier for the specified Access Grants location.</td></tr>
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
access_grants_location_id
FROM aws.s3.access_grants_locations
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>access_grants_locations</code> resource, the following permissions are required:

### Create
```json
s3:CreateAccessGrantsLocation,
iam:PassRole,
s3:TagResource
```

### List
```json
s3:ListAccessGrantsLocations
```

