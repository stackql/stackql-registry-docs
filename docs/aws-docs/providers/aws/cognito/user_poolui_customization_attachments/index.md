---
title: user_poolui_customization_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - user_poolui_customization_attachments
  - cognito
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

Creates, updates, deletes or gets an <code>user_poolui_customization_attachment</code> resource or lists <code>user_poolui_customization_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_poolui_customization_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Cognito::UserPoolUICustomizationAttachment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cognito.user_poolui_customization_attachments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="user_pool_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="client_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="c_ss" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooluicustomizationattachment.html"><code>AWS::Cognito::UserPoolUICustomizationAttachment</code></a>.

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
    <td><CopyableCode code="UserPoolId, ClientId, region" /></td>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples

Gets all properties from an individual <code>user_poolui_customization_attachment</code>.
```sql
SELECT
region,
user_pool_id,
client_id,
c_ss
FROM aws.cognito.user_poolui_customization_attachments
WHERE region = 'us-east-1' AND data__Identifier = '<UserPoolId>|<ClientId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>user_poolui_customization_attachment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.cognito.user_poolui_customization_attachments (
 UserPoolId,
 ClientId,
 region
)
SELECT 
'{{ UserPoolId }}',
 '{{ ClientId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.cognito.user_poolui_customization_attachments (
 UserPoolId,
 ClientId,
 CSS,
 region
)
SELECT 
 '{{ UserPoolId }}',
 '{{ ClientId }}',
 '{{ CSS }}',
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
  - name: user_poolui_customization_attachment
    props:
      - name: UserPoolId
        value: '{{ UserPoolId }}'
      - name: ClientId
        value: '{{ ClientId }}'
      - name: CSS
        value: '{{ CSS }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.cognito.user_poolui_customization_attachments
WHERE data__Identifier = '<UserPoolId|ClientId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>user_poolui_customization_attachments</code> resource, the following permissions are required:

### Create
```json
cognito-idp:SetUICustomization,
cognito-idp:GetUICustomization
```

### Read
```json
cognito-idp:GetUICustomization
```

### Update
```json
cognito-idp:SetUICustomization
```

### Delete
```json
cognito-idp:SetUICustomization,
cognito-idp:GetUICustomization
```
