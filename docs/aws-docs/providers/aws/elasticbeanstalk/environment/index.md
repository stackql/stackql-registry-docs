---
title: environment
hide_title: false
hide_table_of_contents: false
keywords:
  - environment
  - elasticbeanstalk
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>environment</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>environment</td></tr>
<tr><td><b>Id</b></td><td><code>aws.elasticbeanstalk.environment</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>PlatformArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the custom platform to use with the environment.</td></tr>
<tr><td><code>ApplicationName</code></td><td><code>string</code></td><td>The name of the application that is associated with this environment.</td></tr>
<tr><td><code>Description</code></td><td><code>string</code></td><td>Your description for this environment.</td></tr>
<tr><td><code>EnvironmentName</code></td><td><code>string</code></td><td>A unique name for the environment.</td></tr>
<tr><td><code>OperationsRole</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment's operations role.</td></tr>
<tr><td><code>Tier</code></td><td><code>object</code></td><td>Specifies the tier to use in creating this environment. The environment tier that you choose determines whether Elastic Beanstalk provisions resources to support a web application that handles HTTP(S) requests or a web application that handles background-processing tasks.</td></tr>
<tr><td><code>VersionLabel</code></td><td><code>string</code></td><td>The name of the application version to deploy.</td></tr>
<tr><td><code>EndpointURL</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>OptionSettings</code></td><td><code>array</code></td><td>Key-value pairs defining configuration options for this environment, such as the instance type.</td></tr>
<tr><td><code>TemplateName</code></td><td><code>string</code></td><td>The name of the Elastic Beanstalk configuration template to use with the environment.</td></tr>
<tr><td><code>SolutionStackName</code></td><td><code>string</code></td><td>The name of an Elastic Beanstalk solution stack (platform version) to use with the environment.</td></tr>
<tr><td><code>CNAMEPrefix</code></td><td><code>string</code></td><td>If specified, the environment attempts to use this value as the prefix for the CNAME in your Elastic Beanstalk environment URL. If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.</td></tr>
<tr><td><code>Tags</code></td><td><code>array</code></td><td>Specifies the tags applied to resources in the environment.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT *<br/>FROM aws.elasticbeanstalk.environment<br/>WHERE region = 'us-east-1'<br/>AND data__Identifier = '&lt;EnvironmentName&gt;'
</pre>
