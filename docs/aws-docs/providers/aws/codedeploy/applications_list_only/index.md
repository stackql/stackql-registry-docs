---
title: applications_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - applications_list_only
  - codedeploy
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

Lists <code>applications</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/applications/"><code>applications</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>applications_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::CodeDeploy::Application resource creates an AWS CodeDeploy application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.codedeploy.applications_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_name" /></td><td><code>string</code></td><td>A name for the application. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the application name.</td></tr>
<tr><td><CopyableCode code="compute_platform" /></td><td><code>string</code></td><td>The compute platform that CodeDeploy deploys the application to.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The metadata that you apply to CodeDeploy applications to help you organize and categorize them. Each tag consists of a key and an optional value, both of which you define.</td></tr>
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
Lists all <code>applications</code> in a region.
```sql
SELECT
region,
application_name
FROM aws.codedeploy.applications_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>applications_list_only</code> resource, see <a href="/providers/aws/codedeploy/applications/#permissions"><code>applications</code></a>


