---
title: image_builders
hide_title: false
hide_table_of_contents: false
keywords:
  - image_builders
  - appstream
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>image_builders</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>image_builders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.appstream.image_builders</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>VpcConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>EnableDefaultInternetAccess</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>DomainJoinInfo</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>AppstreamAgentVersion</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ImageName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DisplayName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>IamRoleArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>InstanceType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>StreamingUrl</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ImageArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>AccessEndpoints</code></td><td><code>array</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.appstream.image_builders
WHERE region = 'us-east-1'
</pre>
