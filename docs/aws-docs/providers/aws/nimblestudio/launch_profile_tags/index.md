---
title: launch_profile_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - launch_profile_tags
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

Expands all tag keys and values for <code>launch_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_profile_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a launch profile which delegates access to a collection of studio components to studio users</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.nimblestudio.launch_profile_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td><p>The description.</p></td></tr>
<tr><td><CopyableCode code="ec2_subnet_ids" /></td><td><code>array</code></td><td><p>Specifies the IDs of the EC2 subnets where streaming sessions will be accessible from.<br />These subnets must support the specified instance types. </p></td></tr>
<tr><td><CopyableCode code="launch_profile_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="launch_profile_protocol_versions" /></td><td><code>array</code></td><td><p>The version number of the protocol that is used by the launch profile. The only valid<br />version is "2021-03-31".</p></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td><p>The name for the launch profile.</p></td></tr>
<tr><td><CopyableCode code="stream_configuration" /></td><td><code>object</code></td><td><p>A configuration for a streaming session.</p></td></tr>
<tr><td><CopyableCode code="studio_component_ids" /></td><td><code>array</code></td><td><p>Unique identifiers for a collection of studio components that can be used with this<br />launch profile.</p></td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td><p>The studio ID. </p></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Expands tags for all <code>launch_profiles</code> in a region.
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
tag_key,
tag_value
FROM aws.nimblestudio.launch_profile_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>launch_profile_tags</code> resource, see <a href="/providers/aws/nimblestudio/launch_profiles/#permissions"><code>launch_profiles</code></a>


