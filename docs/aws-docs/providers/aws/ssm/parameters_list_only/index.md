---
title: parameters_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - parameters_list_only
  - ssm
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

Lists <code>parameters</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/parameters/"><code>parameters</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>parameters_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::SSM::Parameter</code> resource creates an SSM parameter in SYSlong Parameter Store.<br />To create an SSM parameter, you must have the IAMlong (IAM) permissions <code>ssm:PutParameter</code> and <code>ssm:AddTagsToResource</code>. On stack creation, CFNlong adds the following three tags to the parameter: <code>aws:cloudformation:stack-name</code>, <code>aws:cloudformation:logical-id</code>, and <code>aws:cloudformation:stack-id</code>, in addition to any custom tags you specify.<br />To add, update, or remove tags during stack update, you must have IAM permissions for both <code>ssm:AddTagsToResource</code> and <code>ssm:RemoveTagsFromResource</code>. For more information, see &#91;Managing Access Using Policies&#93;(https://docs.aws.amazon.com/systems-manager/latest/userguide/security-iam.html#security_iam_access-manage) in the *User Guide*.<br />For information about valid values for parameters, see &#91;About requirements and constraints for parameter names&#93;(https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html#sysman-parameter-name-constraints) in the *User Guide* and &#91;PutParameter&#93;(https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutParameter.html) in the *API Reference*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssm.parameters_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the parameter.<br />The maximum length constraint listed below includes capacity for additional system attributes that aren't part of the name. The maximum length for a parameter name, including the full length of the parameter Amazon Resource Name (ARN), is 1011 characters. For example, the length of the following parameter name is 65 characters, not 20 characters: <code>arn:aws:ssm:us-east-2:111222333444:parameter/ExampleParameterName</code></td></tr>
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
Lists all <code>parameters</code> in a region.
```sql
SELECT
region,
name
FROM aws.ssm.parameters_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>parameters_list_only</code> resource, see <a href="/providers/aws/ssm/parameters/#permissions"><code>parameters</code></a>

