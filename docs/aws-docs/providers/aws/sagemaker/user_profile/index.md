---
title: user_profile
hide_title: false
hide_table_of_contents: false
keywords:
  - user_profile
  - sagemaker
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>user_profile</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_profile</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>user_profile</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.user_profile</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>UserProfileArn</code></td><td><code>string</code></td><td>The user profile Amazon Resource Name (ARN).</td></tr>
<tr><td><code>DomainId</code></td><td><code>string</code></td><td>The ID of the associated Domain.</td></tr>
<tr><td><code>SingleSignOnUserIdentifier</code></td><td><code>string</code></td><td>A specifier for the type of value specified in SingleSignOnUserValue. Currently, the only supported value is "UserName". If the Domain's AuthMode is SSO, this field is required. If the Domain's AuthMode is not SSO, this field cannot be specified.</td></tr>
<tr><td><code>SingleSignOnUserValue</code></td><td><code>string</code></td><td>The username of the associated AWS Single Sign-On User for this UserProfile. If the Domain's AuthMode is SSO, this field is required, and must match a valid username of a user in your directory. If the Domain's AuthMode is not SSO, this field cannot be specified.</td></tr>
<tr><td><code>UserProfileName</code></td><td><code>string</code></td><td>A name for the UserProfile.</td></tr>
<tr><td><code>UserSettings</code></td><td><code>undefined</code></td><td>A collection of settings.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of tags to apply to the user profile.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.sagemaker.user_profile
WHERE region = 'us-east-1' AND data__Identifier = '&lt;UserProfileName&gt;' AND data__Identifier = '&lt;DomainId&gt;'
</pre>
