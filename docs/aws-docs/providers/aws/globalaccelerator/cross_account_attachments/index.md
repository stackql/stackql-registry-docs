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


Used to retrieve a list of <code>cross_account_attachments</code> in a region or to create or delete a <code>cross_account_attachments</code> resource, use <code>cross_account_attachment</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cross_account_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GlobalAccelerator::CrossAccountAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.globalaccelerator.cross_account_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="attachment_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the attachment.</td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
attachment_arn
FROM aws.globalaccelerator.cross_account_attachments
;
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>cross_account_attachment</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- cross_account_attachment.iql (required properties only)
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
-- cross_account_attachment.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
globalaccelerator:DescribeCrossAccountAttachment,
globalaccelerator:DeleteCrossAccountAttachment
```

### List
```json
globalaccelerator:ListCrossAccountAttachments
```

