---
title: security_profiles
hide_title: false
hide_table_of_contents: false
keywords:
  - security_profiles
  - iot
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

Used to retrieve a list of <code>security_profiles</code> in a region or create a <code>security_profiles</code> resource, use <code>security_profile</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A security profile defines a set of expected behaviors for devices in your account.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iot.security_profiles" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="security_profile_name" /></td><td><code>string</code></td><td>A unique identifier for the security profile.</td></tr>
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
security_profile_name
FROM aws.iot.security_profiles
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>security_profiles</code> resource, the following permissions are required:

### Create
```json
iot:CreateSecurityProfile,
iot:AttachSecurityProfile,
iot:DescribeSecurityProfile,
iot:TagResource,
iam:PassRole
```

### List
```json
iot:ListSecurityProfiles
```

