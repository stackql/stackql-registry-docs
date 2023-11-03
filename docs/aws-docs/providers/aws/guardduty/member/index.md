---
title: member
hide_title: false
hide_table_of_contents: false
keywords:
  - member
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
Gets an individual <code>member</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>member</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.guardduty.member</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Status</code></td><td><code>string</code></td><td></td></tr><tr><td><code>MemberId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Email</code></td><td><code>string</code></td><td></td></tr><tr><td><code>Message</code></td><td><code>string</code></td><td></td></tr><tr><td><code>DisableEmailNotification</code></td><td><code>boolean</code></td><td></td></tr><tr><td><code>DetectorId</code></td><td><code>string</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.guardduty.member
WHERE region = 'us-east-1' AND data__Identifier = '{MemberId}'
</pre>
