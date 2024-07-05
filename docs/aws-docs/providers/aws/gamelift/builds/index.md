---
title: builds
hide_title: false
hide_table_of_contents: false
keywords:
  - builds
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

Creates, updates, deletes or gets a <code>build</code> resource or lists <code>builds</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>builds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::GameLift::Build</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.gamelift.builds" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="build_id" /></td><td><code>string</code></td><td>A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A descriptive label that is associated with a build. Build names do not need to be unique.</td></tr>
<tr><td><CopyableCode code="operating_system" /></td><td><code>string</code></td><td>The operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build. If your game build contains multiple executables, they all must run on the same operating system. If an operating system is not specified when creating a build, Amazon GameLift uses the default value (WINDOWS_2012). This value cannot be changed later.</td></tr>
<tr><td><CopyableCode code="storage_location" /></td><td><code>object</code></td><td>Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift to access your Amazon S3 bucket. The S3 bucket and your new build must be in the same Region.</td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td>Version information that is associated with this build. Version strings do not need to be unique.</td></tr>
<tr><td><CopyableCode code="server_sdk_version" /></td><td><code>string</code></td><td>A server SDK version you used when integrating your game server build with Amazon GameLift. By default Amazon GameLift sets this value to 4.0.2.</td></tr>
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
    <td><CopyableCode code=", region" /></td>
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
Gets all <code>builds</code> in a region.
```sql
SELECT
region,
build_id,
name,
operating_system,
storage_location,
version,
server_sdk_version
FROM aws.gamelift.builds
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>build</code>.
```sql
SELECT
region,
build_id,
name,
operating_system,
storage_location,
version,
server_sdk_version
FROM aws.gamelift.builds
WHERE region = 'us-east-1' AND data__Identifier = '<BuildId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>build</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.gamelift.builds (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.gamelift.builds (
 Name,
 OperatingSystem,
 StorageLocation,
 Version,
 ServerSdkVersion,
 region
)
SELECT 
 '{{ Name }}',
 '{{ OperatingSystem }}',
 '{{ StorageLocation }}',
 '{{ Version }}',
 '{{ ServerSdkVersion }}',
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
  - name: build
    props:
      - name: Name
        value: '{{ Name }}'
      - name: OperatingSystem
        value: '{{ OperatingSystem }}'
      - name: StorageLocation
        value:
          Bucket: '{{ Bucket }}'
          Key: '{{ Key }}'
          ObjectVersion: '{{ ObjectVersion }}'
          RoleArn: '{{ RoleArn }}'
      - name: Version
        value: '{{ Version }}'
      - name: ServerSdkVersion
        value: '{{ ServerSdkVersion }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.gamelift.builds
WHERE data__Identifier = '<BuildId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>builds</code> resource, the following permissions are required:

### Create
```json
gamelift:DescribeBuild,
gamelift:CreateBuild
```

### Read
```json
gamelift:DescribeBuild
```

### Update
```json
gamelift:UpdateBuild
```

### Delete
```json
gamelift:DescribeBuild,
gamelift:DeleteBuild
```

### List
```json
gamelift:ListBuilds
```

