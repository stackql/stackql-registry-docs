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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>delegated_admin</code> resource, use <code>delegated_admins</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delegated_admin</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::DelegatedAdmin resource represents the AWS Security Hub delegated admin account in your organization. One delegated admin resource is allowed to create for the organization in each region in which you configure the AdminAccountId.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.delegated_admin" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="delegated_admin_identifier" /></td><td><code>string</code></td><td>The identifier of the DelegatedAdmin being created and assigned as the unique identifier</td></tr>
<tr><td><CopyableCode code="admin_account_id" /></td><td><code>string</code></td><td>The Amazon Web Services account identifier of the account to designate as the Security Hub administrator account</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The current status of the Security Hub administrator account. Indicates whether the account is currently enabled as a Security Hub administrator</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
WHERE region = 'us-east-1' AND data__Identifier = '<DelegatedAdminIdentifier>';
```


## Permissions

To operate on the <code>delegated_admin</code> resource, the following permissions are required:

### Read
```json
securityhub:ListOrganizationAdminAccounts,
organizations:DescribeOrganization
```

