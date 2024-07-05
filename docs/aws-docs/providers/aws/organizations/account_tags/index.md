---
title: account_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - account_tags
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Expands all tag keys and values for <code>accounts</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>You can use AWS::Organizations::Account to manage accounts in organization.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.organizations.account_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_name" /></td><td><code>string</code></td><td>The friendly name of the member account.</td></tr>
<tr><td><CopyableCode code="email" /></td><td><code>string</code></td><td>The email address of the owner to assign to the new member account.</td></tr>
<tr><td><CopyableCode code="role_name" /></td><td><code>string</code></td><td>The name of an IAM role that AWS Organizations automatically preconfigures in the new member account. Default name is OrganizationAccountAccessRole if not specified.</td></tr>
<tr><td><CopyableCode code="parent_ids" /></td><td><code>array</code></td><td>List of parent nodes for the member account. Currently only one parent at a time is supported. Default is root.</td></tr>
<tr><td><CopyableCode code="account_id" /></td><td><code>string</code></td><td>If the account was created successfully, the unique identifier (ID) of the new account.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the account.</td></tr>
<tr><td><CopyableCode code="joined_method" /></td><td><code>string</code></td><td>The method by which the account joined the organization.</td></tr>
<tr><td><CopyableCode code="joined_timestamp" /></td><td><code>string</code></td><td>The date the account became a part of the organization.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the account in the organization.</td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>accounts</code> in a region.
```sql
SELECT
region,
account_name,
email,
role_name,
parent_ids,
account_id,
arn,
joined_method,
joined_timestamp,
status,
tag_key,
tag_value
FROM aws.organizations.account_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>account_tags</code> resource, see <a href="/providers/aws/organizations/accounts/#permissions"><code>accounts</code></a>


