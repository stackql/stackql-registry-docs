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


Used to retrieve a list of <code>resource_data_syncs</code> in a region or to create or delete a <code>resource_data_syncs</code> resource, use <code>resource_data_sync</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_data_syncs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::SSM::ResourceDataSync</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssm.resource_data_syncs" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="sync_name" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
sync_name
FROM aws.ssm.resource_data_syncs
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>resource_data_sync</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- resource_data_sync.iql (required properties only)
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
-- resource_data_sync.iql (all properties)
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

## `DELETE` Example

```sql
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

### List
```json
ssm:ListResourceDataSync
```

