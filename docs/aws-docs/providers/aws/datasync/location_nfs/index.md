---
title: location_nfs
hide_title: false
hide_table_of_contents: false
keywords:
  - location_nfs
  - datasync
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

Creates, updates, deletes or gets a <code>location_nf</code> resource or lists <code>location_nfs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>location_nfs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DataSync::LocationNFS</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datasync.location_nfs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="mount_options" /></td><td><code>object</code></td><td>The mount options used by DataSync to access the SMB server.</td></tr>
<tr><td><CopyableCode code="on_prem_config" /></td><td><code>object</code></td><td>Contains a list of Amazon Resource Names (ARNs) of agents that are used to connect an NFS server.</td></tr>
<tr><td><CopyableCode code="server_hostname" /></td><td><code>string</code></td><td>The name of the NFS server. This value is the IP address or DNS name of the NFS server.</td></tr>
<tr><td><CopyableCode code="subdirectory" /></td><td><code>string</code></td><td>The subdirectory in the NFS file system that is used to read data from the NFS source location or write data to the NFS destination.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="location_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the NFS location.</td></tr>
<tr><td><CopyableCode code="location_uri" /></td><td><code>string</code></td><td>The URL of the NFS location that was described.</td></tr>
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
    <td><CopyableCode code="OnPremConfig, region" /></td>
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
Gets all <code>location_nfs</code> in a region.
```sql
SELECT
region,
mount_options,
on_prem_config,
server_hostname,
subdirectory,
tags,
location_arn,
location_uri
FROM aws.datasync.location_nfs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>location_nf</code>.
```sql
SELECT
region,
mount_options,
on_prem_config,
server_hostname,
subdirectory,
tags,
location_arn,
location_uri
FROM aws.datasync.location_nfs
WHERE region = 'us-east-1' AND data__Identifier = '<LocationArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>location_nf</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.datasync.location_nfs (
 OnPremConfig,
 region
)
SELECT 
'{{ OnPremConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datasync.location_nfs (
 MountOptions,
 OnPremConfig,
 ServerHostname,
 Subdirectory,
 Tags,
 region
)
SELECT 
 '{{ MountOptions }}',
 '{{ OnPremConfig }}',
 '{{ ServerHostname }}',
 '{{ Subdirectory }}',
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
  - name: location_nf
    props:
      - name: MountOptions
        value:
          Version: '{{ Version }}'
      - name: OnPremConfig
        value:
          AgentArns:
            - '{{ AgentArns[0] }}'
      - name: ServerHostname
        value: '{{ ServerHostname }}'
      - name: Subdirectory
        value: '{{ Subdirectory }}'
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
DELETE FROM aws.datasync.location_nfs
WHERE data__Identifier = '<LocationArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>location_nfs</code> resource, the following permissions are required:

### Create
```json
datasync:CreateLocationNfs,
datasync:DescribeLocationNfs,
datasync:ListTagsForResource,
datasync:TagResource
```

### Read
```json
datasync:DescribeLocationNfs,
datasync:ListTagsForResource
```

### Update
```json
datasync:DescribeLocationNfs,
datasync:ListTagsForResource,
datasync:TagResource,
datasync:UntagResource,
datasync:UpdateLocationNfs
```

### Delete
```json
datasync:DeleteLocation
```

### List
```json
datasync:ListLocations
```

