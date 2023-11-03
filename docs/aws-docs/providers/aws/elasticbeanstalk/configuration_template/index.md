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
<tr><td><b>Id</b></td><td><code>aws.elasticbeanstalk.configuration_template</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>ApplicationName</code></td><td><code>string</code></td><td>The name of the Elastic Beanstalk application to associate with this configuration template. </td></tr><tr><td><code>Description</code></td><td><code>string</code></td><td>An optional description for this configuration.</td></tr><tr><td><code>EnvironmentId</code></td><td><code>string</code></td><td>The ID of an environment whose settings you want to use to create the configuration template. You must specify EnvironmentId if you don't specify PlatformArn, SolutionStackName, or SourceConfiguration. </td></tr><tr><td><code>OptionSettings</code></td><td><code>array</code></td><td>Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see [Option Values](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html) in the AWS Elastic Beanstalk Developer Guide. </td></tr><tr><td><code>PlatformArn</code></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the custom platform. For more information, see [Custom Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html) in the AWS Elastic Beanstalk Developer Guide. </td></tr><tr><td><code>SolutionStackName</code></td><td><code>string</code></td><td>The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, 64bit Amazon Linux 2013.09 running Tomcat 7 Java 7. A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see [Supported Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html) in the AWS Elastic Beanstalk Developer Guide.

 You must specify SolutionStackName if you don't specify PlatformArn, EnvironmentId, or SourceConfiguration.

 Use the ListAvailableSolutionStacks API to obtain a list of available solution stacks. </td></tr><tr><td><code>SourceConfiguration</code></td><td><code>undefined</code></td><td>An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.

Values specified in OptionSettings override any values obtained from the SourceConfiguration.

You must specify SourceConfiguration if you don't specify PlatformArn, EnvironmentId, or SolutionStackName.

Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name. </td></tr><tr><td><code>TemplateName</code></td><td><code>string</code></td><td>The name of the configuration template</td></tr>
</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
<pre>
SELECT * 
FROM aws.elasticbeanstalk.configuration_template
WHERE region = 'us-east-1' AND data__Identifier = '{ApplicationName}' AND data__Identifier = '{TemplateName}'
</pre>
