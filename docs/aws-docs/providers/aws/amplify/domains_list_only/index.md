---
title: domains_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - domains_list_only
  - amplify
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

Lists <code>domains</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/domains/"><code>domains</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>domains_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Amplify::Domain resource allows you to connect a custom domain to your app.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplify.domains_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_sub_domain_creation_patterns" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_sub_domain_iam_role" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_record" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="certificate_settings" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="update_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_auto_sub_domain" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="status_reason" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sub_domain_settings" /></td><td><code>array</code></td><td></td></tr>
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
Lists all <code>domains</code> in a region.
```sql
SELECT
region,
arn
FROM aws.amplify.domains_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>domains_list_only</code> resource, see <a href="/providers/aws/amplify/domains/#permissions"><code>domains</code></a>


