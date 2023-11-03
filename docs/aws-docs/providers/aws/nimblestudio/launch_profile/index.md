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
Gets an individual <code>launch_profile</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.nimblestudio.launch_profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td><p>The description.</p></td></tr><tr><td><code>Ec2SubnetIds</code></td><td><code>array</code></td><td><p>Specifies the IDs of the EC2 subnets where streaming sessions will be accessible from.
            These subnets must support the specified instance types. </p></td></tr><tr><td><code>LaunchProfileId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>LaunchProfileProtocolVersions</code></td><td><code>array</code></td><td><p>The version number of the protocol that is used by the launch profile. The only valid
            version is "2021-03-31".</p></td></tr><tr><td><code>Name</code></td><td><code>string</code></td><td><p>The name for the launch profile.</p></td></tr><tr><td><code>StreamConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>StudioComponentIds</code></td><td><code>array</code></td><td><p>Unique identifiers for a collection of studio components that can be used with this
            launch profile.</p></td></tr><tr><td><code>StudioId</code></td><td><code>string</code></td><td><p>The studio ID. </p></td></tr><tr><td><code>Tags</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT * 
FROM aws.nimblestudio.launch_profile
WHERE region = 'us-east-1' AND data__Identifier = '{LaunchProfileId}' AND data__Identifier = '{StudioId}'
```
