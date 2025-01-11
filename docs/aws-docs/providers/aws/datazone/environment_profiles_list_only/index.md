---
title: environment_profiles_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_profiles_list_only
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

Lists <code>environment_profiles</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/environment_profiles/"><code>environment_profiles</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_profiles_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>AWS Datazone Environment Profile is pre-configured set of resources and blueprints that provide reusable templates for creating environments.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.environment_profiles_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td>The ID of the Amazon DataZone domain in which this environment profile is created.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of this Amazon DataZone environment profile.</td></tr>
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
Lists all <code>environment_profiles</code> in a region.
```sql
SELECT
region,
domain_id,
id
FROM aws.datazone.environment_profiles_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>environment_profiles_list_only</code> resource, see <a href="/providers/aws/datazone/environment_profiles/#permissions"><code>environment_profiles</code></a>

