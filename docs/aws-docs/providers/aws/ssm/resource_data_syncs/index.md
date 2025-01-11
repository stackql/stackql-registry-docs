---
title: resource_data_syncs
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_data_syncs
  - ssm
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

Creates, updates, deletes or gets a <code>resource_data_sync</code> resource or lists <code>resource_data_syncs</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_data_syncs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SSM::ResourceDataSync</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssm.resource_data_syncs" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="s3_destination" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sync_source" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="bucket_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="bucket_region" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sync_format" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sync_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sync_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="bucket_prefix" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ssm-resourcedatasync.html"><code>AWS::SSM::ResourceDataSync</code></a>.

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
    <td><CopyableCode code="SyncName, region" /></td>
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
Gets all <code>resource_data_syncs</code> in a region.
```sql
SELECT
region,
s3_destination,
kms_key_arn,
sync_source,
bucket_name,
bucket_region,
sync_format,
sync_name,
sync_type,
bucket_prefix
FROM aws.ssm.resource_data_syncs
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>resource_data_sync</code>.
```sql
SELECT
region,
s3_destination,
kms_key_arn,
sync_source,
bucket_name,
bucket_region,
sync_format,
sync_name,
sync_type,
bucket_prefix
FROM aws.ssm.resource_data_syncs
WHERE region = 'us-east-1' AND data__Identifier = '<SyncName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_data_sync</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ssm.resource_data_syncs (
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
INSERT INTO aws.ssm.resource_data_syncs (
 S3Destination,
 KMSKeyArn,
 SyncSource,
 BucketName,
 BucketRegion,
 SyncFormat,
 SyncType,
 BucketPrefix,
 region
)
SELECT 
 '{{ S3Destination }}',
 '{{ KMSKeyArn }}',
 '{{ SyncSource }}',
 '{{ BucketName }}',
 '{{ BucketRegion }}',
 '{{ SyncFormat }}',
 '{{ SyncType }}',
 '{{ BucketPrefix }}',
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
  - name: resource_data_sync
    props:
      - name: S3Destination
        value:
          KMSKeyArn: '{{ KMSKeyArn }}'
          BucketPrefix: '{{ BucketPrefix }}'
          BucketName: '{{ BucketName }}'
          BucketRegion: '{{ BucketRegion }}'
          SyncFormat: '{{ SyncFormat }}'
      - name: KMSKeyArn
        value: '{{ KMSKeyArn }}'
      - name: SyncSource
        value:
          IncludeFutureRegions: '{{ IncludeFutureRegions }}'
          SourceRegions:
            - '{{ SourceRegions[0] }}'
          SourceType: '{{ SourceType }}'
          AwsOrganizationsSource:
            OrganizationalUnits:
              - '{{ OrganizationalUnits[0] }}'
            OrganizationSourceType: '{{ OrganizationSourceType }}'
      - name: BucketName
        value: '{{ BucketName }}'
      - name: BucketRegion
        value: '{{ BucketRegion }}'
      - name: SyncFormat
        value: '{{ SyncFormat }}'
      - name: SyncType
        value: '{{ SyncType }}'
      - name: BucketPrefix
        value: '{{ BucketPrefix }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.ssm.resource_data_syncs
WHERE data__Identifier = '<SyncName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resource_data_syncs</code> resource, the following permissions are required:

### Create
```json
ssm:CreateResourceDataSync,
ssm:ListResourceDataSync
```

### Delete
```json
ssm:ListResourceDataSync,
ssm:DeleteResourceDataSync
```

### Update
```json
ssm:ListResourceDataSync,
ssm:UpdateResourceDataSync
```

### List
```json
ssm:ListResourceDataSync
```

### Read
```json
ssm:ListResourceDataSync
```
