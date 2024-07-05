---
title: configuration_templates_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_templates_list_only
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Lists <code>configuration_templates</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/configuration_templates/"><code>configuration_templates</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_templates_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElasticBeanstalk::ConfigurationTemplate</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticbeanstalk.configuration_templates_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>The name of the Elastic Beanstalk application to associate with this configuration template.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>An optional description for this configuration.</td></tr>
<tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The ID of an environment whose settings you want to use to create the configuration template. You must specify EnvironmentId if you don't specify PlatformArn, SolutionStackName, or SourceConfiguration.</td></tr>
<tr><td><CopyableCode code="option_settings" /></td><td><code>array</code></td><td>Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see &#91;Option Values&#93;(https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html) in the AWS Elastic Beanstalk Developer Guide.</td></tr>
<tr><td><CopyableCode code="platform_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the custom platform. For more information, see &#91;Custom Platforms&#93;(https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html) in the AWS Elastic Beanstalk Developer Guide.</td></tr>
<tr><td><CopyableCode code="solution_stack_name" /></td><td><code>string</code></td><td>The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, 64bit Amazon Linux 2013.09 running Tomcat 7 Java 7. A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see &#91;Supported Platforms&#93;(https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html) in the AWS Elastic Beanstalk Developer Guide.<br />You must specify SolutionStackName if you don't specify PlatformArn, EnvironmentId, or SourceConfiguration.<br />Use the ListAvailableSolutionStacks API to obtain a list of available solution stacks.</td></tr>
<tr><td><CopyableCode code="source_configuration" /></td><td><code>object</code></td><td>An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.<br />Values specified in OptionSettings override any values obtained from the SourceConfiguration.<br />You must specify SourceConfiguration if you don't specify PlatformArn, EnvironmentId, or SolutionStackName.<br />Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name.</td></tr>
<tr><td><CopyableCode code="template_name" /></td><td><code>string</code></td><td>The name of the configuration template</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>configuration_templates</code> in a region.
```sql
SELECT
region,
application_name,
template_name
FROM aws.elasticbeanstalk.configuration_templates_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>configuration_templates_list_only</code> resource, see <a href="/providers/aws/elasticbeanstalk/configuration_templates/#permissions"><code>configuration_templates</code></a>


