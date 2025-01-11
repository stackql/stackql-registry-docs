---
title: contacts
hide_title: false
hide_table_of_contents: false
keywords:
  - contacts
  - ssmcontacts
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

Creates, updates, deletes or gets a <code>contact</code> resource or lists <code>contacts</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contacts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SSMContacts::Contact</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmcontacts.contacts" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="alias" /></td><td><code>string</code></td><td>Alias of the contact. String value with 20 to 256 characters. Only alphabetical, numeric characters, dash, or underscore allowed.</td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td>Name of the contact. String value with 3 to 256 characters. Only alphabetical, space, numeric characters, dash, or underscore allowed.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>Contact type, which specify type of contact. Currently supported values: “PERSONAL”, “SHARED”, “OTHER“.</td></tr>
<tr><td><CopyableCode code="plan" /></td><td><code>array</code></td><td>The stages that an escalation plan or engagement plan engages contacts and contact methods in.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the contact.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssmcontacts-contact.html"><code>AWS::SSMContacts::Contact</code></a>.

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
    <td><CopyableCode code="Alias, DisplayName, Type, region" /></td>
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
Gets all <code>contacts</code> in a region.
```sql
SELECT
region,
alias,
display_name,
type,
plan,
arn
FROM aws.ssmcontacts.contacts
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>contact</code>.
```sql
SELECT
region,
alias,
display_name,
type,
plan,
arn
FROM aws.ssmcontacts.contacts
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>contact</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ssmcontacts.contacts (
 Alias,
 DisplayName,
 Type,
 region
)
SELECT 
'{{ Alias }}',
 '{{ DisplayName }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ssmcontacts.contacts (
 Alias,
 DisplayName,
 Type,
 Plan,
 region
)
SELECT 
 '{{ Alias }}',
 '{{ DisplayName }}',
 '{{ Type }}',
 '{{ Plan }}',
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
  - name: contact
    props:
      - name: Alias
        value: '{{ Alias }}'
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: Type
        value: '{{ Type }}'
      - name: Plan
        value:
          - DurationInMinutes: '{{ DurationInMinutes }}'
            Targets:
              - ContactTargetInfo:
                  ContactId: '{{ ContactId }}'
                  IsEssential: '{{ IsEssential }}'
                ChannelTargetInfo:
                  ChannelId: '{{ ChannelId }}'
                  RetryIntervalInMinutes: '{{ RetryIntervalInMinutes }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ssmcontacts.contacts
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>contacts</code> resource, the following permissions are required:

### Create
```json
ssm-contacts:CreateContact,
ssm-contacts:GetContact,
ssm-contacts:AssociateContact
```

### Read
```json
ssm-contacts:GetContact
```

### Update
```json
ssm-contacts:UpdateContact,
ssm-contacts:GetContact,
ssm-contacts:AssociateContact
```

### Delete
```json
ssm-contacts:DeleteContact,
ssm-contacts:GetContact,
ssm-contacts:AssociateContact
```

### List
```json
ssm-contacts:ListContacts
```
