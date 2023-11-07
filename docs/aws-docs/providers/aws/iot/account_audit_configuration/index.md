---
title: account_audit_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - account_audit_configuration
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
Gets an individual <code>account_audit_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_audit_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>account_audit_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iot.account_audit_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AccountId</code></td><td><code>string</code></td><td>Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).</td></tr>
<tr><td><code>AuditCheckConfigurations</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>AuditNotificationTargetConfigurations</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>RoleArn</code></td><td><code>string</code></td><td>The ARN of the role that grants permission to AWS IoT to access information about your devices, policies, certificates and other items as required when performing an audit.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.iot.account_audit_configuration<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;AccountId&gt;'
</pre>
