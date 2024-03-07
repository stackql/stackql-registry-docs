---
title: organization_admin
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_admin
  - detective
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>organization_admin</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_admin</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>organization_admin</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.detective.organization_admin</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td>The account ID of the account that should be registered as your Organization's delegated administrator for Detective</td></tr>
<tr><td><code>graph_arn</code></td><td><code>string</code></td><td>The Detective graph ARN</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
account_id,
graph_arn
FROM awscc.detective.organization_admin
WHERE region = 'us-east-1'
AND data__Identifier = '{AccountId}';
```

## Permissions

To operate on the <code>organization_admin</code> resource, the following permissions are required:

### Read
```json
detective:ListOrganizationAdminAccount,
organizations:DescribeOrganization
```

### Delete
```json
detective:DisableOrganizationAdminAccount,
detective:ListOrganizationAdminAccount,
organizations:DescribeOrganization
```

