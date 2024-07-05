---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
  - mediapackage
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

Creates, updates, deletes or gets an <code>asset</code> resource or lists <code>assets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::MediaPackage::Asset</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.mediapackage.assets" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the Asset.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The time the Asset was initially submitted for Ingest.</td></tr>
<tr><td><CopyableCode code="egress_endpoints" /></td><td><code>array</code></td><td>The list of egress endpoints available for the Asset.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The unique identifier for the Asset.</td></tr>
<tr><td><CopyableCode code="packaging_group_id" /></td><td><code>string</code></td><td>The ID of the PackagingGroup for the Asset.</td></tr>
<tr><td><CopyableCode code="resource_id" /></td><td><code>string</code></td><td>The resource ID to include in SPEKE key requests.</td></tr>
<tr><td><CopyableCode code="source_arn" /></td><td><code>string</code></td><td>ARN of the source object in S3.</td></tr>
<tr><td><CopyableCode code="source_role_arn" /></td><td><code>string</code></td><td>The IAM role_arn used to access the source S3 bucket.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>A collection of tags associated with a resource</td></tr>
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
    <td><CopyableCode code="Id, PackagingGroupId, SourceArn, SourceRoleArn, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>assets</code> in a region.
```sql
SELECT
region,
arn,
created_at,
egress_endpoints,
id,
packaging_group_id,
resource_id,
source_arn,
source_role_arn,
tags
FROM aws.mediapackage.assets
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>asset</code>.
```sql
SELECT
region,
arn,
created_at,
egress_endpoints,
id,
packaging_group_id,
resource_id,
source_arn,
source_role_arn,
tags
FROM aws.mediapackage.assets
WHERE region = 'us-east-1' AND data__Identifier = '<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>asset</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.mediapackage.assets (
 Id,
 PackagingGroupId,
 SourceArn,
 SourceRoleArn,
 region
)
SELECT 
'{{ Id }}',
 '{{ PackagingGroupId }}',
 '{{ SourceArn }}',
 '{{ SourceRoleArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.mediapackage.assets (
 EgressEndpoints,
 Id,
 PackagingGroupId,
 ResourceId,
 SourceArn,
 SourceRoleArn,
 Tags,
 region
)
SELECT 
 '{{ EgressEndpoints }}',
 '{{ Id }}',
 '{{ PackagingGroupId }}',
 '{{ ResourceId }}',
 '{{ SourceArn }}',
 '{{ SourceRoleArn }}',
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
  - name: asset
    props:
      - name: EgressEndpoints
        value:
          - PackagingConfigurationId: '{{ PackagingConfigurationId }}'
            Url: '{{ Url }}'
      - name: Id
        value: '{{ Id }}'
      - name: PackagingGroupId
        value: '{{ PackagingGroupId }}'
      - name: ResourceId
        value: '{{ ResourceId }}'
      - name: SourceArn
        value: '{{ SourceArn }}'
      - name: SourceRoleArn
        value: '{{ SourceRoleArn }}'
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
DELETE FROM aws.mediapackage.assets
WHERE data__Identifier = '<Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>assets</code> resource, the following permissions are required:

### Create
```json
mediapackage-vod:CreateAsset,
mediapackage-vod:DescribeAsset,
mediapackage-vod:TagResource,
iam:PassRole
```

### Read
```json
mediapackage-vod:DescribeAsset
```

### Delete
```json
mediapackage-vod:DescribeAsset,
mediapackage-vod:DeleteAsset
```

### List
```json
mediapackage-vod:ListAssets,
mediapackage-vod:DescribePackagingGroup
```

