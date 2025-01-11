---
title: email_addresses
hide_title: false
hide_table_of_contents: false
keywords:
  - email_addresses
  - connect
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

Creates, updates, deletes or gets an <code>email_address</code> resource or lists <code>email_addresses</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>email_addresses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Connect::EmailAddress</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.connect.email_addresses" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The identifier of the Amazon Connect instance.</td></tr>
<tr><td><CopyableCode code="email_address_arn" /></td><td><code>string</code></td><td>The identifier of the email address.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description for the email address.</td></tr>
<tr><td><CopyableCode code="email_address" /></td><td><code>string</code></td><td>Email address to be created for this instance</td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td>The display name for the email address.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>One or more tags.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-connect-emailaddress.html"><code>AWS::Connect::EmailAddress</code></a>.

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
    <td><CopyableCode code="InstanceArn, EmailAddress, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
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
Gets all <code>email_addresses</code> in a region.
```sql
SELECT
region,
instance_arn,
email_address_arn,
description,
email_address,
display_name,
tags
FROM aws.connect.email_addresses
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>email_address</code>.
```sql
SELECT
region,
instance_arn,
email_address_arn,
description,
email_address,
display_name,
tags
FROM aws.connect.email_addresses
WHERE region = 'us-east-1' AND data__Identifier = '<EmailAddressArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>email_address</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.connect.email_addresses (
 InstanceArn,
 EmailAddress,
 region
)
SELECT 
'{{ InstanceArn }}',
 '{{ EmailAddress }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.connect.email_addresses (
 InstanceArn,
 Description,
 EmailAddress,
 DisplayName,
 Tags,
 region
)
SELECT 
 '{{ InstanceArn }}',
 '{{ Description }}',
 '{{ EmailAddress }}',
 '{{ DisplayName }}',
 '{{ Tags }}',
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
  - name: email_address
    props:
      - name: InstanceArn
        value: '{{ InstanceArn }}'
      - name: Description
        value: '{{ Description }}'
      - name: EmailAddress
        value: '{{ EmailAddress }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.connect.email_addresses
WHERE data__Identifier = '<EmailAddressArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>email_addresses</code> resource, the following permissions are required:

### Create
```json
connect:CreateEmailAddress,
connect:TagResource,
connect:ListIntegrationAssociations,
ses:GetEmailIdentity,
ses:DescribeReceiptRule,
ses:UpdateReceiptRule,
iam:PassRole
```

### Read
```json
connect:DescribeEmailAddress
```

### Update
```json
connect:UpdateEmailAddressMetadata,
connect:TagResource,
connect:UntagResource
```

### Delete
```json
connect:DeleteEmailAddress,
connect:UntagResource,
iam:PassRole,
ses:DescribeReceiptRule,
ses:UpdateReceiptRule
```

### List
```json
connect:DescribeEmailAddress,
connect:SearchEmailAddresses
```
