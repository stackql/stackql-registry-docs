---
title: user_pool_risk_configuration_attachments
hide_title: false
hide_table_of_contents: false
keywords:
  - user_pool_risk_configuration_attachments
  - cognito
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>user_pool_risk_configuration_attachments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_pool_risk_configuration_attachments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cognito.user_pool_risk_configuration_attachments</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>Id</code></td><td><code>string</code></td><td></td></tr><tr><td><code>CompromisedCredentialsRiskConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>UserPoolId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>ClientId</code></td><td><code>string</code></td><td></td></tr><tr><td><code>AccountTakeoverRiskConfiguration</code></td><td><code>undefined</code></td><td></td></tr><tr><td><code>RiskExceptionConfiguration</code></td><td><code>undefined</code></td><td></td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.cognito.user_pool_risk_configuration_attachments
WHERE region = 'us-east-1'
</pre>
