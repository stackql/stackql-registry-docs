---
title: mission_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - mission_profiles
  - groundstation
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

Creates, updates, deletes or gets a <code>mission_profile</code> resource or lists <code>mission_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mission_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Ground Station Mission Profile resource type for CloudFormation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.groundstation.mission_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name used to identify a mission profile.</td></tr>
<tr><td><CopyableCode code="contact_pre_pass_duration_seconds" /></td><td><code>integer</code></td><td>Pre-pass time needed before the contact.</td></tr>
<tr><td><CopyableCode code="contact_post_pass_duration_seconds" /></td><td><code>integer</code></td><td>Post-pass time needed after the contact.</td></tr>
<tr><td><CopyableCode code="minimum_viable_contact_duration_seconds" /></td><td><code>integer</code></td><td>Visibilities with shorter duration than the specified minimum viable contact duration will be ignored when searching for available contacts.</td></tr>
<tr><td><CopyableCode code="streams_kms_key" /></td><td><code>object</code></td><td>The ARN of a KMS Key used for encrypting data during transmission from the source to destination locations.</td></tr>
<tr><td><CopyableCode code="streams_kms_role" /></td><td><code>string</code></td><td>The ARN of the KMS Key or Alias Key role used to define permissions on KMS Key usage.</td></tr>
<tr><td><CopyableCode code="dataflow_edges" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tracking_config_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-missionprofile.html"><code>AWS::GroundStation::MissionProfile</code></a>.

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
    <td><CopyableCode code="Name, MinimumViableContactDurationSeconds, DataflowEdges, TrackingConfigArn, region" /></td>
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
Gets all <code>mission_profiles</code> in a region.
```sql
SELECT
region,
name,
contact_pre_pass_duration_seconds,
contact_post_pass_duration_seconds,
minimum_viable_contact_duration_seconds,
streams_kms_key,
streams_kms_role,
dataflow_edges,
tracking_config_arn,
tags,
id,
arn,
region
FROM aws.groundstation.mission_profiles
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>mission_profile</code>.
```sql
SELECT
region,
name,
contact_pre_pass_duration_seconds,
contact_post_pass_duration_seconds,
minimum_viable_contact_duration_seconds,
streams_kms_key,
streams_kms_role,
dataflow_edges,
tracking_config_arn,
tags,
id,
arn,
region
FROM aws.groundstation.mission_profiles
WHERE region = 'us-east-1' AND data__Identifier = '<Id>|<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>mission_profile</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.groundstation.mission_profiles (
 Name,
 MinimumViableContactDurationSeconds,
 DataflowEdges,
 TrackingConfigArn,
 region
)
SELECT 
'{{ Name }}',
 '{{ MinimumViableContactDurationSeconds }}',
 '{{ DataflowEdges }}',
 '{{ TrackingConfigArn }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.groundstation.mission_profiles (
 Name,
 ContactPrePassDurationSeconds,
 ContactPostPassDurationSeconds,
 MinimumViableContactDurationSeconds,
 StreamsKmsKey,
 StreamsKmsRole,
 DataflowEdges,
 TrackingConfigArn,
 Tags,
 region
)
SELECT 
 '{{ Name }}',
 '{{ ContactPrePassDurationSeconds }}',
 '{{ ContactPostPassDurationSeconds }}',
 '{{ MinimumViableContactDurationSeconds }}',
 '{{ StreamsKmsKey }}',
 '{{ StreamsKmsRole }}',
 '{{ DataflowEdges }}',
 '{{ TrackingConfigArn }}',
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
  - name: mission_profile
    props:
      - name: Name
        value: '{{ Name }}'
      - name: ContactPrePassDurationSeconds
        value: '{{ ContactPrePassDurationSeconds }}'
      - name: ContactPostPassDurationSeconds
        value: '{{ ContactPostPassDurationSeconds }}'
      - name: MinimumViableContactDurationSeconds
        value: '{{ MinimumViableContactDurationSeconds }}'
      - name: StreamsKmsKey
        value:
          KmsKeyArn: '{{ KmsKeyArn }}'
          KmsAliasArn: '{{ KmsAliasArn }}'
      - name: StreamsKmsRole
        value: '{{ StreamsKmsRole }}'
      - name: DataflowEdges
        value:
          - Source: '{{ Source }}'
            Destination: '{{ Destination }}'
      - name: TrackingConfigArn
        value: '{{ TrackingConfigArn }}'
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
DELETE FROM aws.groundstation.mission_profiles
WHERE data__Identifier = '<Id|Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>mission_profiles</code> resource, the following permissions are required:

### Create
```json
groundstation:CreateMissionProfile,
groundstation:GetMissionProfile,
groundstation:TagResource,
iam:PassRole,
kms:DescribeKey,
kms:CreateGrant
```

### Read
```json
groundstation:GetMissionProfile,
groundstation:ListTagsForResource,
kms:DescribeKey,
kms:CreateGrant
```

### Update
```json
groundstation:UpdateMissionProfile,
groundstation:GetMissionProfile,
groundstation:ListTagsForResource,
groundstation:TagResource,
groundstation:UntagResource,
iam:PassRole,
kms:DescribeKey,
kms:CreateGrant
```

### Delete
```json
groundstation:DeleteMissionProfile,
groundstation:GetMissionProfile
```

### List
```json
groundstation:ListMissionProfiles
```
