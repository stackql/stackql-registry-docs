---
title: studio_session_mapping
hide_title: false
hide_table_of_contents: false
keywords:
  - studio_session_mapping
  - emr
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>studio_session_mapping</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio_session_mapping</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
null
<tr><td><b>Id</b></td><td><code>aws.emr.studio_session_mapping</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>IdentityName</code></td><td><code>string</code></td><td>The name of the user or group. For more information, see UserName and DisplayName in the AWS SSO Identity Store API Reference. Either IdentityName or IdentityId must be specified.</td></tr>
<tr><td><code>IdentityType</code></td><td><code>string</code></td><td>Specifies whether the identity to map to the Studio is a user or a group.</td></tr>
<tr><td><code>SessionPolicyArn</code></td><td><code>undefined</code></td><td>The Amazon Resource Name (ARN) for the session policy that will be applied to the user or group. Session policies refine Studio user permissions without the need to use multiple IAM user roles.</td></tr>
<tr><td><code>StudioId</code></td><td><code>string</code></td><td>The ID of the Amazon EMR Studio to which the user or group will be mapped.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.emr.studio_session_mapping
WHERE region = 'us-east-1' AND data__Identifier = '&lt;StudioId&gt;' AND data__Identifier = '&lt;IdentityType&gt;' AND data__Identifier = '&lt;IdentityName&gt;'
</pre>
