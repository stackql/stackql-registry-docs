---
title: loggings
hide_title: false
hide_table_of_contents: false
keywords:
  - loggings
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
Retrieves a list of <code>loggings</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>loggings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>loggings</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.loggings</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AccountId</code></td><td><code>string</code></td><td>Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).</td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td>The ARN of the role that allows IoT to write to Cloudwatch logs.</td></tr>
<tr><td><code>DefaultLogLevel</code></td><td><code>string</code></td><td>The log level to use. Valid values are: ERROR, WARN, INFO, DEBUG, or DISABLED.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.iot.loggings<br/>WHERE region = 'us-east-1'
</pre>
