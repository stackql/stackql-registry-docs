---
title: delegated_admin
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_admin
  - securityhub
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets or operates on an individual <code>delegated_admin</code> resource, use <code>delegated_admins</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delegated_admin</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::DelegatedAdmin resource represents the AWS Security Hub delegated admin account in your organization. One delegated admin resource is allowed to create for the organization in each region in which you configure the AdminAccountId.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.securityhub.delegated_admin</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>delegated_admin_identifier</code></td><td><code>string</code></td><td>The identifier of the DelegatedAdmin being created and assigned as the unique identifier</td></tr>
<tr><td><code>admin_account_id</code></td><td><code>string</code></td><td>The Amazon Web Services account identifier of the account to designate as the Security Hub administrator account</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The current status of the Security Hub administrator account. Indicates whether the account is currently enabled as a Security Hub administrator</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
delegated_admin_identifier,
admin_account_id,
status
FROM aws.securityhub.delegated_admin
WHERE data__Identifier = '<DelegatedAdminIdentifier>';
```

## Permissions

To operate on the <code>delegated_admin</code> resource, the following permissions are required:

### Read
```json
securityhub:ListOrganizationAdminAccounts,
organizations:DescribeOrganization
```

### Delete
```json
securityhub:DisableOrganizationAdminAccount,
organizations:DescribeOrganization
```

