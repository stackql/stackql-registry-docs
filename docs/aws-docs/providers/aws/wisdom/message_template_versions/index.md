---
title: message_template_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - message_template_versions
  - wisdom
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

Creates, updates, deletes or gets a <code>message_template_version</code> resource or lists <code>message_template_versions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>message_template_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A version for the specified customer-managed message template within the specified knowledge base.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wisdom.message_template_versions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="message_template_arn" /></td><td><code>string</code></td><td>The unqualified Amazon Resource Name (ARN) of the message template.</td></tr>
<tr><td><CopyableCode code="message_template_version_arn" /></td><td><code>string</code></td><td>The unqualified Amazon Resource Name (ARN) of the message template version.</td></tr>
<tr><td><CopyableCode code="message_template_content_sha256" /></td><td><code>string</code></td><td>The content SHA256 of the message template.</td></tr>
<tr><td><CopyableCode code="message_template_version_number" /></td><td><code>number</code></td><td>Current version number of the message template.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-wisdom-messagetemplateversion.html"><code>AWS::Wisdom::MessageTemplateVersion</code></a>.

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
    <td><CopyableCode code="MessageTemplateArn, region" /></td>
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
Gets all <code>message_template_versions</code> in a region.
```sql
SELECT
region,
message_template_arn,
message_template_version_arn,
message_template_content_sha256,
message_template_version_number
FROM aws.wisdom.message_template_versions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>message_template_version</code>.
```sql
SELECT
region,
message_template_arn,
message_template_version_arn,
message_template_content_sha256,
message_template_version_number
FROM aws.wisdom.message_template_versions
WHERE region = 'us-east-1' AND data__Identifier = '<MessageTemplateVersionArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>message_template_version</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.wisdom.message_template_versions (
 MessageTemplateArn,
 region
)
SELECT 
'{{ MessageTemplateArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.wisdom.message_template_versions (
 MessageTemplateArn,
 MessageTemplateContentSha256,
 region
)
SELECT 
 '{{ MessageTemplateArn }}',
 '{{ MessageTemplateContentSha256 }}',
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
  - name: message_template_version
    props:
      - name: MessageTemplateArn
        value: '{{ MessageTemplateArn }}'
      - name: MessageTemplateContentSha256
        value: '{{ MessageTemplateContentSha256 }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.wisdom.message_template_versions
WHERE data__Identifier = '<MessageTemplateVersionArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>message_template_versions</code> resource, the following permissions are required:

### Create
```json
wisdom:CreateMessageTemplateVersion,
wisdom:ListMessageTemplateVersions
```

### Delete
```json
wisdom:DeleteMessageTemplate
```

### Update
```json
wisdom:CreateMessageTemplateVersion
```

### List
```json
wisdom:ListMessageTemplateVersions
```

### Read
```json
wisdom:GetMessageTemplate
```
