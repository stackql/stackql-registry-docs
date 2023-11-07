---
title: fleets
hide_title: false
hide_table_of_contents: false
keywords:
  - fleets
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
Retrieves a list of <code>fleets</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>fleets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>fleets</td></tr>
<tr><td><b>Id</b></td><td><code>aws.appstream.fleets</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ComputeCapacity</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Platform</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>VpcConfig</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>FleetType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>EnableDefaultInternetAccess</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>DomainJoinInfo</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>SessionScriptS3Location</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>Name</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>ImageName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MaxUserDurationInSeconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>IdleDisconnectTimeoutInSeconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>UsbDeviceFilterStrings</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>DisconnectTimeoutInSeconds</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>DisplayName</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>StreamView</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>IamRoleArn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>InstanceType</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MaxConcurrentSessions</code></td><td><code>integer</code></td><td></td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>ImageArn</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.appstream.fleets<br/>WHERE region = 'us-east-1'
</pre>
