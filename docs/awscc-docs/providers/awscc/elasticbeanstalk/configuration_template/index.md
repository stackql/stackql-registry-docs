---
title: configuration_template
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_template
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
Gets an individual <code>configuration_template</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_template</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>configuration_template</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.elasticbeanstalk.configuration_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>application_name</code></td><td><code>string</code></td><td>The name of the Elastic Beanstalk application to associate with this configuration template. </td></tr>
<tr><td><code>description</code></td><td><code>string</code></td><td>An optional description for this configuration.</td></tr>
<tr><td><code>environment_id</code></td><td><code>string</code></td><td>The ID of an environment whose settings you want to use to create the configuration template. You must specify EnvironmentId if you don't specify PlatformArn, SolutionStackName, or SourceConfiguration. </td></tr>
<tr><td><code>option_settings</code></td><td><code>array</code></td><td>Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see &#91;Option Values&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;elasticbeanstalk&#x2F;latest&#x2F;dg&#x2F;command-options.html) in the AWS Elastic Beanstalk Developer Guide. </td></tr>
<tr><td><code>platform_arn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the custom platform. For more information, see &#91;Custom Platforms&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;elasticbeanstalk&#x2F;latest&#x2F;dg&#x2F;custom-platforms.html) in the AWS Elastic Beanstalk Developer Guide. </td></tr>
<tr><td><code>solution_stack_name</code></td><td><code>string</code></td><td>The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, 64bit Amazon Linux 2013.09 running Tomcat 7 Java 7. A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see &#91;Supported Platforms&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;elasticbeanstalk&#x2F;latest&#x2F;dg&#x2F;concepts.platforms.html) in the AWS Elastic Beanstalk Developer Guide.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt; You must specify SolutionStackName if you don't specify PlatformArn, EnvironmentId, or SourceConfiguration.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt; Use the ListAvailableSolutionStacks API to obtain a list of available solution stacks. </td></tr>
<tr><td><code>source_configuration</code></td><td><code>object</code></td><td>An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Values specified in OptionSettings override any values obtained from the SourceConfiguration.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;You must specify SourceConfiguration if you don't specify PlatformArn, EnvironmentId, or SolutionStackName.&lt;br&#x2F;&gt;&lt;br&#x2F;&gt;Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name. </td></tr>
<tr><td><code>template_name</code></td><td><code>string</code></td><td>The name of the configuration template</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>configuration_template</code> resource, the following permissions are required:

### Read
<pre>
elasticbeanstalk:DescribeConfigurationSettings</pre>

### Update
<pre>
elasticbeanstalk:UpdateConfigurationTemplate</pre>

### Delete
<pre>
elasticbeanstalk:DeleteConfigurationTemplate,
elasticbeanstalk:DescribeConfigurationSettings</pre>


## Example
```sql
SELECT
region,
application_name,
description,
environment_id,
option_settings,
platform_arn,
solution_stack_name,
source_configuration,
template_name
FROM awscc.elasticbeanstalk.configuration_template
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ApplicationName&gt;'
AND data__Identifier = '&lt;TemplateName&gt;'
```
