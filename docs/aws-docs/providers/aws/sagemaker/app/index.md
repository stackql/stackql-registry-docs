---
title: app
hide_title: false
hide_table_of_contents: false
keywords:
  - app
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
Gets an individual <code>app</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>app</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>app</td></tr>
<tr><td><b>Id</b></td><td><code>aws.sagemaker.app</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>AppArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the app.</td></tr>
<tr><td><code>AppName</code></td><td><code>string</code></td><td>The name of the app.</td></tr>
<tr><td><code>AppType</code></td><td><code>string</code></td><td>The type of app.</td></tr>
<tr><td><code>DomainId</code></td><td><code>string</code></td><td>The domain ID.</td></tr>
<tr><td><code>ResourceSpec</code></td><td><code>undefined</code></td><td>The instance type and the Amazon Resource Name (ARN) of the SageMaker image created on the instance.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>A list of tags to apply to the app.</td></tr>
<tr><td><code>UserProfileName</code></td><td><code>string</code></td><td>The user profile name.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.sagemaker.app
WHERE region = 'us-east-1' AND data__Identifier = '&lt;AppName&gt;' AND data__Identifier = '&lt;AppType&gt;' AND data__Identifier = '&lt;DomainId&gt;' AND data__Identifier = '&lt;UserProfileName&gt;'
</pre>
