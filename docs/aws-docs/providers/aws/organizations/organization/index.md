---
title: organization
hide_title: false
hide_table_of_contents: false
keywords:
  - organization
  - organizations
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

Gets or operates on an individual <code>organization</code> resource, use <code>organizations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Organizations::Organization</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.organizations.organization" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique identifier (ID) of an organization.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an organization.</td></tr>
<tr><td><CopyableCode code="feature_set" /></td><td><code>string</code></td><td>Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.</td></tr>
<tr><td><CopyableCode code="management_account_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the account that is designated as the management account for the organization.</td></tr>
<tr><td><CopyableCode code="management_account_id" /></td><td><code>string</code></td><td>The unique identifier (ID) of the management account of an organization.</td></tr>
<tr><td><CopyableCode code="management_account_email" /></td><td><code>string</code></td><td>The email address that is associated with the AWS account that is designated as the management account for the organization.</td></tr>
<tr><td><CopyableCode code="root_id" /></td><td><code>string</code></td><td>The unique identifier (ID) for the root.</td></tr>
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
id,
arn,
feature_set,
management_account_arn,
management_account_id,
management_account_email,
root_id
FROM aws.organizations.organization
WHERE data__Identifier = '<Id>';
```

## Permissions

To operate on the <code>organization</code> resource, the following permissions are required:

### Read
```json
organizations:DescribeOrganization,
organizations:ListRoots
```

### Delete
```json
organizations:DeleteOrganization,
organizations:DescribeOrganization
```

