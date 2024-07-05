---
title: launch_templates_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - launch_templates_list_only
  - ec2
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

Lists <code>launch_templates</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/launch_templates/"><code>launch_templates</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>launch_templates_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies the properties for creating a launch template.<br />The minimum required properties for specifying a launch template are as follows:<br />+ You must specify at least one property for the launch template data.<br />+ You can optionally specify a name for the launch template. If you do not specify a name, CFN creates a name for you.<br /><br />A launch template can contain some or all of the configuration information to launch an instance. When you launch an instance using a launch template, instance properties that are not specified in the launch template use default values, except the <code>ImageId</code> property, which has no default value. If you do not specify an AMI ID for the launch template <code>ImageId</code> property, you must specify an AMI ID for the instance <code>ImageId</code> property.<br />For more information, see &#91;Launch an instance from a launch template&#93;(https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon EC2 User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.launch_templates_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="launch_template_name" /></td><td><code>string</code></td><td>A name for the launch template.</td></tr>
<tr><td><CopyableCode code="launch_template_data" /></td><td><code>object</code></td><td>The information for the launch template.</td></tr>
<tr><td><CopyableCode code="version_description" /></td><td><code>string</code></td><td>A description for the first version of the launch template.</td></tr>
<tr><td><CopyableCode code="tag_specifications" /></td><td><code>array</code></td><td>The tags to apply to the launch template on creation. To tag the launch template, the resource type must be <code>launch-template</code>.<br />To specify the tags for the resources that are created when an instance is launched, you must use &#91;TagSpecifications&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-launchtemplate.html#cfn-ec2-launchtemplate-tagspecifications).</td></tr>
<tr><td><CopyableCode code="latest_version_number" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="launch_template_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_version_number" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>launch_templates</code> in a region.
```sql
SELECT
region,
launch_template_id
FROM aws.ec2.launch_templates_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>launch_templates_list_only</code> resource, see <a href="/providers/aws/ec2/launch_templates/#permissions"><code>launch_templates</code></a>


