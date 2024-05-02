---
title: delegated_admins
hide_title: false
hide_table_of_contents: false
keywords:
  - delegated_admins
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
Retrieves a list of <code>delegated_admins</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delegated_admins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::DelegatedAdmin resource represents the AWS Security Hub delegated admin account in your organization. One delegated admin resource is allowed to create for the organization in each region in which you configure the AdminAccountId.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.securityhub.delegated_admins</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>delegated_admin_identifier</code></td><td><code>string</code></td><td>The identifier of the DelegatedAdmin being created and assigned as the unique identifier</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
delegated_admin_identifier
FROM aws.securityhub.delegated_admins
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>delegated_admins</code> resource, the following permissions are required:

### Create
```json
securityhub:EnableOrganizationAdminAccount,
organizations:DescribeOrganization,
organizations:EnableAWSServiceAccess,
organizations:RegisterDelegatedAdministrator
```

### List
```json
securityhub:ListOrganizationAdminAccounts,
organizations:DescribeOrganization
```

