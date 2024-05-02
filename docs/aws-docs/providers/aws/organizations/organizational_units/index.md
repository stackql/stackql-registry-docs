---
title: organizational_units
hide_title: false
hide_table_of_contents: false
keywords:
  - organizational_units
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
Retrieves a list of <code>organizational_units</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organizational_units</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>You can use organizational units (OUs) to group accounts together to administer as a single unit. This greatly simplifies the management of your accounts. For example, you can attach a policy-based control to an OU, and all accounts within the OU automatically inherit the policy. You can create multiple OUs within a single organization, and you can create OUs within other OUs. Each OU can contain multiple accounts, and you can move accounts from one OU to another. However, OU names must be unique within a parent OU or root.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.organizations.organizational_units</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td>The unique identifier (ID) associated with this OU.</td></tr>
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
id
FROM aws.organizations.organizational_units
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>organizational_units</code> resource, the following permissions are required:

### Create
```json
organizations:CreateOrganizationalUnit,
organizations:DescribeOrganizationalUnit,
organizations:ListParents,
organizations:ListTagsForResource,
organizations:TagResource
```

### List
```json
organizations:ListOrganizationalUnitsForParent
```

