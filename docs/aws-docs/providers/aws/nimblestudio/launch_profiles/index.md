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
Retrieves a list of <code>launch_profiles</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_profiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.nimblestudio.launch_profiles</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>&lt;p&gt;The description.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>Ec2SubnetIds</code></td><td><code>array</code></td><td>&lt;p&gt;Specifies the IDs of the EC2 subnets where streaming sessions will be accessible from.&lt;br&#x2F;&gt;            These subnets must support the specified instance types. &lt;&#x2F;p&gt;</td></tr>
<tr><td><code>LaunchProfileId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>LaunchProfileProtocolVersions</code></td><td><code>array</code></td><td>&lt;p&gt;The version number of the protocol that is used by the launch profile. The only valid&lt;br&#x2F;&gt;            version is "2021-03-31".&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td>&lt;p&gt;The name for the launch profile.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>StreamConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>StudioComponentIds</code></td><td><code>array</code></td><td>&lt;p&gt;Unique identifiers for a collection of studio components that can be used with this&lt;br&#x2F;&gt;            launch profile.&lt;&#x2F;p&gt;</td></tr>
<tr><td><code>StudioId</code></td><td><code>string</code></td><td>&lt;p&gt;The studio ID. &lt;&#x2F;p&gt;</td></tr>
<tr><td><code>Tags</code></td><td><code>undefined</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.nimblestudio.launch_profiles
WHERE region = 'us-east-1'
</pre>
