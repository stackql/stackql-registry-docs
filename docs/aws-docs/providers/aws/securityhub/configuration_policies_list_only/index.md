---
title: configuration_policies_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_policies_list_only
  - securityhub
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

Lists <code>configuration_policies</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/configuration_policies/"><code>configuration_policies</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_policies_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::ConfigurationPolicy resource represents the Central Configuration Policy in your account.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.configuration_policies_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the configuration policy.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the configuration policy.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the configuration policy.</td></tr>
<tr><td><CopyableCode code="configuration_policy" /></td><td><code>object</code></td><td>An object that defines how Security Hub is configured.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The universally unique identifier (UUID) of the configuration policy.</td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td>The date and time, in UTC and ISO 8601 format.</td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td>The date and time, in UTC and ISO 8601 format.</td></tr>
<tr><td><CopyableCode code="service_enabled" /></td><td><code>boolean</code></td><td>Indicates whether the service that the configuration policy applies to is enabled in the policy.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td>A key-value pair to associate with a resource.</td></tr>
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
Lists all <code>configuration_policies</code> in a region.
```sql
SELECT
region,
arn
FROM aws.securityhub.configuration_policies_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>configuration_policies_list_only</code> resource, see <a href="/providers/aws/securityhub/configuration_policies/#permissions"><code>configuration_policies</code></a>


