---
title: scripts
hide_title: false
hide_table_of_contents: false
keywords:
  - scripts
  - gamelift
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

Creates, updates, deletes or gets a <code>script</code> resource or lists <code>scripts</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scripts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::GameLift::Script resource creates a new script record for your Realtime Servers script. Realtime scripts are JavaScript that provide configuration settings and optional custom game logic for your game. The script is deployed when you create a Realtime Servers fleet to host your game sessions. Script logic is executed during an active game session.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.scripts" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A descriptive label that is associated with a script. Script names do not need to be unique.</td></tr>
<tr><td><CopyableCode code="storage_location" /></td><td><code>object</code></td><td>The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the ObjectVersion parameter to specify an earlier version.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>The version that is associated with a script. Version strings do not need to be unique.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td>A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example "1469498468.057").</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift script resource and uniquely identifies it. ARNs are unique across all Regions. In a GameLift script ARN, the resource ID matches the Id value.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>A unique identifier for the Realtime script</td></tr>
<tr><td><CopyableCode code="size_on_disk" /></td><td><code>integer</code></td><td>The file size of the uploaded Realtime script, expressed in bytes. When files are uploaded from an S3 location, this value remains at "0".</td></tr>
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
    <td><CopyableCode code="StorageLocation, region" /></td>
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
Gets all <code>scripts</code> in a region.
```sql
SELECT
region,
name,
storage_location,
version,
tags,
creation_time,
arn,
id,
size_on_disk
FROM aws.gamelift.scripts
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>script</code>.
```sql
SELECT
region,
name,
storage_location,
version,
tags,
creation_time,
arn,
id,
size_on_disk
FROM aws.gamelift.scripts
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>script</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.gamelift.scripts (
 StorageLocation,
 region
)
SELECT 
'{{ StorageLocation }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.gamelift.scripts (
 Name,
 StorageLocation,
 Version,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ StorageLocation }}',
 '{{ Version }}',
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
  - name: script
    props:
      - name: Name
        value: '{{ Name }}'
      - name: StorageLocation
        value:
          Bucket: '{{ Bucket }}'
          Key: '{{ Key }}'
          ObjectVersion: '{{ ObjectVersion }}'
          RoleArn: '{{ RoleArn }}'
      - name: Version
        value: '{{ Version }}'
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
DELETE FROM aws.gamelift.scripts
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>scripts</code> resource, the following permissions are required:

### Create
```json
gamelift:CreateScript,
gamelift:ListTagsForResource,
gamelift:TagResource,
gamelift:DescribeScript,
iam:PassRole
```

### Read
```json
gamelift:DescribeScript,
gamelift:ListScripts,
gamelift:ListTagsForResource
```

### Delete
```json
gamelift:DeleteScript
```

### List
```json
gamelift:ListScripts,
gamelift:DescribeScript
```

### Update
```json
gamelift:DescribeScript,
gamelift:UpdateScript,
gamelift:ListTagsForResource,
gamelift:TagResource,
gamelift:UntagResource,
iam:PassRole
```

