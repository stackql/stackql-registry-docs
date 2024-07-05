---
title: environments_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - environments_list_only
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

Lists <code>environments</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/environments/"><code>environments</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environments_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::ElasticBeanstalk::Environment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticbeanstalk.environments_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="platform_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the custom platform to use with the environment.</td></tr>
<tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>The name of the application that is associated with this environment.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Your description for this environment.</td></tr>
<tr><td><CopyableCode code="environment_name" /></td><td><code>string</code></td><td>A unique name for the environment.</td></tr>
<tr><td><CopyableCode code="operations_role" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of an existing IAM role to be used as the environment's operations role.</td></tr>
<tr><td><CopyableCode code="tier" /></td><td><code>object</code></td><td>Specifies the tier to use in creating this environment. The environment tier that you choose determines whether Elastic Beanstalk provisions resources to support a web application that handles HTTP(S) requests or a web application that handles background-processing tasks.</td></tr>
<tr><td><CopyableCode code="version_label" /></td><td><code>string</code></td><td>The name of the application version to deploy.</td></tr>
<tr><td><CopyableCode code="endpoint_url" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="option_settings" /></td><td><code>array</code></td><td>Key-value pairs defining configuration options for this environment, such as the instance type.</td></tr>
<tr><td><CopyableCode code="template_name" /></td><td><code>string</code></td><td>The name of the Elastic Beanstalk configuration template to use with the environment.</td></tr>
<tr><td><CopyableCode code="solution_stack_name" /></td><td><code>string</code></td><td>The name of an Elastic Beanstalk solution stack (platform version) to use with the environment.</td></tr>
<tr><td><CopyableCode code="cname_prefix" /></td><td><code>string</code></td><td>If specified, the environment attempts to use this value as the prefix for the CNAME in your Elastic Beanstalk environment URL. If not specified, the CNAME is generated automatically by appending a random alphanumeric string to the environment name.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Specifies the tags applied to resources in the environment.</td></tr>
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
Lists all <code>environments</code> in a region.
```sql
SELECT
region,
environment_name
FROM aws.elasticbeanstalk.environments_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>environments_list_only</code> resource, see <a href="/providers/aws/elasticbeanstalk/environments/#permissions"><code>environments</code></a>


