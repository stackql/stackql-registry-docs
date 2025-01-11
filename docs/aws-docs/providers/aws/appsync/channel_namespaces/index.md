---
title: channel_namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - channel_namespaces
  - appsync
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

Creates, updates, deletes or gets a <code>channel_namespace</code> resource or lists <code>channel_namespaces</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channel_namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AppSync ChannelNamespace</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appsync.channel_namespaces" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="api_id" /></td><td><code>string</code></td><td>AppSync Api Id that this Channel Namespace belongs to.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Namespace indentifier.</td></tr>
<tr><td><CopyableCode code="subscribe_auth_modes" /></td><td><code>array</code></td><td>List of AuthModes supported for Subscribe operations.</td></tr>
<tr><td><CopyableCode code="publish_auth_modes" /></td><td><code>array</code></td><td>List of AuthModes supported for Publish operations.</td></tr>
<tr><td><CopyableCode code="code_handlers" /></td><td><code>string</code></td><td>String of APPSYNC_JS code to be used by the handlers.</td></tr>
<tr><td><CopyableCode code="code_s3_location" /></td><td><code>string</code></td><td>The Amazon S3 endpoint where the code is located.</td></tr>
<tr><td><CopyableCode code="channel_namespace_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the Channel Namespace.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this AppSync API.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appsync-channelnamespace.html"><code>AWS::AppSync::ChannelNamespace</code></a>.

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
    <td><CopyableCode code="ApiId, Name, region" /></td>
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
Gets all <code>channel_namespaces</code> in a region.
```sql
SELECT
region,
api_id,
name,
subscribe_auth_modes,
publish_auth_modes,
code_handlers,
code_s3_location,
channel_namespace_arn,
tags
FROM aws.appsync.channel_namespaces
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>channel_namespace</code>.
```sql
SELECT
region,
api_id,
name,
subscribe_auth_modes,
publish_auth_modes,
code_handlers,
code_s3_location,
channel_namespace_arn,
tags
FROM aws.appsync.channel_namespaces
WHERE region = 'us-east-1' AND data__Identifier = '<ChannelNamespaceArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>channel_namespace</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.appsync.channel_namespaces (
 ApiId,
 Name,
 region
)
SELECT 
'{{ ApiId }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appsync.channel_namespaces (
 ApiId,
 Name,
 SubscribeAuthModes,
 PublishAuthModes,
 CodeHandlers,
 CodeS3Location,
 Tags,
 region
)
SELECT 
 '{{ ApiId }}',
 '{{ Name }}',
 '{{ SubscribeAuthModes }}',
 '{{ PublishAuthModes }}',
 '{{ CodeHandlers }}',
 '{{ CodeS3Location }}',
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
  - name: channel_namespace
    props:
      - name: ApiId
        value: '{{ ApiId }}'
      - name: Name
        value: '{{ Name }}'
      - name: SubscribeAuthModes
        value:
          - AuthType: '{{ AuthType }}'
      - name: PublishAuthModes
        value: null
      - name: CodeHandlers
        value: '{{ CodeHandlers }}'
      - name: CodeS3Location
        value: '{{ CodeS3Location }}'
      - name: Tags
        value:
          - Value: '{{ Value }}'
            Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.appsync.channel_namespaces
WHERE data__Identifier = '<ChannelNamespaceArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>channel_namespaces</code> resource, the following permissions are required:

### Create
```json
appsync:CreateChannelNamespace,
appsync:TagResource,
appsync:GetChannelNamespace,
s3:GetObject
```

### Read
```json
appsync:GetChannelNamespace,
appsync:ListTagsForResource
```

### Update
```json
appsync:UpdateChannelNamespace,
appsync:TagResource,
appsync:UntagResource,
appsync:GetChannelNamespace,
s3:GetObject
```

### Delete
```json
appsync:DeleteChannelNamespace,
appsync:UntagResource
```

### List
```json
appsync:ListChannelNamespaces
```
