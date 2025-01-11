---
title: resolvers_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - resolvers_list_only
  - appsync
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

Lists <code>resolvers</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/resolvers/"><code>resolvers</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resolvers_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::AppSync::Resolver</code> resource defines the logical GraphQL resolver that you attach to fields in a schema. Request and response templates for resolvers are written in Apache Velocity Template Language (VTL) format. For more information about resolvers, see &#91;Resolver Mapping Template Reference&#93;(https://docs.aws.amazon.com/appsync/latest/devguide/resolver-mapping-template-reference.html).<br />When you submit an update, CFNLong updates resources based on differences between what you submit and the stack's current template. To cause this resource to be updated you must change a property value for this resource in the CFNshort template. Changing the S3 file content without changing a property value will not result in an update operation.<br />See &#91;Update Behaviors of Stack Resources&#93;(https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appsync.resolvers_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="resolver_arn" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>resolvers</code> in a region.
```sql
SELECT
region,
resolver_arn
FROM aws.appsync.resolvers_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>resolvers_list_only</code> resource, see <a href="/providers/aws/appsync/resolvers/#permissions"><code>resolvers</code></a>

