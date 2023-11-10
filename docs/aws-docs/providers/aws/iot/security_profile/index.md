---
title: security_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - security_profile
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
Gets an individual <code>security_profile</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>security_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>security_profile</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.security_profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>security_profile_name</code></td><td><code>string</code></td><td>A unique identifier for the security profile.</td></tr>
<tr><td><code>security_profile_description</code></td><td><code>string</code></td><td>A description of the security profile.</td></tr>
<tr><td><code>behaviors</code></td><td><code>array</code></td><td>Specifies the behaviors that, when violated by a device (thing), cause an alert.</td></tr>
<tr><td><code>alert_targets</code></td><td><code>object</code></td><td>Specifies the destinations to which alerts are sent.</td></tr>
<tr><td><code>additional_metrics_to_retain_v2</code></td><td><code>array</code></td><td>A list of metrics whose data is retained (stored). By default, data is retained for any metric used in the profile's behaviors, but it is also retained for any metric specified here.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>Metadata that can be used to manage the security profile.</td></tr>
<tr><td><code>target_arns</code></td><td><code>array</code></td><td>A set of target ARNs that the security profile is attached to.</td></tr>
<tr><td><code>security_profile_arn</code></td><td><code>string</code></td><td>The ARN (Amazon resource name) of the created security profile.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
security_profile_name,
security_profile_description,
behaviors,
alert_targets,
additional_metrics_to_retain_v2,
tags,
target_arns,
security_profile_arn
FROM aws.iot.security_profile
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;SecurityProfileName&gt;'
```
