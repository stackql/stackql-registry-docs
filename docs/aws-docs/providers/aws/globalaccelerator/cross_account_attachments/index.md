---
title: cross_account_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - cross_account_attachments
  - globalaccelerator
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

Creates, updates, deletes or gets a <code>cross_account_attachment</code> resource or lists <code>cross_account_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cross_account_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GlobalAccelerator::CrossAccountAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.globalaccelerator.cross_account_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The Friendly identifier of the attachment.</td></tr>
<tr><td><CopyableCode code="attachment_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the attachment.</td></tr>
<tr><td><CopyableCode code="principals" /></td><td><code>array</code></td><td>Principals to share the resources with.</td></tr>
<tr><td><CopyableCode code="resources" /></td><td><code>array</code></td><td>Resources shared using the attachment.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, region" /></td>
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
Gets all <code>cross_account_attachments</code> in a region.
```sql
SELECT
region,
name,
attachment_arn,
principals,
resources,
tags
FROM aws.globalaccelerator.cross_account_attachments
;
```
Gets all properties from an individual <code>cross_account_attachment</code>.
```sql
SELECT
region,
name,
attachment_arn,
principals,
resources,
tags
FROM aws.globalaccelerator.cross_account_attachments
WHERE data__Identifier = '<AttachmentArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>cross_account_attachment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.globalaccelerator.cross_account_attachments (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.globalaccelerator.cross_account_attachments (
 Name,
 Principals,
 Resources,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Principals }}',
 '{{ Resources }}',
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
  - name: cross_account_attachment
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Principals
        value:
          - '{{ Principals[0] }}'
      - name: Resources
        value:
          - EndpointId: '{{ EndpointId }}'
            Region: '{{ Region }}'
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
DELETE FROM aws.globalaccelerator.cross_account_attachments
WHERE data__Identifier = '<AttachmentArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>cross_account_attachments</code> resource, the following permissions are required:

### Create
```json
globalaccelerator:DescribeCrossAccountAttachment,
globalaccelerator:CreateCrossAccountAttachment,
globalaccelerator:TagResource
```

### Read
```json
globalaccelerator:DescribeCrossAccountAttachment
```

### Update
```json
globalaccelerator:UpdateCrossAccountAttachment,
globalaccelerator:DescribeCrossAccountAttachment,
globalaccelerator:TagResource,
globalaccelerator:UntagResource
```

### Delete
```json
globalaccelerator:DescribeCrossAccountAttachment,
globalaccelerator:DeleteCrossAccountAttachment
```

### List
```json
globalaccelerator:ListCrossAccountAttachments
```

