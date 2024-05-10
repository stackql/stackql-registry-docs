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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>mission_profile</code> resource, use <code>mission_profiles</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mission_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Ground Station Mission Profile resource type for CloudFormation.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.groundstation.mission_profile" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>A name used to identify a mission profile.</td></tr>
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

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
WHERE region = 'us-east-1' AND data__Identifier = '<Id>|<Arn>';
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

