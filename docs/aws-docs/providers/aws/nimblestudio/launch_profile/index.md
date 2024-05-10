---
title: launch_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - launch_profile
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>launch_profile</code> resource, use <code>launch_profiles</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a launch profile which delegates access to a collection of studio components to studio users</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.launch_profile" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>&lt;p&gt;The description.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="ec2_subnet_ids" /></td><td><code>array</code></td><td>&lt;p&gt;Specifies the IDs of the EC2 subnets where streaming sessions will be accessible from.&lt;br&#x2F;&gt;            These subnets must support the specified instance types. &lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="launch_profile_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="launch_profile_protocol_versions" /></td><td><code>array</code></td><td>&lt;p&gt;The version number of the protocol that is used by the launch profile. The only valid&lt;br&#x2F;&gt;            version is "2021-03-31".&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>&lt;p&gt;The name for the launch profile.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="stream_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="studio_component_ids" /></td><td><code>array</code></td><td>&lt;p&gt;Unique identifiers for a collection of studio components that can be used with this&lt;br&#x2F;&gt;            launch profile.&lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td>&lt;p&gt;The studio ID. &lt;&#x2F;p&gt;</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
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
description,
ec2_subnet_ids,
launch_profile_id,
launch_profile_protocol_versions,
name,
stream_configuration,
studio_component_ids,
studio_id,
tags
FROM aws.nimblestudio.launch_profile
WHERE region = 'us-east-1' AND data__Identifier = '<LaunchProfileId>|<StudioId>';
```


## Permissions

To operate on the <code>launch_profile</code> resource, the following permissions are required:

### Read
```json
nimble:GetLaunchProfile
```

### Update
```json
nimble:UpdateLaunchProfile,
nimble:GetLaunchProfile,
ec2:CreateNetworkInterface,
ec2:CreateNetworkInterfacePermission,
ec2:DescribeSubnets,
ec2:RunInstances
```

