---
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
  - guardduty
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>members</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>members</td></tr>
<tr><td><b>Id</b></td><td><code>aws.guardduty.members</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>MemberId</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Email</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>Message</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>DisableEmailNotification</code></td><td><code>boolean</code></td><td></td></tr>
<tr><td><code>DetectorId</code></td><td><code>string</code></td><td></td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.guardduty.members<br/>WHERE region = 'us-east-1'
</pre>
