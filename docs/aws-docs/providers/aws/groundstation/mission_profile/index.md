---
title: mission_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - mission_profile
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
Gets an individual <code>mission_profile</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mission_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Ground Station Mission Profile resource type for CloudFormation.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.groundstation.mission_profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>A name used to identify a mission profile.</td></tr>
<tr><td><code>contact_pre_pass_duration_seconds</code></td><td><code>integer</code></td><td>Pre-pass time needed before the contact.</td></tr>
<tr><td><code>contact_post_pass_duration_seconds</code></td><td><code>integer</code></td><td>Post-pass time needed after the contact.</td></tr>
<tr><td><code>minimum_viable_contact_duration_seconds</code></td><td><code>integer</code></td><td>Visibilities with shorter duration than the specified minimum viable contact duration will be ignored when searching for available contacts.</td></tr>
<tr><td><code>streams_kms_key</code></td><td><code>object</code></td><td>The ARN of a KMS Key used for encrypting data during transmission from the source to destination locations.</td></tr>
<tr><td><code>streams_kms_role</code></td><td><code>string</code></td><td>The ARN of the KMS Key or Alias Key role used to define permissions on KMS Key usage.</td></tr>
<tr><td><code>dataflow_edges</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>tracking_config_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.groundstation.mission_profile
WHERE data__Identifier = '<Id>|<Arn>';
```

## Permissions

To operate on the <code>mission_profile</code> resource, the following permissions are required:

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

