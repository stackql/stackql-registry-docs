---
title: connect_peer
hide_title: false
hide_table_of_contents: false
keywords:
  - connect_peer
  - networkmanager
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>connect_peer</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connect_peer</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>connect_peer</td></tr>
<tr><td><b>Id</b></td><td><code>aws.networkmanager.connect_peer</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>PeerAddress</code></td><td><code>string</code></td><td>The IP address of the Connect peer.</td></tr>
<tr><td><code>CoreNetworkAddress</code></td><td><code>string</code></td><td>The IP address of a core network.</td></tr>
<tr><td><code>BgpOptions</code></td><td><code>undefined</code></td><td>Bgp options for connect peer.</td></tr>
<tr><td><code>InsideCidrBlocks</code></td><td><code>array</code></td><td>The inside IP addresses used for a Connect peer configuration.</td></tr>
<tr><td><code>CoreNetworkId</code></td><td><code>string</code></td><td>The ID of the core network.</td></tr>
<tr><td><code>ConnectAttachmentId</code></td><td><code>string</code></td><td>The ID of the attachment to connect.</td></tr>
<tr><td><code>ConnectPeerId</code></td><td><code>string</code></td><td>The ID of the Connect peer.</td></tr>
<tr><td><code>EdgeLocation</code></td><td><code>string</code></td><td>The Connect peer Regions where edges are located.</td></tr>
<tr><td><code>State</code></td><td><code>string</code></td><td>State of the connect peer.</td></tr>
<tr><td><code>CreatedAt</code></td><td><code>string</code></td><td>Connect peer creation time.</td></tr>
<tr><td><code>Configuration</code></td><td><code>undefined</code></td><td>Configuration of the connect peer.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.networkmanager.connect_peer
WHERE region = 'us-east-1' AND data__Identifier = '&lt;ConnectPeerId&gt;'
</pre>
