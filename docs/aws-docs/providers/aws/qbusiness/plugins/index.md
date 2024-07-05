---
title: plugins
hide_title: false
hide_table_of_contents: false
keywords:
  - plugins
  - qbusiness
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

Creates, updates, deletes or gets a <code>plugin</code> resource or lists <code>plugins</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>plugins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::QBusiness::Plugin Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.qbusiness.plugins" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auth_configuration" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="build_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_plugin_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="plugin_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="plugin_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="server_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="ApplicationId, AuthConfiguration, DisplayName, Type, region" /></td>
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
Gets all <code>plugins</code> in a region.
```sql
SELECT
region,
application_id,
auth_configuration,
build_status,
created_at,
custom_plugin_configuration,
display_name,
plugin_arn,
plugin_id,
server_url,
state,
tags,
type,
updated_at
FROM aws.qbusiness.plugins
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>plugin</code>.
```sql
SELECT
region,
application_id,
auth_configuration,
build_status,
created_at,
custom_plugin_configuration,
display_name,
plugin_arn,
plugin_id,
server_url,
state,
tags,
type,
updated_at
FROM aws.qbusiness.plugins
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>|<PluginId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>plugin</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.qbusiness.plugins (
 ApplicationId,
 AuthConfiguration,
 DisplayName,
 Type,
 region
)
SELECT 
'{{ ApplicationId }}',
 '{{ AuthConfiguration }}',
 '{{ DisplayName }}',
 '{{ Type }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.qbusiness.plugins (
 ApplicationId,
 AuthConfiguration,
 CustomPluginConfiguration,
 DisplayName,
 ServerUrl,
 State,
 Tags,
 Type,
 region
)
SELECT 
 '{{ ApplicationId }}',
 '{{ AuthConfiguration }}',
 '{{ CustomPluginConfiguration }}',
 '{{ DisplayName }}',
 '{{ ServerUrl }}',
 '{{ State }}',
 '{{ Tags }}',
 '{{ Type }}',
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
  - name: plugin
    props:
      - name: ApplicationId
        value: '{{ ApplicationId }}'
      - name: AuthConfiguration
        value: null
      - name: CustomPluginConfiguration
        value:
          Description: '{{ Description }}'
          ApiSchemaType: '{{ ApiSchemaType }}'
          ApiSchema: null
      - name: DisplayName
        value: '{{ DisplayName }}'
      - name: ServerUrl
        value: '{{ ServerUrl }}'
      - name: State
        value: '{{ State }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: Type
        value: '{{ Type }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.qbusiness.plugins
WHERE data__Identifier = '<ApplicationId|PluginId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>plugins</code> resource, the following permissions are required:

### Create
```json
iam:PassRole,
qbusiness:CreatePlugin,
qbusiness:GetPlugin,
qbusiness:ListTagsForResource,
qbusiness:TagResource,
qbusiness:UpdatePlugin
```

### Read
```json
qbusiness:GetPlugin,
qbusiness:ListTagsForResource
```

### Update
```json
iam:PassRole,
qbusiness:GetPlugin,
qbusiness:ListTagsForResource,
qbusiness:TagResource,
qbusiness:UntagResource,
qbusiness:UpdatePlugin
```

### Delete
```json
qbusiness:DeletePlugin,
qbusiness:GetPlugin
```

### List
```json
qbusiness:ListPlugins
```

