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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets a <code>delegated_admin</code> resource or lists <code>delegated_admins</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delegated_admins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::SecurityHub::DelegatedAdmin</code> resource designates the delegated ASHlong administrator account for an organization. You must enable the integration between ASH and AOlong before you can designate a delegated ASH administrator. Only the management account for an organization can designate the delegated ASH administrator account. For more information, see &#91;Designating the delegated administrator&#93;(https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html#designate-admin-instructions) in the *User Guide*.<br />To change the delegated administrator account, remove the current delegated administrator account, and then designate the new account.<br />To designate multiple delegated administrators in different organizations and AWS-Regions, we recommend using &#91;mappings&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/mappings-section-structure.html).<br />Tags aren't supported for this resource.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.delegated_admins" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="delegated_admin_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="admin_account_id" /></td><td><code>string</code></td><td>The AWS-account identifier of the account to designate as the Security Hub administrator account.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-delegatedadmin.html"><code>AWS::SecurityHub::DelegatedAdmin</code></a>.

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
    <td><CopyableCode code="AdminAccountId, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>delegated_admins</code> in a region.
```sql
SELECT
region,
delegated_admin_identifier,
admin_account_id,
status
FROM aws.securityhub.delegated_admins
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>delegated_admin</code>.
```sql
SELECT
region,
delegated_admin_identifier,
admin_account_id,
status
FROM aws.securityhub.delegated_admins
WHERE region = 'us-east-1' AND data__Identifier = '<DelegatedAdminIdentifier>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>delegated_admin</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.securityhub.delegated_admins (
 AdminAccountId,
 region
)
SELECT 
'{{ AdminAccountId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.securityhub.delegated_admins (
 AdminAccountId,
 region
)
SELECT 
 '{{ AdminAccountId }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: delegated_admin
    props:
      - name: AdminAccountId
        value: '{{ AdminAccountId }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.securityhub.delegated_admins
WHERE data__Identifier = '<DelegatedAdminIdentifier>'
AND region = 'us-east-1';
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

### List
```json
securityhub:ListOrganizationAdminAccounts,
organizations:DescribeOrganization
```
