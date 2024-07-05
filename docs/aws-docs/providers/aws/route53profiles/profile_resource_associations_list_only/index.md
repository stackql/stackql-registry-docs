---
title: profile_resource_associations_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - profile_resource_associations_list_only
  - route53profiles
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

Lists <code>profile_resource_associations</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/profile_resource_associations/"><code>profile_resource_associations</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>profile_resource_associations_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Route53Profiles::ProfileResourceAssociation</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.route53profiles.profile_resource_associations_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="profile_id" /></td><td><code>string</code></td><td>The ID of the profile that you associated the resource to that is specified by ResourceArn.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Primary Identifier for Profile Resource Association</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of an association between the Profile and resource.</td></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The arn of the resource that you associated to the Profile.</td></tr>
<tr><td><CopyableCode code="resource_properties" /></td><td><code>string</code></td><td>A JSON-formatted string with key-value pairs specifying the properties of the associated resource.</td></tr>
<tr><td><CopyableCode code="resource_type" /></td><td><code>string</code></td><td>The type of the resource associated to the Profile.</td></tr>
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
Lists all <code>profile_resource_associations</code> in a region.
```sql
SELECT
region,
id
FROM aws.route53profiles.profile_resource_associations_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>profile_resource_associations_list_only</code> resource, see <a href="/providers/aws/route53profiles/profile_resource_associations/#permissions"><code>profile_resource_associations</code></a>


