---
title: group_profiles_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - group_profiles_list_only
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

Lists <code>group_profiles</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/group_profiles/"><code>group_profiles</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>group_profiles_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Group profiles represent groups of Amazon DataZone users. Groups can be manually created, or mapped to Active Directory groups of enterprise customers. In Amazon DataZone, groups serve two purposes. First, a group can map to a team of users in the organizational chart, and thus reduce the administrative work of a Amazon DataZone project owner when there are new employees joining or leaving a team. Second, corporate administrators use Active Directory groups to manage and update user statuses and so Amazon DataZone domain administrators can use these group memberships to implement Amazon DataZone domain policies.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.group_profiles_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The identifier of the Amazon DataZone domain in which the group profile is created.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone group profile.</td></tr>
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
Lists all <code>group_profiles</code> in a region.
```sql
SELECT
region,
domain_id,
id
FROM aws.datazone.group_profiles_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>group_profiles_list_only</code> resource, see <a href="/providers/aws/datazone/group_profiles/#permissions"><code>group_profiles</code></a>

