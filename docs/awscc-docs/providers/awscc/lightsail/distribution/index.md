---
title: distribution
hide_title: false
hide_table_of_contents: false
keywords:
  - distribution
  - lightsail
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>distribution</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>distribution</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>distribution</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.lightsail.distribution</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>distribution_name</code></td><td><code>string</code></td><td>The name for the distribution.</td></tr>
<tr><td><code>distribution_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>bundle_id</code></td><td><code>string</code></td><td>The bundle ID to use for the distribution.</td></tr>
<tr><td><code>ip_address_type</code></td><td><code>string</code></td><td>The IP address type for the distribution.</td></tr>
<tr><td><code>cache_behaviors</code></td><td><code>array</code></td><td>An array of objects that describe the per-path cache behavior for the distribution.</td></tr>
<tr><td><code>cache_behavior_settings</code></td><td><code>object</code></td><td>An object that describes the cache behavior settings for the distribution.</td></tr>
<tr><td><code>default_cache_behavior</code></td><td><code>object</code></td><td>An object that describes the default cache behavior for the distribution.</td></tr>
<tr><td><code>origin</code></td><td><code>object</code></td><td>An object that describes the origin resource for the distribution, such as a Lightsail instance or load balancer.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of the distribution.</td></tr>
<tr><td><code>able_to_update_bundle</code></td><td><code>boolean</code></td><td>Indicates whether the bundle that is currently applied to your distribution, specified using the distributionName parameter, can be changed to another bundle.</td></tr>
<tr><td><code>is_enabled</code></td><td><code>boolean</code></td><td>Indicates whether the distribution is enabled.</td></tr>
<tr><td><code>certificate_name</code></td><td><code>string</code></td><td>The certificate attached to the Distribution.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>distribution</code> resource, the following permissions are required:

### Read
<pre>
lightsail:GetDistributions</pre>

### Update
<pre>
lightsail:AttachCertificateToDistribution,
lightsail:DetachCertificateFromDistribution,
lightsail:GetCertificates,
lightsail:GetCertificateDetails,
lightsail:GetDistributions,
lightsail:TagResource,
lightsail:UntagResource,
lightsail:UpdateDistribution,
lightsail:UpdateDistributionBundle</pre>

### Delete
<pre>
lightsail:DeleteDistribution,
lightsail:GetDistributions</pre>


## Example
```sql
SELECT
region,
distribution_name,
distribution_arn,
bundle_id,
ip_address_type,
cache_behaviors,
cache_behavior_settings,
default_cache_behavior,
origin,
status,
able_to_update_bundle,
is_enabled,
certificate_name,
tags
FROM awscc.lightsail.distribution
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;DistributionName&gt;'
```
