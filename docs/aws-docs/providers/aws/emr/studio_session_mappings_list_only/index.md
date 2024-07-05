---
title: studio_session_mappings_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - studio_session_mappings_list_only
  - emr
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

Lists <code>studio_session_mappings</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/studio_session_mappings/"><code>studio_session_mappings</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>studio_session_mappings_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.emr.studio_session_mappings_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="identity_name" /></td><td><code>string</code></td><td>The name of the user or group. For more information, see UserName and DisplayName in the AWS SSO Identity Store API Reference. Either IdentityName or IdentityId must be specified.</td></tr>
<tr><td><CopyableCode code="identity_type" /></td><td><code>string</code></td><td>Specifies whether the identity to map to the Studio is a user or a group.</td></tr>
<tr><td><CopyableCode code="session_policy_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) for the session policy that will be applied to the user or group. Session policies refine Studio user permissions without the need to use multiple IAM user roles.</td></tr>
<tr><td><CopyableCode code="studio_id" /></td><td><code>string</code></td><td>The ID of the Amazon EMR Studio to which the user or group will be mapped.</td></tr>
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
Lists all <code>studio_session_mappings</code> in a region.
```sql
SELECT
region,
studio_id,
identity_type,
identity_name
FROM aws.emr.studio_session_mappings_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>studio_session_mappings_list_only</code> resource, see <a href="/providers/aws/emr/studio_session_mappings/#permissions"><code>studio_session_mappings</code></a>


