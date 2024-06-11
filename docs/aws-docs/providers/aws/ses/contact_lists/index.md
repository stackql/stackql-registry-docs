---
title: contact_lists
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_lists
  - ses
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

Creates, updates, deletes or gets a <code>contact_list</code> resource or lists <code>contact_lists</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_lists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::SES::ContactList.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ses.contact_lists" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="contact_list_name" /></td><td><code>string</code></td><td>The name of the contact list.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the contact list.</td></tr>
<tr><td><CopyableCode code="topics" /></td><td><code>array</code></td><td>The topics associated with the contact list.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags (keys and values) associated with the contact list.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>contact_lists</code> in a region.
```sql
SELECT
region,
contact_list_name
FROM aws.ses.contact_lists
WHERE region = 'us-east-1';
```
Gets all properties from a <code>contact_list</code>.
```sql
SELECT
region,
contact_list_name,
description,
topics,
tags
FROM aws.ses.contact_lists
WHERE region = 'us-east-1' AND data__Identifier = '<ContactListName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>contact_list</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ses.contact_lists (
 ContactListName,
 Description,
 Topics,
 Tags,
 region
)
SELECT 
'{{ ContactListName }}',
 '{{ Description }}',
 '{{ Topics }}',
 '{{ Tags }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ses.contact_lists (
 ContactListName,
 Description,
 Topics,
 Tags,
 region
)
SELECT 
 '{{ ContactListName }}',
 '{{ Description }}',
 '{{ Topics }}',
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
  - name: contact_list
    props:
      - name: ContactListName
        value: '{{ ContactListName }}'
      - name: Description
        value: '{{ Description }}'
      - name: Topics
        value:
          - TopicName: '{{ TopicName }}'
            DisplayName: '{{ DisplayName }}'
            Description: '{{ Description }}'
            DefaultSubscriptionStatus: '{{ DefaultSubscriptionStatus }}'
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
DELETE FROM aws.ses.contact_lists
WHERE data__Identifier = '<ContactListName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>contact_lists</code> resource, the following permissions are required:

### Create
```json
ses:CreateContactList
```

### Read
```json
ses:GetContactList
```

### Update
```json
ses:UpdateContactList,
ses:UntagResource,
ses:TagResource
```

### Delete
```json
ses:DeleteContactList
```

### List
```json
ses:ListContactLists
```

