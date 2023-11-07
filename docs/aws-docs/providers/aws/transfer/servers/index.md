---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - transfer
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>servers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>servers</td></tr>
<tr><td><b>Id</b></td><td><code>aws.transfer.servers</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>LoggingRole</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Protocols</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>IdentityProviderDetails</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>EndpointDetails</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>PreAuthenticationLoginBanner</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ServerId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>PostAuthenticationLoginBanner</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EndpointType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>SecurityPolicyName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ProtocolDetails</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>WorkflowDetails</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>Arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Domain</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>IdentityProviderType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>Certificate</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.transfer.servers<br/>WHERE region = 'us-east-1'
</pre>
