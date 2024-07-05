---
title: user_profiles_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - user_profiles_list_only
  - datazone
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

Lists <code>user_profiles</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/user_profiles/"><code>user_profiles</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_profiles_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A user profile represents Amazon DataZone users. Amazon DataZone supports both IAM roles and SSO identities to interact with the Amazon DataZone Management Console and the data portal for different purposes. Domain administrators use IAM roles to perform the initial administrative domain-related work in the Amazon DataZone Management Console, including creating new Amazon DataZone domains, configuring metadata form types, and implementing policies. Data workers use their SSO corporate identities via Identity Center to log into the Amazon DataZone Data Portal and access projects where they have memberships.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.user_profiles_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="details" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The identifier of the Amazon DataZone domain in which the user profile is created.</td></tr>
<tr><td><CopyableCode code="domain_identifier" /></td><td><code>string</code></td><td>The identifier of the Amazon DataZone domain in which the user profile would be created.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone user profile.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of the user profile.</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the user profile.</td></tr>
<tr><td><CopyableCode code="user_identifier" /></td><td><code>string</code></td><td>The ID of the user.</td></tr>
<tr><td><CopyableCode code="user_type" /></td><td><code>string</code></td><td>The type of the user.</td></tr>
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
Lists all <code>user_profiles</code> in a region.
```sql
SELECT
region,
domain_id,
id
FROM aws.datazone.user_profiles_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>user_profiles_list_only</code> resource, see <a href="/providers/aws/datazone/user_profiles/#permissions"><code>user_profiles</code></a>


