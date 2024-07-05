---
title: applications_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - applications_list_only
  - sso
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
<tr><td><b>Description</b></td><td>Resource Type definition for Identity Center (SSO) Application</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sso.applications_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name you want to assign to this Identity Center (SSO) Application</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description information for the Identity Center (SSO) Application</td></tr>
<tr><td><CopyableCode code="instance_arn" /></td><td><code>string</code></td><td>The ARN of the instance of IAM Identity Center under which the operation will run</td></tr>
<tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td>The Application ARN that is returned upon creation of the Identity Center (SSO) Application</td></tr>
<tr><td><CopyableCode code="application_provider_arn" /></td><td><code>string</code></td><td>The ARN of the application provider under which the operation will run</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>Specifies whether the application is enabled or disabled</td></tr>
<tr><td><CopyableCode code="portal_options" /></td><td><code>object</code></td><td>A structure that describes the options for the portal associated with an application</td></tr>
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
Lists all <code>applications</code> in a region.
```sql
SELECT
region,
application_arn
FROM aws.sso.applications_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>applications_list_only</code> resource, see <a href="/providers/aws/sso/applications/#permissions"><code>applications</code></a>


