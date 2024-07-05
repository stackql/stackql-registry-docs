---
title: custom_plugins
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_plugins
  - kafkaconnect
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

Creates, updates, deletes or gets a <code>custom_plugin</code> resource or lists <code>custom_plugins</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_plugins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kafkaconnect.custom_plugins" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the custom plugin.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A summary description of the custom plugin.</td></tr>
<tr><td><CopyableCode code="custom_plugin_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the custom plugin to use.</td></tr>
<tr><td><CopyableCode code="content_type" /></td><td><code>string</code></td><td>The type of the plugin file.</td></tr>
<tr><td><CopyableCode code="file_description" /></td><td><code>object</code></td><td>Details about the custom plugin file.</td></tr>
<tr><td><CopyableCode code="location" /></td><td><code>object</code></td><td>Information about the location of a custom plugin.</td></tr>
<tr><td><CopyableCode code="revision" /></td><td><code>integer</code></td><td>The revision of the custom plugin.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="Name, ContentType, Location, region" /></td>
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
Gets all <code>custom_plugins</code> in a region.
```sql
SELECT
region,
name,
description,
custom_plugin_arn,
content_type,
file_description,
location,
revision,
tags
FROM aws.kafkaconnect.custom_plugins
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>custom_plugin</code>.
```sql
SELECT
region,
name,
description,
custom_plugin_arn,
content_type,
file_description,
location,
revision,
tags
FROM aws.kafkaconnect.custom_plugins
WHERE region = 'us-east-1' AND data__Identifier = '<CustomPluginArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>custom_plugin</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.kafkaconnect.custom_plugins (
 Name,
 ContentType,
 Location,
 region
)
SELECT 
'{{ Name }}',
 '{{ ContentType }}',
 '{{ Location }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.kafkaconnect.custom_plugins (
 Name,
 Description,
 ContentType,
 Location,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ Description }}',
 '{{ ContentType }}',
 '{{ Location }}',
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
  - name: custom_plugin
    props:
      - name: Name
        value: '{{ Name }}'
      - name: Description
        value: '{{ Description }}'
      - name: ContentType
        value: '{{ ContentType }}'
      - name: Location
        value:
          S3Location:
            BucketArn: '{{ BucketArn }}'
            FileKey: '{{ FileKey }}'
            ObjectVersion: '{{ ObjectVersion }}'
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
DELETE FROM aws.kafkaconnect.custom_plugins
WHERE data__Identifier = '<CustomPluginArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>custom_plugins</code> resource, the following permissions are required:

### Create
```json
kafkaconnect:DescribeCustomPlugin,
kafkaconnect:ListTagsForResource,
kafkaconnect:CreateCustomPlugin,
kafkaconnect:TagResource,
s3:GetObject,
s3:GetObjectVersion,
s3:GetObjectAttributes,
s3:GetObjectVersionAttributes
```

### Read
```json
kafkaconnect:DescribeCustomPlugin,
kafkaconnect:ListTagsForResource
```

### Update
```json
kafkaconnect:DescribeCustomPlugin,
kafkaconnect:ListTagsForResource,
kafkaconnect:TagResource,
kafkaconnect:UntagResource
```

### Delete
```json
kafkaconnect:DeleteCustomPlugin,
kafkaconnect:DescribeCustomPlugin
```

### List
```json
kafkaconnect:ListCustomPlugins
```

