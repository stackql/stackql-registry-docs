---
title: access_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - access_policy
  - iotsitewise
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

Gets or operates on an individual <code>access_policy</code> resource, use <code>access_policies</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>access_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::IoTSiteWise::AccessPolicy</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotsitewise.access_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="access_policy_id" /></td><td><code>string</code></td><td>The ID of the access policy.</td></tr>
<tr><td><CopyableCode code="access_policy_arn" /></td><td><code>string</code></td><td>The ARN of the access policy.</td></tr>
<tr><td><CopyableCode code="access_policy_identity" /></td><td><code>object</code></td><td>The identity for this access policy. Choose either a user or a group but not both.</td></tr>
<tr><td><CopyableCode code="access_policy_permission" /></td><td><code>string</code></td><td>The permission level for this access policy. Valid values are ADMINISTRATOR or VIEWER.</td></tr>
<tr><td><CopyableCode code="access_policy_resource" /></td><td><code>object</code></td><td>The AWS IoT SiteWise Monitor resource for this access policy. Choose either portal or project but not both.</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
access_policy_id,
access_policy_arn,
access_policy_identity,
access_policy_permission,
access_policy_resource
FROM aws.iotsitewise.access_policy
WHERE data__Identifier = '<AccessPolicyId>';
```

## Permissions

To operate on the <code>access_policy</code> resource, the following permissions are required:

### Read
```json
iotsitewise:DescribeAccessPolicy
```

### Update
```json
iotsitewise:DescribeAccessPolicy,
iotsitewise:UpdateAccessPolicy
```

### Delete
```json
iotsitewise:DescribeAccessPolicy,
iotsitewise:DeleteAccessPolicy
```

