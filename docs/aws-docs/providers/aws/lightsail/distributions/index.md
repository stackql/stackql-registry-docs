---
title: distributions
hide_title: false
hide_table_of_contents: false
keywords:
  - distributions
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
Retrieves a list of <code>distributions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>distributions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.lightsail.distributions</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>DistributionName</code></td><td><code>string</code></td><td>The name for the distribution.</td></tr><tr><td><code>DistributionArn</code></td><td><code>string</code></td><td></td></tr><tr><td><code>BundleId</code></td><td><code>string</code></td><td>The bundle ID to use for the distribution.</td></tr><tr><td><code>IpAddressType</code></td><td><code>string</code></td><td>The IP address type for the distribution.</td></tr><tr><td><code>CacheBehaviors</code></td><td><code>array</code></td><td>An array of objects that describe the per-path cache behavior for the distribution.</td></tr><tr><td><code>CacheBehaviorSettings</code></td><td><code>undefined</code></td><td>An object that describes the cache behavior settings for the distribution.</td></tr><tr><td><code>DefaultCacheBehavior</code></td><td><code>undefined</code></td><td>An object that describes the default cache behavior for the distribution.</td></tr><tr><td><code>Origin</code></td><td><code>undefined</code></td><td>An object that describes the origin resource for the distribution, such as a Lightsail instance or load balancer.</td></tr><tr><td><code>Status</code></td><td><code>string</code></td><td>The status of the distribution.</td></tr><tr><td><code>AbleToUpdateBundle</code></td><td><code>boolean</code></td><td>Indicates whether the bundle that is currently applied to your distribution, specified using the distributionName parameter, can be changed to another bundle.</td></tr><tr><td><code>IsEnabled</code></td><td><code>boolean</code></td><td>Indicates whether the distribution is enabled.</td></tr><tr><td><code>CertificateName</code></td><td><code>string</code></td><td>The certificate attached to the Distribution.</td></tr><tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.lightsail.distributions
WHERE region = 'us-east-1'
</pre>
