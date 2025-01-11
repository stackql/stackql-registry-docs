---
title: organization_conformance_packs_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - organization_conformance_packs_list_only
  - config
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

Lists <code>organization_conformance_packs</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/organization_conformance_packs/"><code>organization_conformance_packs</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>organization_conformance_packs_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::Config::OrganizationConformancePack.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.config.organization_conformance_packs_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="organization_conformance_pack_name" /></td><td><code>string</code></td><td>The name of the organization conformance pack.</td></tr>
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
Lists all <code>organization_conformance_packs</code> in a region.
```sql
SELECT
region,
organization_conformance_pack_name
FROM aws.config.organization_conformance_packs_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>organization_conformance_packs_list_only</code> resource, see <a href="/providers/aws/config/organization_conformance_packs/#permissions"><code>organization_conformance_packs</code></a>

