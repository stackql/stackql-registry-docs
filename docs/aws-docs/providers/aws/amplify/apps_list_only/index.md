---
title: apps_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - apps_list_only
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

Lists <code>apps</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/apps/"><code>apps</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apps_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::Amplify::App resource creates Apps in the Amplify Console. An App is a collection of branches.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplify.apps_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="access_token" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="app_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="auto_branch_creation_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="basic_auth_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="build_spec" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_headers" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="custom_rules" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="default_domain" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enable_branch_auto_deletion" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_variables" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="iam_service_role" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="oauth_token" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="platform" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="repository" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
Lists all <code>apps</code> in a region.
```sql
SELECT
region,
arn
FROM aws.amplify.apps_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>apps_list_only</code> resource, see <a href="/providers/aws/amplify/apps/#permissions"><code>apps</code></a>


