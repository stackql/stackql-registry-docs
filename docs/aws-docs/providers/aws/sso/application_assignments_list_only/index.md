---
title: application_assignments_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - application_assignments_list_only
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

Lists <code>application_assignments</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/application_assignments/"><code>application_assignments</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>application_assignments_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for SSO application access grant to a user or group.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.sso.application_assignments_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="application_arn" /></td><td><code>string</code></td><td>The ARN of the application.</td></tr>
<tr><td><CopyableCode code="principal_type" /></td><td><code>string</code></td><td>The entity type for which the assignment will be created.</td></tr>
<tr><td><CopyableCode code="principal_id" /></td><td><code>string</code></td><td>An identifier for an object in IAM Identity Center, such as a user or group</td></tr>
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
Lists all <code>application_assignments</code> in a region.
```sql
SELECT
region,
application_arn,
principal_type,
principal_id
FROM aws.sso.application_assignments_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>application_assignments_list_only</code> resource, see <a href="/providers/aws/sso/application_assignments/#permissions"><code>application_assignments</code></a>

