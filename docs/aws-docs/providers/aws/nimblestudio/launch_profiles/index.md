---
title: launch_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - launch_profiles
  - nimblestudio
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

Used to retrieve a list of <code>launch_profiles</code> in a region or create a <code>launch_profiles</code> resource, use <code>launch_profile</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a launch profile which delegates access to a collection of studio components to studio users</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.launch_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="launch_profile_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td>&lt;p&gt;The studio ID. &lt;&#x2F;p&gt;</td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
launch_profile_id,
studio_id
FROM aws.nimblestudio.launch_profiles
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>launch_profiles</code> resource, the following permissions are required:

### Create
```json
nimble:CreateLaunchProfile,
nimble:GetLaunchProfile,
nimble:TagResource,
ec2:CreateNetworkInterface,
ec2:CreateNetworkInterfacePermission,
ec2:RunInstances,
ec2:DescribeSubnets
```

### List
```json
nimble:ListLaunchProfiles
```

